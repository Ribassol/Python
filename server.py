import Pyro.core
import Pyro.naming
from library import *

def main_1():
    Pyro.core.initServer()

    daemon = Pyro.core.Daemon() 
    uri = daemon.connect(library(), "libNuno")

    print "The daemon runs on port:",daemon.port
    print "The object's uri is:",uri

    daemon.requestLoop()


def main_2():
    Pyro.core.initServer()

    #########################################
    #locator = Pyro.naming.NameServerLocator()
    #ns = locator.getNS(host = 'hostname', port = 9090)
    #ns = locator.getNS()
    #########################################

    daemon = Pyro.core.Daemon()

    #daemon.useNameServer(ns)
    
    uri = daemon.connect(library(), "libNuno")

    print "The daemon runs on port:",daemon.port
    print "The object's uri is:",uri

    try:
        daemon.requestLoop()

    finally:
        daemon.shutdown()
        print "Server desligado. Adeus!"

main_1()    
#main_2()
