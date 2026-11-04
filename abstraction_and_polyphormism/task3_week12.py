'''
Task 3: Shape Area Calculator
An engineering application needs to calculate the area of different shapes. Write a Python
program that performs the following tasks:
i. Create an abstract class named Shape.
ii. Define an abstract method named area().
iii. Create a class named Circle that inherits from Shape.
iv) Implement area() in Circle using:
Area = π × radius²
v) Create a class named Rectangle that inherits from Shape.
vi. Implement area() in Rectangle using:
Area = Length × Width
vii. Create one circle object and one rectangle object.
viii. Calculate and display the area of both shapes.
ix) Explain how the program demonstrates polymorphism.
'''

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        return 3.142 * self.radius * self.radius


class Rectangle(Shape):

    def area(self):
        return self.length * self.width


# Main section
circle = Circle()
circle.radius = 7

rectangle = Rectangle()
rectangle.length = 10
rectangle.width = 5

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())

'''
Explanation:

Polymorphism is demonstrated because both Circle and Rectangle implement the same area() method, but calculate the area differently.
'''
