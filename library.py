class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"'{self.title}' by {self.author} - {self.copies} copies available"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        self.books.append(Book(title, author, copies))
        print(f"Book '{title}' added to the library.")

    def list_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.copies > 0:
                book.copies -= 1
                print(f"You have borrowed '{title}'.")
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.copies += 1
                print(f"Thank you for returning '{title}'.")
                return
        print(f"'{title}' does not belong to this library.")


# Example usage
if __name__ == "__main__":
    library = Library()
    library.add_book("1984", "George Orwell", 3)
    library.add_book("To Kill a Mockingbird", "Harper Lee", 2)

    print("\nAvailable books:")
    library.list_books()

    print("\nBorrowing '1984':")
    library.borrow_book("1984")

    print("\nAvailable books after borrowing:")
    library.list_books()

    print("\nReturning '1984':")
    library.return_book("1984")

    print("\nAvailable books after returning:")
    library.list_books()