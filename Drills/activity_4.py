"""
Part 4.a
Write a program that asks the user to enter a list of names then
finds and prints the longest name in the list.
"""
names=[]
biggest = ""
while True:
    name = input("enter some stuff")
    if name != "":
        names.append(name)
        if len(name) > len(biggest):
            biggest = name
    else:
        break
"""
Part 4.b
Edit the above code so that it uses list Comprehension 
"""

filtered_list = [name for name in names if name[0].lower() in "aeiou"]









