class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True
class Library:
    def __init__(self):
        self.books = []
    def add_book(self,title,author):
        new_book = Book(title,author)
        self.books.append(new_book)
        self.save_books()
    def save_books(self):
        for b in self.books:
            print(b)
    def save_books(self):
        with open('library.txt','w') as f:
            for book in self.books:
                line = f'{book.title},{book.author} , is available\n'
                f.write(line)
l = Library()
l.add_book('Harry Portter','JK Rowling')
l.add_book('Lords of rings','Tolkien')
l.save_books()
