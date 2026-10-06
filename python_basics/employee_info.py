# A program to receive employee info, calculate Annual salary and display Their whole information

EmployeeName = input("Enter your Name: ")
EmployeeId = input("Enter Your Employee ID: ")
EmployeeAge = int(input("Enter your Age: "))
BasicSalary = float(input("Enter Your Basic Salary: Kes "))


AnnualSalary = BasicSalary * 12 

print("#"*36)
print("#"*8+"EMPLOYEE INFORMATION"+"#"*8)
print(f"Employee Name: {EmployeeName}")
print(f"Employee Id: {EmployeeId}")
print(f"Employee Age: {EmployeeAge}")
print(f"Basic Salary: Kes {BasicSalary:.2f}")
print(f"Annual Salary: Kes {AnnualSalary:.2f}")
print("#"*36)

