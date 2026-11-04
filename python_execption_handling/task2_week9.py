'''
Task 2: Student Age Registration
A university registration system requires students to enter their age. Write a Python program
that performs the following tasks:
i. Ask the student to enter their age.
ii. Convert the input to an integer.
iii. Use try...except to handle invalid input.
iv. If the user enters a valid number, display:
Age successfully recorded
v. If the user enters text such as "twenty", display:
Invalid age entered
vi. Ensure that the program does not terminate unexpectedly because of the invalid
input.
'''
try:
    age = int(input("Enter your age: "))

    print("Age successfully recorded")

except ValueError:
    print("Invalid age entered")
