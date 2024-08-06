import pexpect

PROMPT = '#'
IP = "172.31.103.4"
USERNAME = "admin"
PASSWORD = "cisco"
COMMAND = [
    "configure terminal",
    "interface Loopback0",
    "ip address 172.16.2.2 255.255.255.255",
    "exit",
    "exit"
]

child = pexpect.spawn("telnet " + IP)
child.expect('Username')
child.sendline(USERNAME)
child.expect('Password')
child.sendline(PASSWORD)

child.expect(PROMPT)

for command in COMMAND:
    child.sendline(command)
    child.expect(PROMPT)
    
print("Loopback interface created with IP address")

child.sendline('exit')
