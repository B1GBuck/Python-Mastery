"""
- Encapsulation is about protecting data inside a class
- Encapsulation prevents accidental changes to your data and hides the internal details of how your class works

** What this means exactly is data (properties) and methods are kept together in a class, while controlling how the data can be accessed outside of the class

"""

# You can make properties private by using a double underscore ( __ ) prefix

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age                   # Private class property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age)                             # This line of code will cause an error to the program




# You are able to access a private property by creating a getter method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

p1 = Person("Greg", 35)
print(p1.name)
print(p1.get_age()) 

# You can modify a private property bey using a setter method

# The setter method can also validate the value before setting it

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age 
        else:
            print("Age must be positive")

p1 = Person("Freddy", 43)
print(p1.get_age())

p1.set_age(36)
print(p1.get_age())

# Why use Encapsulation
"""
Encapsulation provides several benefits:

- Data Protection: Prevevts accidental data modification

- Validation:You can validate data before setting it 

- Flexibility: Internal implementation can change without affecting external code

- Control: You have full control over how data is accessed and modified

"""

# Validation

class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")
    
    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"
        
student = Student("Sid")
student.set_grade(65)
print(student.get_grade())
print(student.get_status())

# Protected Properties

# Python also has a convention for protected properties using a single underscore ( _ ) prefix

class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary               # Protected Property

p1 = ("William", 49000)
print(p1.name)
print(p1._salary)

# Private Methods

# Methods can be made private by using the double underscore prefix

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True
    
    def add(self, num):
        if self.__validate(num):
            self.result += num 
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)


"""
Properties are the Pythonic way of access control to attributes

Python allows you to use the @property decorator to let you control attribute access 
while keeping clean dot notation, instead of having to write separate methods

"""

# 2.3 Library Tracker V3

class ProtectedBook:
    library_name = "GP Library"
    total_books = 0
    def __init__(self, title, author, pages, is_checked_out=False):
        self._title = title
        self._author = author
        self._pages = pages
        self._is_checked_out = is_checked_out
        ProtectedBook.total_books += 1

    @classmethod
    def get_total_books(cls):
        print(f"Total books in library: {cls.total_books}")
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = value
    
    @property
    def is_checked_out(self):
        return self._is_checked_out
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"You checked out '{self._title}'")
        else:
            print(f"Sorry, '{self._title}' is not available")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"'{self._title}' has been returned")
        else:
            print(f"'{self._title}' was not checked out")
        
    def describe(self):
        print(f"'{self._title}' by {self._author} ({self._pages} pages) - {self.library_name}")



book1 = ProtectedBook("Green Eggs and Ham", "Dr. Seuss", 100)
book2 = ProtectedBook("48 Laws of Power", "Robert Greene", 1000)

book1.describe()
book2.describe()

ProtectedBook.get_total_books()

print(book1.pages)
print(book2.pages)

book1.pages = 600
print(book1.pages)

try:
    book2.pages = -7
except ValueError as e:
    print(e)