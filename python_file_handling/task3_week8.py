'''
 Reading Customer Records
A company has stored customer information in a file called customers.txt. Write a Python
program that performs the following tasks:
i. Open customers.txt in read mode (r).
ii. Read the contents of the file.
iii. Display the contents on the screen.
iv. Close the file.
v. State the purpose of each of the following file modes:
• r
• w
• a
'''
# Open file in read mode
f = open("customers.txt", "r")

# Read file contents
contents = f.read()

# Display contents
print(contents)

# Close file
f.close()

'''
Question v: Purpose of file modes
- r – Opens a file for reading.
- w – Opens a file for writing and replaces existing contents.
- a – Opens a file for appending new information.
'''
