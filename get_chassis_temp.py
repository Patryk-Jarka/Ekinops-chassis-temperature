from pysnmp.hlapi import SnmpEngine, CommunityData, UdpTransportTarget,\
                         ContextData, ObjectType, ObjectIdentity, getCmd
import sys
host_IP=sys.argv[1]
community_arg=sys.argv[2]+'21'                         # '21' -> default slot for get info about chassis temperature (CH600HC)

iterator = getCmd(
    SnmpEngine(),
    CommunityData(community_arg, mpModel=1),           # mpModel for snmp v2c - value -> 1
    UdpTransportTarget((host_IP, 161)),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.4.1.20044.45.3.1.64.0'))
)

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('{} at {}'.format(errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

def return_value():
    for oid, val in varBinds:
        return(str((f'{oid.prettyPrint()} = {val.prettyPrint()}')))

value=return_value()
value=value.replace('SNMPv2-SMI::enterprises.20044.45.3.1.64.0 = ','')
dec_value=int(value)
hex_value=hex(dec_value)
msb=hex_value[2]+hex_value[3]
lsb=hex_value[4]+hex_value[5]
msb_to_dec=int(msb,base=16)
lsb_to_dec=int(lsb,base=16)
temp=float(msb_to_dec + float(lsb_to_dec/256))
temp_round=round(temp,1)
print(temp_round)


