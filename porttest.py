
from pysnmp.hlapi import *
from ipaddress import *
from datetime import datetime
import os

def snmp_getcmd(community, ip, port, OID):
    return (getCmd(SnmpEngine(),
                   CommunityData(community),
                   UdpTransportTarget((ip, port)),
                   ContextData(),
                   ObjectType(ObjectIdentity(OID))))

def snmp_get_next(community, ip, port, OID):
    errorIndication, errorStatus, errorIndex, varBinds = next(snmp_getcmd(community, ip, port, OID))
    for name, val in varBinds:
        return (val.prettyPrint())

list_OID=['1.3.6.1.2.1.4.20.1.1']
def snmp_getnextcmd_next(community, ip, port, OID):
    # метод обрабатывает class generator от def snmp_getnext
    # OID - это список OID в виде list_OID = [OID_ipAdEntAddr,OID_ipAdEntIfIndex,OID_ipAdEntNetMask], где переменные строковые значения
    # в виде '1.2.3.4'
    # возвращаем двумерный список со значениями, по количеству OID
    list_result = [] # для формирования списков первого уровня
    list_result2 = [] # итоговый список
    g = (snmp_get_next(community, ip, port, OID[0])) #начинаем с первого OID
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
            '''
            if errors(errorIndication, errorStatus, errorIndex, ip_address_host, file):
                if str(varBinds).find(oid) != -1:
                    i = 0
                    for name, val in varBinds:
                        list_result.append(val.prettyPrint())
                else:
                    i = i + 1
                    flag = False
            else:
            '''
            #file.write(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + ' : ' + 'Error snmp_getnextcmd_next ip = ' + ip + ' OID = '+ OID[0] + '\n')
            #print('Error snmp_getnextcmd_next ', False)
            i = i + 1
            flag = False
    list_result2.append(list_result)
    return list_result2

print(snmp_getnextcmd_next('public','192.168.43.152',161,list_OID))
