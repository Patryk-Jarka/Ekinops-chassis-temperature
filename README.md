Ekinops---chassis-temperature

For correct use is required library "pysnmp" -> https://pypi.org/project/pysnmp/

Script is for use as external check in zabbix for get chassis temperature DWDM Ekinops C600HC. If you want use in zabbix move this script to:/usr/lib/zabbix/externalscripts and configure item.

For request about temp is OID used: 1.3.6.1.4.1.20044.45.3.1.64.0 (OID from official Ekinops Docs for C600HC) 

Script default using v2c version SNMP

Script take 2 arguments in command line: get_chassis_temp.py <HOST_IP> <SNMP_COMMUNITY> 

Where:

<HOST_IP> - IP address your Ekinops device
<SNMP_COMMUNITY> - SNMP Community for Ekinops device (default in v2c verion in use)




