'''
Task 1: ATM Input Validation
An ATM requires customers to enter the amount they want to withdraw. A customer may
accidentally enter text instead of a number. Write a Python program that performs the following
tasks:
i. Ask the customer to enter the withdrawal amount.
ii. Convert the entered value to an integer.
iii. Place the conversion operation inside a try block.
iv. Use an except block to handle ValueError.
v. Display:
Invalid amount. Please enter a number.
when invalid data is entered.
vi. Display the withdrawal amount when a valid number is entered.
'''
try:
    amount = int(input("Enter withdrawal amount: "))

    print("Withdrawal amount:", amount)

except ValueError:
    print("Invalid amount. Please enter a number.")
