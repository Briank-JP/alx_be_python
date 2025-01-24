class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
    

class EBook(Book):
    def __init__(self, filesize:int, title:str, author:str):
        super().__init__(title, author)
        self.filesize = filesize
    
class PrintBook(Book):
    def __init__(self, title:str, author:str, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count


class  Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"{book.title} by {book.author}, {book.filesize}MB")
            elif isinstance(book, PrintBook):
                print(f"{book.title} by {book.author}, {book.page_count} pages")
            else:
                print(f"{book.title} by {book.author}")
