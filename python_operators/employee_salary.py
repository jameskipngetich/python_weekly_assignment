'''
 Employee Salary Calculation
A company calculates an employee's net salary by adding a 10% housing allowance to the basic
salary and subtracting a fixed deduction. Write a Python program that performs the following
tasks:
i. Ask the user to enter:
• Employee name
• Basic salary
• Monthly deduction
ii. Convert the salary and deduction to floating-point numbers.
iii. Calculate the housing allowance using:
Housing Allowance = 10% × Basic Salary
iv) Calculate the gross salary using:
Gross Salary = Basic Salary + Housing Allowance
v) Calculate the net salary using:
Net Salary = Gross Salary − Deduction
vi. Display the basic salary, allowance, gross salary, deduction and net salary.
'''

EmployeeName = input("Enter your name: ")
BasicSalary = float(input("Enter your basic salary: "))
MonthlyDeduction = float(input("Enter Your monthly deduction: "))

HousingAllowance = 10/100 * BasicSalary

GrossSalary = BasicSalary + HousingAllowance

NetSalary = GrossSalary - MonthlyDeduction

print("="*30)
print(f"Employee Name: {EmployeeName}")
print(f"Employee Basic salary: kes {BasicSalary}")
print(f"Employee House Allowance: kes {HousingAllowance}")
print(f"Employee Gross salary: kes {GrossSalary}")
print(f"Employee Monthly deduction: kes {MonthlyDeduction}")
print(f"Employee Net salary: kes {NetSalary}")

