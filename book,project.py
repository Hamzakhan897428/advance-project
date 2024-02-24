def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    books[title] = {'Author': author, 'Genre': genre}
    print("Book added successfully!")

def display_books(books):
    if not books:
        print("No books in the database.")
    else:
        print("Books in the database:")
        for title, details in books.items():
            print(f"Title: {title}, Author: {details['Author']}, Genre: {details['Genre']}")

def search_book(books):
    title = input("Enter the title of the book to search: ")
    if title in books:
        print(f"Book found - Title: {title}, Author: {books[title]['Author']}, Genre: {books[title]['Genre']}")
    else:
        print("Book not found in the database.")

def get_book(books):
    title = input("Enter the title of the book to retrieve: ")
    if title in books:
        print(f"Here is your book: {title}")
        del books[title]
    else:
        print("Book not found in the database.")

def main():
    books = {}
    while True:
        print("\nOptions:")
        print("1. Add book")
        print("2. Display books")
        print("3. Search book")
        print("4. Get book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            display_books(books)
        elif choice == '3':
            search_book(books)
        elif choice == '4':
            get_book(books)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()