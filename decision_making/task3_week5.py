'''
Task 3: Employee Bonus
A company awards employees a bonus if they have worked for at least three years and have
achieved a performance rating of 4 or 5. Write a Python program that performs the following
tasks:
i. Ask the employee to enter:
• Employee name
• Years of service
• Performance rating
ii. Convert the years of service and performance rating to integers.
iii. Use logical operators to check whether:
• Years of service is at least 3 AND
• Performance rating is at least 4.
iv) If the employee qualifies, display:
Employee qualifies for a bonus
v) Otherwise, display:
Employee does not qualify for a bonus
vi. Display the employee's details and eligibility result.
'''

# Get employee details
name = input("Enter employee name: ")
years = int(input("Enter years of service: "))
rating = int(input("Enter performance rating: "))

# Check bonus eligibility
if years >= 3 and (rating == 4 or rating == 5):
    result = "Employee qualifies for a bonus"

else:
    result = "Employee does not qualify for a bonus"

# Display employee details
print("\nEmployee Name:", name)
print("Years of Service:", years)
print("Performance Rating:", rating)
print("Eligibility:", result)
