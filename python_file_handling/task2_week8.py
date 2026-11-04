'''
Task 2: Sales Records
A supermarket stores daily sales in a file named sales.txt. Write a Python program that performs
the following tasks:
i. Open sales.txt in append mode (a).
ii. Ask the user to enter:
• Product name
• Quantity sold
• Total sales amount
iii. Write the new sales record to the file.
iv. Close the file.
v. Explain why append mode is appropriate for this application.
'''
# Open file in append mode
f = open("sales.txt", "a")

# Get sales information
product = input("Enter product name: ")
quantity = int(input("Enter quantity sold: "))
amount = float(input("Enter total sales amount: "))

# Write record to file
print("Product:", product, file=f)
print("Quantity Sold:", quantity, file=f)
print("Total Sales:", amount, file=f)
print("--------------------", file=f)

# Close file
f.close()

print("Sales record saved successfully.")


'''
Question v: Why is append mode appropriate?

Append mode adds new records to the end of an existing file without deleting previously stored records.
'''
