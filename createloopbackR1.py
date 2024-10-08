import pexpect
import getpass
import os

PROMPT = '#'
IP = "172.31.103.3"
# USERNAME = "admin"
# PASSWORD = "cisco"
USERNAME = os.environ.get('TELNET_USER')
PASSWORD = os.environ.get('TELNET_PASSWORD')
COMMANDIP ="ip address 172.16.1.1 255.255.255.255"

try:
    child = pexpect.spawn("telnet " + IP)
    child.expect('Username')
    child.sendline(USERNAME)
    child.expect('Password')
    child.sendline(PASSWORD)
    child.expect(PROMPT)
except:
    print("Telnet failed")
    
child.sendline('conf t')
child.expect("\(config\)" + PROMPT)
child.sendline('int loopback 0')
child.expect("\(config-if\)" + PROMPT)
child.sendline("vrf forwarding control-data")
child.expect("\(config-if\)" + PROMPT)
child.sendline(COMMANDIP)

print("Loopback interface created with IP address")

child.sendline('exit')
