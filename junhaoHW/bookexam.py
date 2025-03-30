class Book:
    def __init__(self, title:str, isbn:str):
        self.title = title
        self.isbn = isbn

    def getTitle(self):
        return self.title
    
    def getIsbn(self):
        return self.isbn
    
    def getBookType(self):
        raise NotImplementedError("This method should be implemented in subclasses")

class EBook(Book):
    def __init__(self, title:str, isbn:str, url:str):
        super().__init__(title, isbn)
        self.url = url

    def getUrl(self):
        return self.url
    
    def getBookType(self):
        return "E-Book"

if __name__ == "__main__":
    print("1")
    mybook = EBook("Python", "No", "google.com")
    Type = mybook.getBookType()
    print(Type)