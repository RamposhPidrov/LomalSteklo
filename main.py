from pysnmp.hlapi import *
import pysnmp
import logging
from datetime import datetime, timedelta
import datetime

#ctrl+alt+shift+J
class Connection:

    def __init__(self, ip, c, p):
        self.ipaddr = ip
        self.community = c
        self.port = p
        return

    def getAllOIDs(self): #вывод всех оидов по корню
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in nextCmd(SnmpEngine(),
                                  CommunityData(self.community),
                                  UdpTransportTarget((self.ipaddr, self.port)),
                                  ContextData(),
                                  ObjectType(ObjectIdentity('1.3')),
                                  lookupMib=False):
            if errorIndication:
                print(errorIndication)
                break
            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
                break
            else:
                for varBind in varBinds:
                    print(' = '.join([x.prettyPrint() for x in varBind]))

    def get_cmd(self, command):
        return (getCmd(SnmpEngine(),
                       CommunityData(self.community),
                       UdpTransportTarget((self.ipaddr, self.port)),
                       ContextData(),
                       ObjectType(command)))

    def get_oid(self, OID): #main cmd, takind next oid
        errorIndication, errorStatus, errorIndex, varBinds = next(self.get_cmd(OID))
        for name, val in varBinds:
            return (val.prettyPrint())

    def snmp_getnextoid(self, OID):
        return (nextCmd(SnmpEngine(),
                        CommunityData(self.community),
                        UdpTransportTarget((self.ipaddr, self.port)),
                        ContextData(),
                        ObjectType(ObjectIdentity(OID))))

    def set_oid(self, OID, new):
        return (setCmd(SnmpEngine(),
                        CommunityData(self.community),
                        UdpTransportTarget((self.ipaddr, self.port)),
                        ContextData(),
                        ObjectType(OID,new)))

    def get_systeminfo(self): #Linux typidor 3.10.0-862.14.4.el7.x86_64 #1 SMP Wed Sep 26 15:12:11 UTC 2018 x86_64
        return self.get_oid(ObjectIdentity('SNMPv2-MIB', 'sysDescr',0).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs'))

    def get_uptime(self):
        ticks = int(self.get_oid(ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')))
        return  datetime.datetime.now() - timedelta(seconds=ticks/100)



    def get_ifrouter(self): #маршрутиризатор ли устройство
        errorIndication, errorStatus, errorIndex, varBinds = next(self.get_cmd((ObjectIdentity('IP-MIB', 'ipForwarding',0).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs'))))
        for varBind in varBinds:
            if(varBind=='notForwarding'):
               return(0)
            else: return(1)

    def get_interfaces(self):
        resultlist=[] #финальный лист листов, каждый лист хранит [индекс, название, айпи, маска]
        iplist=[]
        masklist=[]
        indlist = []  # хранит индексы интерфейсов
        flag=1
        oid_generator = (self.snmp_getnextoid('1.3.6.1.2.1.4.20.1.1'))
        while(flag==1): #получение индексов, ipv4, масок
            errorIndication, errorStatus, errorIndex, varBinds =next(oid_generator)
            if errorIndication:
                return (errorIndication)
            elif errorStatus:
                return ('%s at %s' % (
                errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            else:
                for varbind in varBinds:
                    if(str(varbind).find('mib-2.4.20.1.1')!=-1):
                        iplist.append(str(varbind).split(' ')[-1])
                    if(str(varbind).find('mib-2.4.20.1.2')!=-1):
                        indlist.append(str(varbind).split(' ')[-1])
                    elif (str(varbind).find('mib-2.4.20.1.3') != -1):
                        masklist.append(str(varbind).split(' ')[-1])
                    elif(len(masklist)>0):
                        flag = 0

        for ind in range(1, len(indlist)+1): #получение названия интерфейсов и объединение всего в resultlist
                                             #Результат:
                                             # [
                                             # индекс | айпи | маска | название | состояние | тип интерфейса | MTU | скорость | физический адресс | Sysuptime интерфейса |
                                             #
                                             #Полное число полученных байтов | число полученных unicast пакетов | число полученных broadcast пакетов | Число полученных но отвергнутых пакетов|
                                             #Число пакетов, полученных с ошибкой | Число пакетов, полученных с ошибочным кодом протокола |
                                             #
                                             # Полное число отправленных байтов | число отправленных unicast пакетов | число отпарвленных broadcast пакетов | Число отправленных, но отвергнутых пакетов|
                                             # Число пакетов, отправленных с ошибкой
                                             # ]
            templist=[]
            templist.append(ind)
            templist.append(iplist[ind-1])
            templist.append(masklist[ind-1])
            errorIndication, errorStatus, errorIndex,varBinds = next(getCmd(SnmpEngine(),
                                    CommunityData(self.community),
                                    UdpTransportTarget((self.ipaddr, self.port)),
                                    ContextData(),
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifDescr',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),  ObjectType(ObjectIdentity('IF-MIB', 'ifOperStatus',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifType',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifMtu',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')), ObjectType(ObjectIdentity('IF-MIB', 'ifSpeed',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifPhysAddress',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')), ObjectType(ObjectIdentity('IF-MIB', 'ifLastChange',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),

                                    #полученные пакеты
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')), ObjectType(ObjectIdentity('IF-MIB', 'ifInUcastPkts',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifInNUcastPkts',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifInDiscards',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')), ObjectType(ObjectIdentity('IF-MIB', 'ifInErrors',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifInUnknownProtos',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),

                                    #отправленные пакеты
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifOutOctets',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')), ObjectType(ObjectIdentity('IF-MIB', 'ifOutUcastPkts',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifOutNUcastPkts',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),
                                    ObjectType(ObjectIdentity('IF-MIB', 'ifOutDiscards',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')), ObjectType(ObjectIdentity('IF-MIB', 'ifOutErrors',ind).addMibSource('/opt/mibs/pysnmp').addMibSource('python_packaged_mibs')),
            ))

            if errorIndication:
                return (errorIndication)
            elif errorStatus:
                return ('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            else:
                for varBind in varBinds:
                    templist.append(' '.join([x.prettyPrint() for x in varBind]).split(' ')[-1])

            resultlist.append(templist)
        return resultlist

def get_uptime_loh(ticks):
    return  datetime.datetime.now() - timedelta(seconds=ticks/100)

test = Connection('192.168.1.107', 'public', 161)

import time

print(test.get_interfaces())

#print(test.set_oid('1.3.6.1.2.1.4.20.1.1.1'))

'''
        OID_ipAdEntAddr = '1.3.6.1.2.1.4.20.1.1'  # From SNMPv2-MIB ip адреса
        OID_ifNumber = '1.3.6.1.2.1.2.1.0'  # From RFC1213-MIB количество интерфейсов ifindex
        OID_sysName = '1.3.6.1.2.1.1.5.0'  # From SNMPv2-MIB hostname/sysname
        OID_ipAdEntIfIndex = '1.3.6.1.2.1.4.20.1.2'  # From SNMPv2-MIB ifindex interface
        OID_ipAdEntNetMask = '1.3.6.1.2.1.4.20.1.3'  # From SNMPv2-MIB
        OID_ifAlias = '1.3.6.1.2.1.31.1.1.1.18'  # Desc интерфейса. для получения к OID надо добавить ifindex
        OID_ifName = '1.3.6.1.2.1.31.1.1.1.1'  # название интерфейса к OID надо добавить ifindex
        varBinds = 0        
'''




'''
for varBind in varBinds:
    print(' = '.join([x.prettyPrint() for x in varBind]))



print(test.snmp_getnextoid('1.3.6.1.2.1.4.20.1.1'))

g = (test.snmp_getnextoid('1.3.6.1.2.1.4.20.1.1'))
print(g)
errorIndication, errorStatus, errorIndex, varBinds = next(g)
for i in range(0,20):
    for name,val in varBinds:
        print(name.prettyPrint(),' ====== ',val.prettyPrint())
    errorIndication, errorStatus, errorIndex, varBinds = next(g)

print('========')
for name,val in varBinds:
        print(name.prettyPrint(),' ====== ',val.prettyPrint())
'''