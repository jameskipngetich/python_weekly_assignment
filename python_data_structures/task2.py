'''
Task 2: Customer Details Using a Tuple
A company wants to store customer information that should not be modified during program
execution. Write a Python program that performs the following tasks:
i. Create a tuple named customer containing:
• Customer name
• Customer ID
• Telephone number
• Email address
ii. Display the complete tuple.
iii. Access and display the customer's name and telephone number using their indexes.
iv) Display the number of items in the tuple using len().
v) Attempt to modify the customer's telephone number.
vi. State why the modification cannot be performed on the tuple.
'''

# Create a tuple
customer = ("John", "CUST001", "0712345678", "john@gmail.com")

# Display complete tuple
print("Customer Details:", customer)

# Access customer name and telephone number
print("Customer Name:", customer[0])
print("Telephone Number:", customer[2])

# Display number of items
print("Number of Items:", len(customer))

# Attempt to modify telephone number
customer[2] = "0798765432"
