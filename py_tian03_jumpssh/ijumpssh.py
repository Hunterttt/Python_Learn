from jumpssh import SSHSession

# establish ssh connection between your local machine and the jump server
gateway_session = SSHSession('192.168.32.101',username='admin',password='123.com',look_for_keys=False, allow_agent=False).open()

print('pass')
# from jump server, establish connection with a remote server
remote_session = gateway_session.get_remote_session('12.1.1.2',username='cisco',password='123.com',look_for_keys=False, allow_agent=False)

print(remote_session.get_cmd_output('show ip int bri'))


#只支持跳板机是windows或者linux