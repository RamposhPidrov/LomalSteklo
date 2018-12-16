from pysnmp.hlapi import *
import logging


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

    def snmp_getcmd(self, OID):
        return (getCmd(SnmpEngine(),
                       CommunityData(self.community),
                       UdpTransportTarget((self.ipaddr, self.port)),
                       ContextData(),
                       ObjectType(ObjectIdentity(OID))))

    def get_oid(self, OID):
        errorIndication, errorStatus, errorIndex, varBinds = next(self.snmp_getcmd(OID))
        for name, val in varBinds:
            return (val.prettyPrint())

    def snmp_getnextcmd(self, OID):
        return (nextCmd(SnmpEngine(),
                        CommunityData(self.community),
                        UdpTransportTarget((self.ipaddr, self.port)),
                        ContextData(),
                        ObjectType(ObjectIdentity(OID))))

    def set_oid(self, OID):

        return

    def get_baseinfo(self): #Linux typidor 3.10.0-862.14.4.el7.x86_64 #1 SMP Wed Sep 26 15:12:11 UTC 2018 x86_64
        return test.get_oid('1.3.6.1.2.1.1.1.0')

    def snmp_getnextcmd_next(self, OID, file):
        # метод обрабатывает class generator от def snmp_getnext
        # OID - это список OID в виде list_OID = [OID_ipAdEntAddr,OID_ipAdEntIfIndex,OID_ipAdEntNetMask], где переменные строковые значения
        # в виде '1.2.3.4'
        # возвращаем двумерный список со значениями, по количеству OID
        list_result = []  # для формирования списков первого уровня
        list_result2 = []  # итоговый список
        g = (snmp_getnextcmd(community, ip, port, OID[0]))  # начинаем с первого OID
        varBinds = 0
        flag = True
        for oid in list_OID:
            if varBinds != 0:
                for name, val in varBinds:
                    list_result2.append(list_result)
                    list_result = []
                    list_result.append(val.prettyPrint())
            i = 0
            while i <= 0:  # по списку
                errorIndication, errorStatus, errorIndex, varBinds = next(g)
                if errors(errorIndication, errorStatus, errorIndex, ip_address_host, file):
                    if str(varBinds).find(oid) != -1:
                        i = 0
                        for name, val in varBinds:
                            list_result.append(val.prettyPrint())
                    else:
                        i = i + 1
                        flag = False
                else:
                    file.write(datetime.strftime(datetime.now(),
                                                 "%Y.%m.%d %H:%M:%S") + ' : ' + 'Error snmp_getnextcmd_next ip = ' + ip + ' OID = ' +
                               OID[0] + '\n')
                    print('Error snmp_getnextcmd_next ', False)
                    i = i + 1
                    flag = False
        list_result2.append(list_result)
        return list_result2








test = Connection('192.168.1.107', 'public', 161)
print(test.snmp_getnextcmd('1.3.6.1.2.1.4.20.1.1'))

g = (test.snmp_getnextcmd('1.3.6.1.2.1.4.20.1.1'))
print(g)
errorIndication, errorStatus, errorIndex, varBinds = next(g)
for i in range(0,20):
    for name,val in varBinds:
        print(name.prettyPrint(),' ====== ',val.prettyPrint())
    errorIndication, errorStatus, errorIndex, varBinds = next(g)

print('========')
for name,val in varBinds:
        print(name.prettyPrint(),' ====== ',val.prettyPrint())