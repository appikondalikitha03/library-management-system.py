import random

# List of books
books = [
    "Python Programming",
    "Data Structures",
    "Machine Learning Basics",
    "Artificial Intelligence",
    "Web Development",
    "Database Management",
    "Computer Networks",
    "Operating Systems"
]

issued_books = []

while True:
    print("\n===== Library Management System =====")
    print("1. View Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Random Book Suggestion")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Books:")
        for book in books:
            print("-", book)

    elif choice == "2":
        book_name = input("Enter book name to issue: ")
        if book_name in books:
            books.remove(book_name)
            issued_books.append(book_name)
            print(f"{book_name} has been issued.")
        else:
            print("Book not available.")

    elif choice == "3":
        book_name = input("Enter book name to return: ")
        if book_name in issued_books:
            issued_books.remove(book_name)
            books.append(book_name)
            print(f"{book_name} has been returned.")
        else:
            print("This book was not issued.")

    elif choice == "4":
        if books:
            suggestion = random.choice(books)
            print("Recommended Book:", suggestion)
        else:
            print("No books available for recommendation.")

    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")