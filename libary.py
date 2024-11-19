#Farhan Nawaz - Gmail (farhannawazofficial@gamil.com) - ID (22569) - GitHub (farhannawaz14)1


class Library:
    def __init__(self, books):
        # Initialize the library with a list of books
        self.available_books = {book: True for book in books}

    def display_available_books(self):
        # Display all available books
        print("Available Books:")
        for book, available in self.available_books.items():
            if available:
                print(book)

    def borrow_book(self, book):
        # Allow students to borrow a book
        if book in self.available_books and self.available_books[book]:
            self.available_books[book] = False
            print(f"Book '{book}' borrowed successfully.")
        else:
            print(f"Sorry, '{book}' is not available for borrowing.")

    def return_book(self, book):
        # Handle the return of a book
        if book in self.available_books and not self.available_books[book]:
            self.available_books[book] = True
            print(f"Book '{book}' returned successfully.")
        else:
            print(f"Invalid return. '{book}' not found or already available.")


class Student:
    def request_book(self):
        # Take input from the student for borrowing a book
        return input("Enter the name of the book you want to borrow: ")

    def return_book(self):
        # Take input from the student for returning a book
        return input("Enter the name of the book you want to return: ")


if __name__ == "__main__":
    # Create an instance of the Library class with an initial list of books
    initial_books = ["Java", "C++", "JavaScript", "Pyhton"]
    library = Library(initial_books)

    # Create an instance of the Student class
    student = Student()

    while True:
        # Display menu options
        print("\nLibrary Management System")
        print("1. List all books")
        print("2. Request a book")
        print("3. Return a book")
        print("4. Exit")

        # Get user choice
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            library.display_available_books()

        elif choice == '2':
            book_to_borrow = student.request_book()
            library.borrow_book(book_to_borrow)

        elif choice == '3':
            book_to_return = student.return_book()
            library.return_book(book_to_return)

        elif choice == '4':
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
