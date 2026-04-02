class Book:
    def __init__(self, title, author, pages, is_checked_out=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_checked_out = is_checked_out
    
    def describe(self):
        print(f"'{self.title}' by {self.author} ({self.pages} pages)")
    
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"You checked out '{self.title}'")
        else:
            print(f"Sorry, '{self.title}' is not available")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned")
        else:
            print(f"'{self.title}' was not checked out")


book1 = Book("Green Eggs and Ham", "Dr. Seuss", 100, True)
book2 = Book("48 Laws of Power", "Robert Greene", 1000)
book3 = Book("10x Rule", "Grant Cardone", 200, True)

book1.describe()
book2.describe()
book3.describe()

book2.check_out()
book2.check_out()

book2.return_book()
book2.return_book()