from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

# Network general options
net.setLogLevel('info')
net.setCompiler(p4rt=True)
net.disableArpTables()
net.execScript('python l2_learning_controller.py s1 digest &', reboot=True)
net.execScript('python l2_learning_controller.py s2 digest &', reboot=True)
net.execScript('python l2_learning_controller.py s3 digest &', reboot=True)
net.execScript('python l2_learning_controller.py s4 digest &', reboot=True)

# Network definition
net.addP4RuntimeSwitch('s1')
net.setP4Source('s1','./p4src/l2_learning_digest.p4')
net.addP4RuntimeSwitch('s2')
net.setP4Source('s2','./p4src/l2_learning_digest.p4')
net.addP4RuntimeSwitch('s3')
net.setP4Source('s3','./p4src/l2_learning_digest.p4')
net.addP4RuntimeSwitch('s4')
net.setP4Source('s4','./p4src/l2_learning_digest.p4')
net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')
net.addHost('h5')
net.addHost('h6')
net.addLink('s1', 'h1')
net.addLink('s1', 'h2')
net.addLink('s2', 's1')
net.addLink('s2', 's3')
net.addLink('s3', 'h3')
net.addLink('s3', 'h4')
net.addLink('s3', 's4')
net.addLink('s4', 'h6')
net.addLink('s4', 'h5')

# Assignment strategy
net.l2()

# Nodes general options
net.enablePcapDumpAll()
net.enableLogAll()
net.enableCli()
net.startNetwork()