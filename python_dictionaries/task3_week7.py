'''
Task 3: Employee Salary Records
A company stores employee names and salaries using a Python dictionary. Write a Python
program that performs the following tasks:
i. Create a dictionary named employees containing at least five employees and
their salaries.
ii. Display all employee names and salaries using a loop.
iii. Update the salary of one employee.
iv. Add a new employee and salary.
v. Calculate and display the total salary payable to all employees.
'''
# Create employees dictionary
employees = {
    "John": 30000,
    "Mary": 40000,
    "Peter": 35000,
    "Jane": 45000,
    "David": 28000
}

# Display employee names and salaries
print("Employee Salary Records:")
for name, salary in employees.items():
    print(name, ":", salary)

# Update salary
employees["John"] = 35000

# Add a new employee
employees["Grace"] = 50000

# Calculate total salary
total = 0

for salary in employees.values():
    total = total + salary

print("\nTotal Salary Payable:", total)
