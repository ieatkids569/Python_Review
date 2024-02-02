# Part 1
# What does the following code do? Add a comment to each line of code

names = []
while True:
    answer = input("Enter a name: ")
    if answer != "":
        names.append(answer)
    else:
        break
print(names)