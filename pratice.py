
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {'title': title, 'author': author, 'available': True}
            print(f"Book '{title}' by {author} added successfully.")
        else:
            print("Book ID already exists. Try a different ID.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available Books:")
            for book_id, book_info in self.books.items():
                print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['available']}")

    def borrow_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]['available']:
                self.books[book_id]['available'] = False
                print(f"Book '{self.books[book_id]['title']}' borrowed successfully.")
            else:
                print("Book is not available for borrowing.")
        else:
            print("Book ID not found.")

    def return_book(self, book_id):
        if book_id in self.books:
            if not self.books[book_id]['available']:
                self.books[book_id]['available'] = True
                print(f"Book '{self.books[book_id]['title']}' returned successfully.")
            else:
                print("Book is already available.")
        else:
            print("Book ID not found.")


# Example usage:
library_system = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        library_system.add_book(book_id, title, author)

    elif choice == '2':
        library_system.display_books()

    elif choice == '3':
        book_id = input("Enter Book ID to borrow: ")
        library_system.borrow_book(book_id)

    elif choice == '4':
        book_id = input("Enter Book ID to return: ")
        library_system.return_book(book_id)

    elif choice == '5':
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
