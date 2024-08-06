import pexpect

PROMPT = '#'
IP = "172.31.103.4"
USERNAME = "admin"
PASSWORD = "cisco"
COMMAND = [
    "configure terminal",
    "interface Loopback0",
    "ip address 172.16.1.1 255.255.255.255",
    "exit",
    "exit"
]

child = pexpect.spawn("telnet" + IP)
child.expect('Username')
child.sendline(USERNAME)
child.expect('Password')
child.sendline(PASSWORD)

child.expect(PROMPT)

for command in COMMAND:
    child.sendline(command)
    child.expect(PROMPT)
    
result = child.before
print(result)
print()
print(result.decode("UTF-8"))

child.sendline('exit')
