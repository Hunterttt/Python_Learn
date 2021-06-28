import ansible_runner



 

def main():
    r = ansible_runner.run(private_data_dir='/etc/ansible', playbook='test.yml')
    #print("{}: {}".format(r.status, r.rc))




if __name__ == '__main__':
    main()