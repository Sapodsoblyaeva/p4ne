import pprint
import paramiko, time
import re


BUF_SIZE = 20000
TIMEOUT = 1

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect("10.31.70.209", username="restapi", password="j0sg1280-7@", look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()


session.send("\n")
session.recv(BUF_SIZE)
session.send("terminal length 0\n")
time.sleep(TIMEOUT)
session.send("\n\n\n")
session.recv(BUF_SIZE)
session.send("show interface\n")


time.sleep(TIMEOUT*2)
out = session.recv(BUF_SIZE).decode()

for l in re.finditer("((GigabitEthernet|Loopback)+[0-9] )", out): 
    print(l.group(0))

for s in re.finditer("([0-9]+ packets )(input|output),+ ([0-9]+ bytes)", out): 
    print(s.group(0))

session.close()

