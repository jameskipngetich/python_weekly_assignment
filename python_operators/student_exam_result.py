'''
Task 3: Student Examination Results
A lecturer wants to calculate the final mark for a student using coursework and examination
marks. Write a Python program that performs the following tasks:
i. Ask the user to enter:
• Student name
• Coursework mark out of 30
• Examination mark out of 70
ii. Calculate the total mark using:
Total Mark = Coursework Mark + Examination Mark
iii. Use comparison operators to determine whether the student has achieved at least 40 marks.
iv) Display the student's name, coursework mark, examination mark and total mark.
v) Display True or False to indicate whether the student has passed.

'''

student_name = input("Enter students name: ")
course_wk = int(input("Enter students coursework mark out of 30: "))
exam = int(input("Enter students Examination mark out of 70: "))

total = course_wk + exam

if ( total >= 40 ) :
    passed = "True"
else:
    passed = "False"

print("="*56)
print(f"Students Name: {student_name} \nCoursework: {course_wk} / 30 \nExamination mark: {exam} / 70 \nTotal Mark: {total} \nPassed: {passed}")
