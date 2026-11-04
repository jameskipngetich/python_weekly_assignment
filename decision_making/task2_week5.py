'''
Task 2: ATM Withdrawal
A bank wants to develop a simple ATM withdrawal program. The customer's account has a
balance of KSh 50,000. Write a Python program that performs the following tasks:
i. Store the initial account balance as KSh 50,000.
ii. Ask the customer to enter the withdrawal amount.
iii. Convert the amount to an integer.
iv. Check that:
• The withdrawal amount is greater than zero.
• The withdrawal amount does not exceed the account balance.
• The withdrawal amount is a multiple of KSh 500.
v. If all conditions are satisfied, deduct the amount from the balance.
vi. Display the remaining balance.
vii. Display an appropriate error message when any of the conditions is not
satisfied.
'''
# Initial account balance
balance = 50000

# Ask customer for withdrawal amount
amount = int(input("Enter withdrawal amount: "))

# Check withdrawal conditions
if amount <= 0:
    print("Invalid withdrawal amount")

elif amount > balance:
    print("Insufficient account balance")

elif amount % 500 != 0:
    print("Amount must be a multiple of KSh 500")

else:
    balance = balance - amount

    print("Withdrawal successful")
    print("Remaining Balance: KSh", balance)
