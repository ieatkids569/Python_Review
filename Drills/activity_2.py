"""
Part 2
The following code asks the user to enter names and saves them in a list.
Fill in the blanks so that it filters out the names that start with a vowel.
"""

names = []
while True:
    answer = input("Enter a name: ")
    if answer != "":
        names.append(answer)
    else:
        break
print(names)

filtered_names = []
for name in _______:
    if ________:
        filtered_names.append(name)

print(filtered_names)