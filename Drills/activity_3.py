"""
Part 3
Write a function, grade_calculator, that takes a list of tuples with (grade, weight) pairs
then calculates and returns the average of weighted grades.

example(800,1000) ⇒ 80%
[(900, 1000), (45, 50), (350, 400)] ⇒ [90% , 90%, 87.5%]
ave = (90 + 90 + 87.5) / 3 = 89.16 %

"""

#Define the funciton
    #create a variable to store the total sum of the weighted grades (set it to 0)

    #loop through the list and get both the grades and weights
        #devide the grade with the weight and add it to the total sum of the weighted grades

    #calculate the average and presented as a percentage
    #(use the length of the list to determin the total number of grade for the average)

    #return the value as a formated string

# Test
example1 = grade_calculator([(800, 1000)])
example2 = grade_calculator([(900, 1000), (45, 50), (350, 400)])

print(f"Example 1: {example1}")
print(f"Example 2: {example2}")
