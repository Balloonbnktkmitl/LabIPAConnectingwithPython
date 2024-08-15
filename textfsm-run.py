import textfsm
from netmiko import ConnectHandler
import argparse

router = {
    "device_type": "cisco_ios",
    "host": "172.31.103.4",
    "username": "admin",
    "password": "cisco",
}

def normalize_output(interface_name):
    interface_name = interface_name.lower()
    if interface_name.startswith("g"):
        return "gigabitethernet" + interface_name[1:]
    elif interface_name.startswith("f"):
        return "fastethernet" + interface_name[1:]
    return interface_name

parser = argparse.ArgumentParser(description="Interface name")
parser.add_argument("interfacename", help="Interface name")
args = parser.parse_args()

interfacename = normalize_output(args.interfacename)

Connection = ConnectHandler(**router)
Connection.enable()

output = Connection.send_command("show ip int brief")

Connection.disconnect()

with open("templates/router-textfsm.tpl") as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(output)
    
found = False

for entry in result:
    if entry[0].lower() == interfacename:
        print(f"Interface: {entry[0]}, IP: {entry[1]}, Status: {entry[2]}")
        found = True
        break

if not found:
    print(f"Interface {interfacename} not found")

# for result in result:
#     print(f"Interface: {result[0]}, IP: {result[1]}, Status: {result[2]}")