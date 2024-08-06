import telnetlib
import getpass
import os
import time

host = "172.31.103.3"
user = os.environ.get('TELNET_USER')
password = os.environ.get('TELNET_PASSWORD')
tn = telnetlib.Telnet(host, 23, 5)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
time.sleep(1)

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
time.sleep(1)

COMMAND = ['conf t', 
           'int g0/1', 
           'vrf forwarding control data',
           'ip address 192.168.1.1 255.255.255.0',
           'no shut',
           'exit',
           'int g0/2',
            'vrf forwarding control data',
            'ip address 192.168.2.1 255.255.255.0',
            'no shut',
            'exit']

for command in COMMAND:
    tn.write(command.encode('ascii') + b"\n")
    time.sleep(1)

tn.close()

