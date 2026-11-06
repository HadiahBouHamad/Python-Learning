class Book:
    def __init__(self, title, author, year, is_checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out

    def checkout(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author} ('Checked out:' {self.is_checked_out})"


class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)

    def list_books(self):
        for book in self.collection:
            print(f"{book.title} by {book.author} year {book.year} - 'Checked out'  {book.is_checked_out }")

    def find_book(self,title):
        for book in self.collection:            
             if book.title.lower() == title.lower():
                return book
        return None
    
    def available_books(self):
        return [book.title for book in self.collection if not book.is_checked_out]

b1 = Book("1984", "George Orwell", 1949)
b2 = Book("The Alchemist", "Paulo Coelho", 1988)


lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.list_books()

b1.checkout()
lib.list_books()

found = lib.find_book("1984")
print(found)  # Should print the book details for "1984"

available = lib.available_books()
print(f'Available books: {", ".join(available)}')  # Should print the titles of available books