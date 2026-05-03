class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.availabilty= True

# defining library class
class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,title,author):
        new_book= Book(title,author)
        self.books.append(new_book)
        print(f"{title} book by {author} is added")
    
    def search_books(self,searchtitle):
        for book in self.books:
            if book.title==searchtitle:
                if book.availabilty:
                         print(f"{searchtitle} is available")
                else:
                    print(f"{searchtitle} is not available")
            else:
                print(f"Book is not availale with {searchtitle}")


    def checkout_book(self,checkout_title):
        for book in self.books:
            if book.title==checkout_title:
                if book.availabilty:
                         book.availabilty=False
                         print(f"{checkout_title} is checked out")
                else:
                    print(f"{checkout_title} is not available so cannot checkout")
                return    
            else:
                print(f"Book is not availale with {checkout_title}")
    def check_available_books(self):
        available_books=[book.title for book in self.books if book.availabilty]
        print(f"available books are: {available_books}") 
    

    def show_available_books(self):
         for book in self.books:
              if(book.availabilty):
                   print(f"{book.title} by {book.author} is availabe")
              else:
                   print(f"{book.title} by {book.author} is sold out")


def main():
     library= Library()
     while True:
          print("1. Add Book")
          print("2. Search Book")
          print("3. Buy Book")
          print("4. show available Books")
          print("5. show all books")
          print("6. Exit")

          option = int(input("\n Enter your option: "))

          if option==1:
               title= input("\n Enter the title of the book ")
               author= input("Enter the author of the book ")
               library.add_book(title,author)
          elif option==2:
                title= input("Enter the title of the book you want to search ")
                library.search_books(title)
          elif option==3:
                title= input("Enter the title of the book you want to buy ")
                library.checkout_book(title)
          elif option==4:
                library.check_available_books()
          elif option==5:
                library.show_available_books()
          else:
               break      
          
main()          














