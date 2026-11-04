'''
Task 1: Student Records File
A lecturer wants to save student information in a text file. Write a Python program that
performs the following tasks:
i. Open a file named students.txt in write mode (w).
ii. Write the following information for at least three students:
• Student name
• Registration number
• Course
• Mark
iii. Use print(..., file=f) or an equivalent method to write the information to the file.
iv. Close the file using close().
v. State what would happen to the existing contents of the file if it already exists and is
opened using w.
'''
# Open file in write mode
f = open("students.txt", "w")

# Write student records
print("Name: John", file=f)
print("Registration: ZU001", file=f)
print("Course: BSc IT", file=f)
print("Mark: 75\n", file=f)

print("Name: Mary", file=f)
print("Registration: ZU002", file=f)
print("Course: BSc IT", file=f)
print("Mark: 80\n", file=f)

print("Name: Peter", file=f)
print("Registration: ZU003", file=f)
print("Course: BSc IT", file=f)
print("Mark: 65", file=f)

# Close file
f.close()

print("Student records saved successfully.")


'''
Question v: What happens when an existing file is opened using w mode?

The existing contents are erased and replaced with the new information.

'''
