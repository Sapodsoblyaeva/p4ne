import re
import ipaddress
import glob

ip_address_regex = "^(([A-z]{2}\ [A-z]{7})\ ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$"

files_list = glob.glob("lab1.6/config_files/*.log")

ip_lines_list = []

ip_interfaces_list = []

def stringToIPaddress(str):
    m = re.match(ip_address_regex, str)

    if m: 
        ip_address = m.group(3)
        mask = m.group(4)
        interface = ipaddress.IPv4Interface(f'{ip_address}/{mask}')
        return interface
    else: 
        return None
            
for file in files_list:
    openedFiled = open(file)
    lines = openedFiled.readlines()
    
    for line in lines: 
        editedLine = line.strip()
        if editedLine.startswith("ip address"):
            interface = stringToIPaddress(editedLine)
            if interface is not None:
                ip_interfaces_list.append(interface)
        
list_without_doubles = sorted(list(set(ip_interfaces_list)))

for int in list_without_doubles:
    print(int)

