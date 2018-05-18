
"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
import fileinput

def initHistory(length):
	history = []
	for i in range(length):
		temp = []
		for j in range(length):
			temp.append(0)
		history.append(temp)
	return history

def initTopo(filePath):
	#calculate the lineNumber of text
	res = []
	for line in fileinput.input(filePath):
		#remove the line-break
		line = line.replace("\r", "")
       		line = line.replace("\n", "")
		temp = []
		for char in line:
			#transform string into integer
			temp.append(int(char))
		res.append(temp)
	print(res)
	return res

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        #initilize netTopo /home/zhl/mininet/custom/test.txt
        topo = initTopo('/home/zhl/mininet/custom/topo.txt')
        length = len(topo)
	history = initHistory(length)
        #arrayList of host
        switches = []
	hosts = []
        for num in range(length):
        	switches.append(self.addSwitch('s' + str(num + 1)))
		hosts.append(self.addHost('h' + str(num + 1)))
	
	for num in range(length):
		self.addLink(hosts[num], switches[num])
	
	i = 0
        for horizontal in topo:
        	j = 0
        	for each in horizontal:
        		if each == 1:
				if(history[i][j] == 0):
        				self.addLink(switches[i],switches[j])
					history[i][j] = 1
					history[j][i] = 1
					
        		j = j + 1
        	i = i + 1

topos = { 'mytopo': ( lambda: MyTopo() ) }


