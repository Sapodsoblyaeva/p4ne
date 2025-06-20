import random
import ipaddress


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        self.getNewRandomNetwork()
        
    def __repr__(self):
        return   "'%s'" % self
        
    def getNewRandomNetwork(self): 
        self.ip = random.randint(0x0B000000, 0xDF000000)
        self.mask = random.randint(8, 24)
        self.network = (self.ip, self.mask)
        ipaddress.IPv4Network.__init__(self, self.network, strict=False)
        
    def regular(self): 
        return not self.is_private

    def randomNet(self):
        if self.regular(): 
            return self
        else: 
            self.getNewRandomNetwork()
            return self.randomNet()
    

net1 = IPv4RandomNetwork()
print(net1.randomNet())

def value_ip(net): 
    print(int(net.netmask)*2**32 + int(net.network_address))
    return int(net.netmask)*2**32 + int(net.network_address)
    
    

net_list = []
for i in range(0, 20): 
    net = IPv4RandomNetwork()
    net_list.append(net)


new_net_list = sorted(net_list, key=value_ip)
print(new_net_list)

