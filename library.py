import Pyro.core
from book import *

class library(Pyro.core.ObjBase):

    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
        self.library = {}
        self.num_books = 0

    def insert_book(self, title, author, year):
        self.library[self.num_books] = book(title, author, self.num_books, year)
        self.num_books += 1

    def search_book(self, search_by, key):
        if search_by == 1:
            if key in self.library.keys():
                print self.library[key]
                return self.library[key]

            print "Id not found"
            return None


        if search_by == 2:
            for i in self.library.values():
                if i.title == key:
                    print i
                    return i

            print "Title not found!"
            return None

    def search_author(self, author):
        list=[]
        for i in self.library.values():
            if i.author == author:
                list.append(i.title)

        return list

    
l= library()

l.insert_book("A", "Manel",1999)
l.insert_book("B", "Toni",1996)
l.insert_book("F", "Ze",2005)
l.insert_book("Z", "Manel",1994)
