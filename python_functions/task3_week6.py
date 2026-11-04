'''
Task 3: Temperature Conversion Function
A weather application needs to convert temperature from Celsius to Fahrenheit. Write a Python
program that performs the following tasks:
i. Define a function named convert_temperature().
ii. Accept the Celsius temperature as a parameter.
iii. Convert Celsius to Fahrenheit using:
Fahrenheit = (Celsius × 9/5) + 32
iv. Return the Fahrenheit value.
v. Ask the user to enter the temperature in Celsius.
vi. Call the function and display the converted temperature to two decimal places.
'''

# Define function
def convert_temperature(celsius):

    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit


# Get temperature from user
celsius = float(input("Enter temperature in Celsius: "))

# Call function
result = convert_temperature(celsius)

# Display converted temperature
print("Temperature in Fahrenheit:", round(result, 2))
