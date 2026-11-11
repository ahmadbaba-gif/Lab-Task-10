"""
Library Management System
Menu-driven program using variables, loops, lists, dictionaries,
functions, and classes/objects.
"""


class Book:
    """Represents one book record in the library."""

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total = quantity        # total copies owned by the library
        self.available = quantity    # copies currently on the shelf

    def display(self):
        print(f"ID: {self.book_id} | Title: {self.title} | "
              f"Author: {self.author} | Available: {self.available}/{self.total}")


class Library:
    """Handles all library operations."""

    def __init__(self):
        self.books = {}    # dictionary: book_id -> Book object
        self.issued = []   # list of dicts: {"book_id": ..., "student": ...}

    # ---------- Add ----------
    def add_book(self, book_id, title, author, quantity):
        if book_id in self.books:
            print("Error: A book with this ID already exists!")
            return
        self.books[book_id] = Book(book_id, title, author, quantity)
        print("Book added successfully!")

    # ---------- View all ----------
    def view_all(self):
        if not self.books:
            print("No books in the library yet.")
            return
        for book in self.books.values():
            book.display()

    # ---------- Search ----------
    def search(self, keyword):
        keyword = keyword.lower()
        found = False
        for book in self.books.values():
            # match by exact ID or by part of the title
            if keyword == book.book_id.lower() or keyword in book.title.lower():
                book.display()
                found = True
        if not found:
            print("Book not found.")

    # ---------- Issue ----------
    def issue_book(self, book_id, student):
        book = self.books.get(book_id)
        if book is None:
            print("Error: Book not found.")
        elif book.available == 0:
            print("Sorry, no copies available right now.")
        else:
            book.available -= 1
            self.issued.append({"book_id": book_id, "student": student})
            print("Book issued successfully!")
            print(f"Available Quantity: {book.available}")

    # ---------- Return ----------
    def return_book(self, book_id, student):
        book = self.books.get(book_id)
        if book is None:
            print("Error: Book not found.")
            return
        # a return must match a book that is currently issued to this student
        for record in self.issued:
            if record["book_id"] == book_id and record["student"].lower() == student.lower():
                self.issued.remove(record)
                book.available += 1
                print("Book returned successfully!")
                print(f"Available Quantity: {book.available}")
                return
        print("Error: No such issued record found (check book ID and student name).")

    # ---------- Delete ----------
    def delete_book(self, book_id):
        book = self.books.get(book_id)
        if book is None:
            print("Error: Book not found.")
        elif book.available != book.total:
            print("Cannot delete: some copies of this book are currently issued.")
        else:
            del self.books[book_id]
            print("Book deleted successfully!")

    # ---------- View issued ----------
    def view_issued(self):
        if not self.issued:
            print("No books are currently issued.")
            return
        for record in self.issued:
            title = self.books[record["book_id"]].title
            print(f"Book ID: {record['book_id']} | Title: {title} | "
                  f"Student: {record['student']}")


# ---------- Input helpers (validation) ----------
def get_text(prompt):
    """Keep asking until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Try again.")


def get_positive_int(prompt):
    """Keep asking until the user enters a positive whole number."""
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Invalid input! Enter a positive whole number.")


def show_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")


def main():
    library = Library()

    while True:  
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nADD NEW BOOK")
            book_id = get_text("Enter Book ID: ")
            title = get_text("Enter Book Title: ")
            author = get_text("Enter Author Name: ")
            quantity = get_positive_int("Enter Quantity: ")
            library.add_book(book_id, title, author, quantity)

        elif choice == "2":
            print("\nALL BOOKS")
            library.view_all()

        elif choice == "3":
            print("\nSEARCH BOOK")
            library.search(get_text("Enter Book ID or Title: "))

        elif choice == "4":
            print("\nISSUE BOOK")
            book_id = get_text("Enter Book ID: ")
            student = get_text("Enter Student Name: ")
            library.issue_book(book_id, student)

        elif choice == "5":
            print("\nRETURN BOOK")
            book_id = get_text("Enter Book ID: ")
            student = get_text("Enter Student Name: ")
            library.return_book(book_id, student)

        elif choice == "6":
            print("\nDELETE BOOK")
            library.delete_book(get_text("Enter Book ID: "))

        elif choice == "7":
            print("\nISSUED BOOKS")
            library.view_issued()

        elif choice == "8":
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
