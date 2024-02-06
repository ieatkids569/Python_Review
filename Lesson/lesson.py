print("--- Python Functions ----")

class Bookbag:
    def __init__(self):
        self.books = []
        self.laptop = None
        self.random = []

    def add_book(self, book):
        self.books.append(book)

    def add_laptop(self, laptop):
        self.laptop = laptop

    def add_items(self, items):
        if len(items) > 0:
             self.random.append(items)
    def get_items(self):
        items = {
            "books": self.books,
            "laptop": self.laptop,
            "random": self.random
        }
        return items

#create code to create bookbags for three people and ask users to add items


#test the methods


import random
class User:
    users = []
    def __init__(self, **kwargs):
        self.id = random.randint(1000, 9999)
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')

        # Add the user to the class variable
        User.users.append(self)

    def __str__(self):
        return f"User: {self.first_name}, Email: {self.email}"

    @classmethod
    def get_all_users(cls):
        return cls.all_users

# Example usage
user1 = User(first_name="Johnny", last_name="Bravo", email="jbravo@email.com", password="al0D12")
user2 = User(first_name="Baily", last_name="Smith", email="bsmith@email.com", password="93nd7ee")

print(user1)
print(user2)


#Create a class to hold data of different schools
#for school registry database




#Create a class to hold course information
#for Brakebills University database



#Inheritance
class Human:
    """
    Represents a human with a name and birthdate.

    Attributes:
        name (str): The name of the human.
        bday (str): The birthdate of the human in the format 'YYYY-MM-DD'.
    """

    def __init__(self, name, bday):
        """
        Initializes a new instance of the Human class.

        Args:
            name (str): The name of the human.
            bday (str): The birthdate of the human in the format 'YYYY-MM-DD'.
        """
        self.name = name
        self.bday = bday

    def greet(self):
        """
        Prints a greeting message.

        Returns:
            str: A greeting message.
        """
        return f"Hello, my name is {self.name}."

class Student(Human):
    """
    Represents a student, inheriting from the Human class.

    Attributes:
        student_id (int): The student ID of the student.
    """

    def __init__(self, name, bday, student_id):
        """
        Initializes a new instance of the Student class.

        Args:
            name (str): The name of the student.
            bday (str): The birthdate of the student in the format 'YYYY-MM-DD'.
            student_id (int): The student ID of the student.
        """
        super().__init__(name, bday)
        self.student_id = student_id

    def study(self):
        """
        Prints a message indicating that the student is studying.

        Returns:
            str: A message indicating that the student is studying.
        """
        return f"{self.name} is studying hard."

# Examples of how to use the classes
human = Human(name="John Doe", bday="1990-05-15")
print(human.greet())  # Output: Hello, my name is John Doe.

student = Student(name="Alice", bday="1995-08-22", student_id=12345)
print(student.greet())  # Output: Hello, my name is Alice.
print(student.study())  # Output: Alice is studying hard.



#Polymorphism
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Parrot:
    def speak(self):
        return "Squawk!"

def animal_sound(animal):
    return animal.speak()

# Examples
dog = Dog()
cat = Cat()
parrot = Parrot()

print(animal_sound(dog))    # Output: Woof!
print(animal_sound(cat))    # Output: Meow!
print(animal_sound(parrot))  # Output: Squawk!

