'''
Task 2: Transport Fare System
A transport company calculates fares differently for different types of vehicles. Write a Python
program that performs the following tasks:
i. Create a parent class named Vehicle.
ii. Define a method named calculateFare().
iii. Create a class named Bus that implements calculateFare() using:
Fare = Distance × 50
iv) Create a class named Taxi that implements calculateFare() using:
Fare = Distance × 100
v) Create one Bus object and one Taxi object.
vi. Pass a distance of 10 kilometres to both objects.
vii. Display the calculated fare for each vehicle.
viii. Explain how calling the same calculateFare() method produces different results for the two
objects.
'''

class Vehicle:

    def calculateFare(self, distance):
        pass


class Bus(Vehicle):

    def calculateFare(self, distance):
        return distance * 50


class Taxi(Vehicle):

    def calculateFare(self, distance):
        return distance * 100


# Main section
bus = Bus()
taxi = Taxi()

distance = 10

print("Bus Fare:", bus.calculateFare(distance))
print("Taxi Fare:", taxi.calculateFare(distance))


'''
Explanation:

The same method calculateFare() produces different results because each class has its own implementation.
'''

