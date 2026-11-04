'''
Task 3: Student Management
A university wants to represent students as objects. Write a Python program that performs the
following tasks:
i. Create a class named Student with the following attributes:
• Student name
• Registration number
• Course
• Mark
ii. Include the following methods:
• setStudentDetails() → to assign student information.
• calculateGrade() → to calculate the grade using:
o 70–100 → A
o 60–69 → B
o 50–59 → C
o 40–49 → D
o Below 40 → F
• displayStudentDetails() → to display the student's information and grade.
iii. In the main section:
• Create a Student object.
• Set the student's details.
• Calculate the grade.
• Display the student details and grade.
'''

class Student:

    def setStudentDetails(self, name, reg_no, course, mark):
        self.name = name
        self.reg_no = reg_no
        self.course = course
        self.mark = mark

    def calculateGrade(self):

        if self.mark >= 70:
            return "A"

        elif self.mark >= 60:
            return "B"

        elif self.mark >= 50:
            return "C"

        elif self.mark >= 40:
            return "D"

        else:
            return "F"

    def displayStudentDetails(self):
        print("Student Name:", self.name)
        print("Registration Number:", self.reg_no)
        print("Course:", self.course)
        print("Mark:", self.mark)
        print("Grade:", self.calculateGrade())


# Main section
student = Student()

student.setStudentDetails("Mary", "ZU001", "BSc IT", 75)

student.displayStudentDetails()
