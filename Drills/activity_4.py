"""
Part 4
Given the following function that creates a new user to add to a dictionary
create a two decorator functions called 'password_validator' which looks at the password arguments
and checks if they:
   1) two passwords match
   2) the password length is between 8 - 15
   3) contains one of these symbols !@$&+=
   4) does not contain the user's name or email

if the password doesn't meet these criteria it should not execute the function
and it should print out an error message
"""

def password_validator(func):
    pass
    #your code here

users = {}

@password_validator
def create_user(name, email, password1, password2):
    users.update({email: {'name': name, 'password': password1}})
    print("User created successfully.")

# Test
create_user("John Doe", "john@example.com", "P@ssw0rd", "P@ssw0rd")  # This should succeed
create_user("Alice", "alice@example.com", "password", "password")  # This should fail due to mismatch