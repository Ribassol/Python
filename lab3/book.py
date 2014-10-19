class book:
    def __init__(self, title, author, ID, year):
        self.title = title
        self.author = author
        self.ID = ID
        self.year = year

    def __str__(self):
        return "Title: "+self.title+".\nAuthor: "+self.author
    


b= book("po", "tt", 10,10)
