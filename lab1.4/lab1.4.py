import random
import ipaddress


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        self.getNewRandomNetwork()
        
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


