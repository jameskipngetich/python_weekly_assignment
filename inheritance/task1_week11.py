'''
Task 1: University Employees
A university has different categories of employees. All employees have a name and employee
ID, while lecturers additionally have a teaching subject.
Write a Python program that performs the following tasks:
i. Create a parent class named Employee with:
• Employee name
• Employee ID
ii. Include a method named displayEmployee() to display the employee details.
iii. Create a child class named Lecturer that inherits from Employee.
iv) Add the following attribute to the Lecturer class:
• Teaching subject
v) Include a method named displayLecturer() to display the employee name, employee ID and
teaching subject.
vi. In the main section:
• Create a Lecturer object.
• Assign the employee details.
• Assign the teaching subject.
• Display all information.
'''
class Employee:

    def displayEmployee(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)


class Lecturer(Employee):

    def displayLecturer(self):
        self.displayEmployee()
        print("Teaching Subject:", self.subject)


# Main section
lecturer = Lecturer()

lecturer.name = "John"
lecturer.employee_id = "EMP001"
lecturer.subject = "Programming"

lecturer.displayLecturer()
