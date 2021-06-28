from netmiko import ConnectHandler
import json
from pprint import pprint

SW1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.32.101',
    'username': 'admin',
    'password': '123.com',
}

connect = ConnectHandler(**SW1)
print ("Sucessfully connected to " + SW1['ip'])
interfaces = connect.send_command('show version', use_genie = True)
#interfaces = connect.send_command('show version')

#print (json.dumps(interfaces, indent=2))
pprint(interfaces)