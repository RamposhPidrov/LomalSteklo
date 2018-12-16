from pysnmp.hlapi import *
from ipaddress import *
from datetime import datetime


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

#code section

sysname = (snmp_get_next('public', '192.168.1.106', 161, '1.3.6.1.2.1.1.5.0'))
print(sysname)
'''
for i in range(0,10):
    errorIndication, errorStatus, errorIndex, varBinds = next(g)
    for name, val in varBinds:
        print(name.prettyPrint(), ' ===NEXT===', val.prettyPrint())
'''

list_OID=['1.3.6.1.2.1.4.20.1.1']
def snmp_getnextcmd_next(community, ip, port, OID, file):
    # метод обрабатывает class generator от def snmp_getnext
    # OID - это список OID в виде list_OID = [OID_ipAdEntAddr,OID_ipAdEntIfIndex,OID_ipAdEntNetMask], где переменные строковые значения
    # в виде '1.2.3.4'
    # возвращаем двумерный список со значениями, по количеству OID
    list_result = [] # для формирования списков первого уровня
    list_result2 = [] # итоговый список
    g = (snmp_getnextcmd(community, ip, port, OID[0])) #начинаем с первого OID
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
            file.write(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + ' : ' + 'Error snmp_getnextcmd_next ip = ' + ip + ' OID = '+ OID[0] + '\n')
            print('Error snmp_getnextcmd_next ', False)
            i = i + 1
            flag = False
    list_result2.append(list_result)
    return list_result2




'''
iterator = getCmd(SnmpEngine(),
                  CommunityData('public'),
                  UdpTransportTarget(('demo.snmplabs.com', 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:  # SNMP engine errors
    print(errorIndication)
else:
    if errorStatus:  # SNMP agent errors
        print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
    else:
        for varBind in varBinds:  # SNMP response contents
            print(' = '.join([x.prettyPrint() for x in varBind]))

###############################################################################

def snmp_getnextcmd(community, ip, port, OID):
    # type class 'generator' errorIndication, errorStatus, errorIndex, result[3]
    # метод next для получения значений по порядку, одного за другим с помощью next()
    return (nextCmd(SnmpEngine(),
                    CommunityData(community),
                    UdpTransportTarget((ip, port)),
                    ContextData(),
                    ObjectType(ObjectIdentity(OID))))

g = (snmp_getnextcmd('public', 'demo.snmplabs.com', 161, '1.3.6.1.2.1.4.20.1.1'))
print(g)
errorIndication, errorStatus, errorIndex, varBinds = next(g)

for i in range(0,10):
    errorIndication, errorStatus, errorIndex, varBinds = next(g)
    for name, val in varBinds:
        print(name.prettyPrint(), ' ===NEXT===', val.prettyPrint())

print('\n')
for name,val in varBinds:
        print(name.prettyPrint(),' ====== ',val.prettyPrint())

'''


'''
# var section

#snmp
community_string = 'derfnutfo'  # From file
ip_address_host = '192.168.88.1'  # From file
port_snmp = 161
OID_sysName = '1.3.6.1.2.1.1.5.0'  # From SNMPv2-MIB hostname/sysname

# function section

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

#code section

sysname = (snmp_get_next(community_string, ip_address_host, port_snmp, OID_sysName))
print('hostname= ' + sysname)
'''