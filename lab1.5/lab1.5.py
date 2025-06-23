import glob

files_list = glob.glob("lab1.5/config_files/*.log")
ip_addresses_list = []
for file in files_list:
    openedFiled = open(file)
    lines = openedFiled.readlines()

    for line in lines: 
        editedLine = line.strip()
        if editedLine.startswith("ip address"):
            ip_addresses_list.append(editedLine)
        
list_without_doubles = sorted(list(set(ip_addresses_list)))

print(list_without_doubles)