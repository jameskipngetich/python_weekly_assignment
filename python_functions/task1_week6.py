'''
Task 1: Electricity Bill Function
An electricity company wants to calculate customers' electricity bills. Write a Python program
that performs the following tasks:
i. Define a function named calculate_bill().
ii. The function should accept:
• Units consumed
• Cost per unit
iii. Calculate the bill using:
Bill = Units Consumed × Cost Per Unit
iv. Return the calculated bill.
v. Ask the user to enter the units consumed and cost per unit.
vi. Call the calculate_bill() function.
vii. Display the calculated electricity bill.
'''

# Define function
def calculate_bill(units, cost):
    bill = units * cost
    return bill


# Get user input
units = float(input("Enter units consumed: "))
cost = float(input("Enter cost per unit: "))

# Call function
total_bill = calculate_bill(units, cost)

# Display result
print("Electricity Bill:", total_bill)
