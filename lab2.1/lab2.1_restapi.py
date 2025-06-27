import requests
import pprint
import re


headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

r = requests.get("https://10.31.70.209/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces", auth=("restapi", "j0sg1280-7@"), headers=headers, verify=False)

dict = r.json()


for i in dict["Cisco-IOS-XE-interfaces-oper:interfaces"]["interface"]:
    pprint.pprint(i["name"])
    
for i in dict["Cisco-IOS-XE-interfaces-oper:interfaces"]["interface"]:
    pprint.pprint(i["statistics"]["in-unicast-pkts"])
    
for i in dict["Cisco-IOS-XE-interfaces-oper:interfaces"]["interface"]:
    pprint.pprint(i["statistics"]["out-unicast-pkts"])