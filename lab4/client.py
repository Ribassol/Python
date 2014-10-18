#!/usr/bin/env python

import Pyro.core
import Pyro.naming

def main():
 
	Pyro.core.initClient()
	
	
	locator = Pyro.naming.NameServerLocator()
	ns = locator.getNS()


	## pode-se usar o nome do objecto directamente para encontrar o URI
	#uri = ns.resolve(':libraries.BookLib70268-1')
	#bd = Pyro.core.getAttrProxyForURI(uri)
	#print 'Conectado!\n\n'
	#bd = Pyro.core.getAttrProxyForURI(uri)


        ## caso nao conheca o nome dos objectos, a funcao list() devolve todos os objectos no grupo
        ## ':libraries'
	servlist = ns.list(':libraries')
	print servlist[5][0]
	obj = ns.resolve(":libraries."+servlist[5][0])
	
	bd = Pyro.core.getAttrProxyForURI(obj)
	
	exit = False
	while not exit:
		l = raw_input("add? search? list? quit?")
		l = l.split()
		
		if len(l)==1:
			command = l[0].upper()
			if command=='QUIT':
				exit = True
			elif command == 'ADD':
				l = raw_input('Insert author title and date separated by # :\n')
				processed_line = l.split('#')
				if len(processed_line) ==3:
					print '%s %s %s'% (processed_line[0], processed_line[1], processed_line[2])
					bd.addBook(processed_line[0], processed_line[1], processed_line[2])
			elif command == 'SEARCH':
				l = raw_input('Insert id :\n')
				processed_line = l.split()
				print processed_line[0]
				if len(processed_line) ==1:
					b = bd.searchBook(int(processed_line[0]))
					print b
			elif command == 'LIST':
				l = raw_input('Insert name :\n')
				processed_line = l.split()
				print processed_line[0]
				if len(processed_line) ==1:
					b_list = bd.listBooks(processed_line[0])
					print b_list
				
			else:
				print bd.bib
			
		
		if len(l)==1 and l[0]=='quit':
			exit = True
    
    

if __name__=="__main__":
    main() 
