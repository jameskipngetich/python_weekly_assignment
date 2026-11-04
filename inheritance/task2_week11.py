'''
Task 2: Bank Accounts
A bank has different types of accounts. All accounts have an account number and balance, while
a savings account also has an interest rate. Write a Python program that performs the following
tasks:
i. Create a parent class named Account with:
• Account number
• Balance
ii. Include a method named displayAccount().
iii. Create a child class named SavingsAccount that inherits from Account.
iv) Add Interest rate to the SavingsAccount class.
v) Include a method named calculateInterest() using:
Interest = Balance × Interest Rate / 100
vi. Create a SavingsAccount object and display the account details and calculated interest.
'''

class Account:

    def displayAccount(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(Account):

    def calculateInterest(self):
        interest = self.balance * self.interest_rate / 100
        return interest


# Main section
account = SavingsAccount()

account.account_number = "ACC001"
account.balance = 50000
account.interest_rate = 5

account.displayAccount()

print("Interest:", account.calculateInterest())
