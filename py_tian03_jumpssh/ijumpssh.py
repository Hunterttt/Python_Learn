from jumpssh import SSHSession

# establish ssh connection between your local machine and the jump server
gateway_session = SSHSession('192.168.32.101',username='admin',password='123.com').open()

# from jump server, establish connection with a remote server
remote_session = gateway_session.get_remote_session('12.1.1.2',username='cisco',password='123.com')

print(remote_session.get_cmd_output('show ip int bri'))