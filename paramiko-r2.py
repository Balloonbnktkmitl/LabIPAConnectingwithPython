import time
import paramiko
import os

USERNAME = os.environ.get('TELNET_USER')
IP = "172.31.103.4"
PATH_KEY = "/home/napp/.ssh/id_r2_rsa"

COMMAND = ['conf t\n',
           'int g0/1\n',
           'vrf forwarding control-data\n',
            'ip address 192.168.2.2 255.255.255.0\n',
            'no shut\n',
            'exit\n',
            'int g0/2\n',
            'vrf forwarding control-data\n',
            'ip address 192.168.3.1 255.255.255.0\n',
            'no shut\n',
            'exit\n',
            'int g0/3\n',
            'vrf forwarding control-data\n',
            'ip address dhcp\n',
            'no shut\n',
            'exit\n']

def connect_ssh(ip, port, username, pathkey, command):
    try:
        privatekey = paramiko.RSAKey.from_private_key_file(pathkey)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port, username, pkey=privatekey, disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']})
        channel = client.invoke_shell()
        for i in command:
            channel.send(i)
            output = channel.recv(65535).decode('utf-8')
            print(output)
            time.sleep(1)
        client.close()
        channel.close()
    except paramiko.SSHException as e:
        print("Connection Failed")
        print(e)
    except Exception as e:
        print(e)

connect_ssh(IP, 22, "admin", PATH_KEY, COMMAND)
