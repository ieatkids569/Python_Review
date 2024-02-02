"""
Part 2
The following function takes four arguments
(email, name, password1, and password2)
and creates a new user, adds it to a dictionary called users
but only if there is no user with the email already in the dictionary
and if the two passwords match.
Finish it by filling in the blank
"""
___ create_user(_____, _____, ________, _________, _____):
    if _________________:
        print(f"User with email {email} already exists. Please choose a different email.")
    elif password1 != password2:
        print("Passwords do not match. Please try again.")
    else:
        users[email] = {'name': name, 'password': password1}
        print(f"User {name} with email {email} has been created successfully.")

# Example usage:
users_dict = {}

email_input = input("Enter email: ")
name_input = input("Enter name: ")
password1_input = input("Enter password: ")
password2_input = input("Confirm password: ")

create_user(email_input, name_input, password1_input, password2_input, users_dict)

# Print the updated users dictionary
print("Updated Users Dictionary:", users_dict)
