'''
Task 1: Student Marks Using a List
A lecturer wants to store the marks of a student in five subjects. Write a Python program that
performs the following tasks:
i. Create a list named marks containing five subject marks.
ii. Display all the marks.
iii. Calculate and display the total marks using sum().
iv. Calculate and display the average mark.
v. Display the highest mark using max().
vi. Display the lowest mark using min().
vii. Modify the mark of the third subject and display the updated list.
'''



# Create a list of five subject marks
marks = [75, 80, 65, 90, 70]

# Display all marks
print("Student Marks:", marks)

# Calculate total marks
total = sum(marks)
print("Total Marks:", total)

# Calculate average
average = total / len(marks)
print("Average Marks:", average)

# Display highest and lowest marks
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

# Modify the third subject mark
marks[2] = 85

# Display updated list
print("Updated Marks:", marks)
