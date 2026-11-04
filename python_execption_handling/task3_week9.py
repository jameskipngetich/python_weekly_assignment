'''
Task 3: File Exception Handling
A company has a program that reads employee information from employees.txt. The file may
not exist when the program is executed. Write a Python program that performs the following
tasks:
i. Use a try block to open employees.txt in read mode.
ii. Read and display the contents of the file.
iii. Use an except FileNotFoundError block to display:
The employee file was not found.
iv. Use a finally block to display:
File processing completed.
v. Ensure that the program handles the missing file without terminating
unexpectedly.
'''

try:
    f = open("employees.txt", "r")

    contents = f.read()

    print(contents)

    f.close()

except FileNotFoundError:
    print("The employee file was not found.")

finally:
    print("File processing completed.")
