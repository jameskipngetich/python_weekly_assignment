'''
Task 3: Transport System
A transport company operates different types of vehicles.
Write a Python program that performs the following tasks:
i. Create a parent class named Vehicle with:
• Registration number
• Model
ii. Include a method named displayVehicle().
iii. Create a child class named Bus that inherits from Vehicle.
iv) Add:
• Passenger capacity
to the Bus class.
v) Include a method named displayBus() to display all vehicle information.
vi. Create a Bus object and display its details.
'''

class Vehicle:

    def displayVehicle(self):
        print("Registration Number:", self.registration_number)
        print("Model:", self.model)


class Bus(Vehicle):

    def displayBus(self):
        self.displayVehicle()
        print("Passenger Capacity:", self.capacity)


# Main section
bus = Bus()

bus.registration_number = "KDA 123A"
bus.model = "Isuzu"
bus.capacity = 50

bus.displayBus()
