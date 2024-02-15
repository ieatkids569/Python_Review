"""
Part 3
Write code that asks the user to enter numbers and them to a list only if the numbers are positive.
"""

# create an empty list to store the numbers
# start a while loop
    # get a number from the user
    # check if the entered number and that it is positive
    # then add it to the list(what data type should the number be?)

    # if nothing is entered stop the loop

# print out the list of positive number

numbers = []
while True:
   num = input("enter a number")
   if num > "0":
         numbers.append(int(num))
   else:
       break

       print(numbers)




