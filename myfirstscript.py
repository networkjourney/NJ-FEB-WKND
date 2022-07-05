from netmiko import ConnectHandler
from netmiko.snmp_autodetect import SNMPDetect
import logging
logging.basicConfig(filename='snmpautodetect.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
multidevice = open(r"C:\Users\njexec\Music\multidevi.txt")
devicelist = multidevice.read().splitlines()
#print(devicelist)
cred123 = open(r"C:\Users\njexec\Music\ciscocred.txt")
newcred123 = cred123.read().splitlines()
#print(newcred123)
user1234 = newcred123[0]
#print(user1234)
pass1234 = newcred123[1]
#print(pass1234)
for abc in devicelist:
    snmpstring123 = input("enter your SNMP v2c string for RO:")
    back1234 = SNMPDetect(abc, snmp_version="v2c", community=snmpstring123)
    backfilllll123 = back1234.autodetect()
    print(backfilllll123)
    deviceinfo123 = {
        "device_type": backfilllll123,
        "ip": abc,
        "username": user1234,
        "password": pass1234
    }
    ssh123 = ConnectHandler(**deviceinfo123)
    print("*"*10 + "Connecting to " + abc)
    cli123 = ssh123.send_command("show ip int br")
    print(cli123)