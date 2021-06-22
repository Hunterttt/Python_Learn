
file = open("/home/hunter/192.168.32.101_show_versions.txt","r")
for line in file.readlines():
        print (line)
file.close()