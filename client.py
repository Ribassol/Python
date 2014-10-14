import Pyro.core


try:
    #remExec = Pyro.core.getProxyForURI("PYRONAME://libNuno")
    remExec = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/libNuno")

    try:
        remExec.insert_book("M", "Quim", 2014)
        print "Eu, cliente, acabei de inserir um livro!"
        remExec.search_book(2, "M")
        print "Eu, cliente, acabei de procurar um livro!"

    except:
        print 'ERRO: Nao consigo usar objectos remotos!'

except:
    print 'ERRO: Nao estabeleci ligacao!'
