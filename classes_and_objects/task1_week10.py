'''
Task 1: Bank Account
A bank wants to develop a Python program to manage customer bank accounts.
Write a Python program that performs the following tasks:
i. Create a class named BankAccount with the following data members:
• Account number
• Customer name
• Balance
ii. Include the following public methods:
• deposit() → to add money to the account balance
• withdraw() → to deduct money from the account balance
• displayAccount() → to display account information and current balance
iii. In the main section:
• Create an object of the BankAccount class.
• Assign account details.
• Deposit KSh 5,000.
• Withdraw KSh 2,000.
• Display the account details and updated balance.
'''
class BankAccount:

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def displayAccount(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Balance:", self.balance)


# Main section
account = BankAccount()

account.account_number = "ACC001"
account.customer_name = "John"
account.balance = 10000

account.deposit(5000)
account.withdraw(2000)

account.displayAccount()
