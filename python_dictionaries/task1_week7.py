'''
Task 1: Student Record
A university wants to store student information using a dictionary.
Write a Python program that performs the following tasks:
i. Create a dictionary named student containing:
• Registration number
• Student name
• Course
• Year of study
ii. Display the student's name and course using their dictionary keys.
iii. Change the student's year of study.
iv) Add an email address to the dictionary.
v) Display the complete updated dictionary.
'''

# Create a student dictionary
student = {
    "reg_no": "ZU001",
    "name": "John",
    "course": "BSc Information Technology",
    "year": 1
}

# Display student name and course
print("Student Name:", student["name"])
print("Course:", student["course"])

# Change year of study
student["year"] = 2

# Add email address
student["email"] = "john@gmail.com"

# Display updated dictionary
print("\nUpdated Student Records:")
print(student)
