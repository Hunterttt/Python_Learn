from netmiko import ConnectHandler
import json

SW1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.32.101',
    'username': 'admin',
    'password': '123.com',
}

connect = ConnectHandler(**SW1)
print ("Sucessfully connected to " + SW1['ip'])
interfaces = connect.send_command('show ip int brief', use_textfsm=True)
#interfaces = connect.send_command('show ip int brief')
print (json.dumps(interfaces, indent=2))








