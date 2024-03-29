#!/usr/bin/python 

from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.cli import CLI


class MyTopology(Topo): 

    """
    A basic topology 
    """
    def __init__(self): 
        Topo.__init__(self)
        
        # Set Up Topology Here 
        switch = self.addSwitch('s1')
        host1 = self.addHost('h1') 

        self.addLink(host1, switch)

if __name__ == '__main__': 
    """
    If this script is run as an executable (by chmod +x), this is what it will do 
    """
    topo = MyTopology()
    net = Mininet( topo=topo ) 
    net.start()
    ## Creates the topology
    ## Loads the topology ## Starts Mininet
    # Commands here will run on the simulated topology CLI(net)
    net.stop() ## Stops Mininet
