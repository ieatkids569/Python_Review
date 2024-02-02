print("--- Python Functions ----")

#defining a funciton

def print_hello():
    print("__________________")
    print("___Hello World____")
    print("__________________")

#calling a function
print_hello()




#single argument
def greeting(name):
    print("__________________")
    print(f"___Hello {name}___")
    print("__________________")





#get a name from the user and pass it to the function


#multiple arguments
def hello_x(x, name):
    for i in range(x):
        print(f'Hello {name}')





#arbitrary Arguments
def greetings(*names):
    for name in names:
        print(f'Hello {name}')






#keyword Arguments
def create_account(name, email, password1, password2):
    if password1 == password2:
        new_user = {
            "name": name,
            "email": email,
            "password": password1
        }
    print(f'New user created\n {new_user}')






#Arbitrary Keyword Arguments

def create_arbt_account(**user_info):
    if "password1" in user_info:
        new_user = {}
        for key, value in user_info.items():
            new_user.update({key: value})
        print(f'New user created\n{new_user}')







#default Argument Value
def greeting_email(name="Employee", message="Welcome to the company!"):
    print(f'Dear {name},\n')
    print(message)
    print('_____________________________\n\n\n')



#Return Arguments

def quadratic(a, b, c):
    x1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
    x2 = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)
    solutions = [x1, x2]

    return solutions





#Lambda Functions
def add_n(n):
    return lambda a: a+n

add_10 = add_n(10)
print(f'5 + 10 = {add_10(5)}')

add_31 = add_n(31)
print(f'4 + 10 = {add_31(4)}')


#Create a function called n_multiplier that takes a number n as input and returns a function that takes a number x as input and returns x*n using lambda functions





#Create a function that will sort a list of lists based on the second element the inner lists.
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]


#Should Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]



#Decorators
import time
def run_time_counter(func):
    def wrapper(a, b, c):
        start = time.time()
        func(a, b, c)
        end = time.time()
        print(f'Run Time: {end - start} sec')
    return wrapper

@run_time_counter
def timed_quadratic(a, b, c):
    x1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
    x2 = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)
    solutions = [x1, x2]
    print(f'x1: {x1}, x2: {x2}, solutions: {solutions}')

timed_quadratic(12, 4, 7)
