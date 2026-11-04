'''
Task 1: Student Grading System
A university wants to automate student grading.
Write a Python program that performs the following tasks:
i. Ask the student to enter their name and examination mark.
ii. Convert the mark to an integer.
iii. Use an if...elif...else statement to assign grades as follows:
• 70–100 → A
• 60–69 → B
• 50–59 → C
• 40–49 → D
• Below 40 → F
iv) If the mark is below 0 or above 100, display:
Invalid mark
v) Display the student's name, mark and grade.

'''
# Ask for student details
name = input("Enter student name: ")
mark = int(input("Enter examination mark: "))

# Check the mark and assign grade
if mark < 0 or mark > 100:
    print("Invalid mark")

elif mark >= 70:
    grade = "A"

elif mark >= 60:
    grade = "B"

elif mark >= 50:
    grade = "C"

elif mark >= 40:
    grade = "D"

else:
    grade = "F"

# Display student details
if mark >= 0 and mark <= 100:
    print("\nStudent Name:", name)
    print("Examination Mark:", mark)
    print("Grade:", grade)
