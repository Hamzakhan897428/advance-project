class Library:
    def __init__(self,listofbooks):
        self.books=listofbooks
    def displayAvailablebook(self):
        print("Books present in this library are:")
        for book in self.books:
            print(" * "+book)
    def barrowbook(self,bookName):
        if bookName in self.books:
            print(f"you have been issued.{bookName},please keep it safe and return it with in 30 days ")
            self.books.remove(bookName)
            return True
        else:
            print("sorry, this book have already been issued to some one else.please wait until retrun the book.")
            return False
    def returnbook(self,bookName):
        self.books.append(bookName)
        print("thanks for returning the books")

class Student:
    def requestbook(self):
        self.books=input("Enter the name of book you want to barrow")
        return self.books
    def requestbook(self):
        self.books=input("Enter the name of book you want to return")
        return self.books
if __name__ == "__main__":
    centrallibrary=Library(["algorithms","clacus","maths","python notes"])
   # centrallibrary.displayAvailablebook()
    student=Student()
    while(True):
        welcomemsg=('''
              =======Welcome to central library======
              please choose an option:
              1:listning all the book
              2:Request a book 
              3:return a book
              4: Exit a library
''')
        a=int(input("Enter a choice: "))
        if  a == 1:
            centrallibrary.displayAvailablebook()
        elif a==2:
            centrallibrary.barrowbook(student.requestbook())
        elif a==3:
            centrallibrary.returnbook(student.requestbook())
        elif a==4:
            print("Thanks for a choosing library! have a great day a head")
            exit()
        else:
            print("invalid choice:")
            
        print(welcomemsg)