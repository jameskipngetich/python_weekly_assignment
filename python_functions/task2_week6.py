'''
Task 2: Student Grade Function
A university wants to reuse the same grading procedure for different students.
Write a Python program that performs the following tasks:
i. Define a function named calculate_grade(mark).
ii. The function should accept the student's mark as a parameter.
iii. Use the following grading criteria:
70–100 → A
60–69 → B
50–59 → C
40–49 → D
Below 40 → F
iv. Return the appropriate grade.
v. Ask the user to enter a student's mark.
vi. Call the function and display the returned grade.
'''

# Define function
def calculate_grade(mark):

    if mark >= 70:
        return "A"

    elif mark >= 60:
        return "B"

    elif mark >= 50:
        return "C"

    elif mark >= 40:
        return "D"

    else:
        return "F"


# Get student mark
mark = int(input("Enter student mark: "))

# Call function
grade = calculate_grade(mark)

# Display grade
print("Student Grade:", grade)
