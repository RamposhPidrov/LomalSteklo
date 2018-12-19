from pysnmp.hlapi import *
import pysnmp
import logging
import datetime
from ipaddress import *


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
        return self.get_oid(ObjectIdentity('SNMPv2-MIB', 'sysDescr',0))

    def get_ifrouter(self): #маршрутиризатор ли устройство
        errorIndication, errorStatus, errorIndex, varBinds = next(self.get_cmd((ObjectIdentity('IP-MIB', 'ipForwarding',0).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@'))))
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
                                             #Результат: [индекс, айпи, маска, название, тип интерфейса, MTU, скорость, физический адресс]
            templist=[]
            templist.append(ind)
            templist.append(iplist[ind-1])
            templist.append(masklist[ind-1])
            errorIndication, errorStatus, errorIndex,varBinds = next(getCmd(SnmpEngine(),
                                      CommunityData(self.community),
                                      UdpTransportTarget((self.ipaddr, self.port)),
                                      ContextData(),
                                      ObjectType(ObjectIdentity('IF-MIB', 'ifDescr',ind)),
                                      ObjectType(ObjectIdentity('IF-MIB', 'ifType',ind)),
                                      ObjectType(ObjectIdentity('IF-MIB', 'ifMtu',ind)),
                                      ObjectType(ObjectIdentity('IF-MIB', 'ifSpeed',ind)),
                                      ObjectType(ObjectIdentity('IF-MIB', 'ifPhysAddress',ind)),
                                      ))
            for varBind in varBinds:
                templist.append(' = '.join([x.prettyPrint() for x in varBind]).split(' ')[-1])
                print(' = '.join([x.prettyPrint() for x in varBind]))

            resultlist.append(templist)
        return resultlist

test = Connection('192.168.43.50', 'public', 161)

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