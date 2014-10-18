#!/usr/bin/env python

# "pyro-nsc listall" : este comando serve para listar
# todos os objectos registados no name server

import library
import Pyro.core
import Pyro.naming


class remoteLibrary(Pyro.core.ObjBase, library.library):
	def __init__(self, name, ns, myName):
		Pyro.core.ObjBase.__init__(self)
		library.library.__init__(self, name)
		self.ns=ns
		self.myName=myName

		servlist = ns.list(':libraries')
		print servlist[0][0] + "-----"

	def listBooks(self, name, local=False):
                if local == False:
                if local == True:
                        
       

def main():
	myName=':libraries.BookLib70268-1'
	
	Pyro.core.initServer()
	
	locator = Pyro.naming.NameServerLocator()
	ns = locator.getNS()
	bd = remoteLibrary("mylib",ns, myName)
	print ns
	print "\n\n\n\n"
	servlist = ns.list(':libraries')
	print servlist[0][0]
	try:
		ns.createGroup(':libraries')
	except:
		pass
	daemon = Pyro.core.Daemon(host = "192.168.2.3")
	daemon.useNameServer(ns)

       
	
	try:
		daemon.connect(bd,myName)
	except:
		pass
	
	try:
	    daemon.requestLoop()
	finally:
	    daemon.shutdown(True)

if __name__=="__main__":
    main() 
