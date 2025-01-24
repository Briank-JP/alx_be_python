class Book:
    def __init__(self, title:str, author:str, year:int):
        self.title = title
        self.author = author
        self.year = year
       
    def __del__(self):
        print(f"Deleting {self.title}")

    def display_info(self):
        print(f'\n{self.title} - {self.author} - {self.year}')

    def __str__(self):
        return f'{self.title} by {self.author}, published in {self.year}'
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    

# my_book = Book('7 habbits', 'stephen covey', 2009)
# my_book.display_info

# del my_book