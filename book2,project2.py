def add_book(books):
    title=input("Enter book title:")
    auther=input("Enter book auther:")
    genre=input("Enter genre:")
    books[title]={"auther":auther,"genure":genre}
    print("books are add successfuly")
def Dislpay_book(books):
    if not books:
        print("NO books in database")
    else:
        print("Book in database.")
        for title,details in books.item():
            print(f"title:{title},Auther{details["Auther"]},Genre{details["Genre"]}")
def Search_book(books):
    title=input("Enter title books search.")
    if title in books:
        print(f"book_found{title},Auther{books[title]['Auther']},Genre{books[title]["Genre"]}")          
def get_book(books):
    title=input("Enter the books of retriveral:")
    if title in books:
        print(f"Here in book{title}")
        del books[title]
    else:
        print("not found in database")
def main():
    books={}
    while True:
        print("\n opertion:")
        print("1:add books")
        print("2:Dislpay books")
        print("3:search books")
        print("4:Get book")
        print("Exit")
        choice=input("Enter your choice:")

        if choice==1:
            add_book(books)
        elif choice==2:
            Dislpay_book(books)
        elif choice==3:
            Search_book(books)
        elif choice==4:
            get_book(books)
        elif choice==5:
            print("Exiting....")
            break
        else:
            print("Enter not choice ,not ")
if __name__ == "__main__":
    main()