'''
Task 1: Payment System
An online shopping system supports different payment methods. Write a Python program that
performs the following tasks:
i. Create an abstract class named Payment.
ii. Define an abstract method named makePayment().
iii. Create a class named MobileMoneyPayment that inherits from Payment.
iv) Implement makePayment() in MobileMoneyPayment to display:
Payment made using Mobile Money
v) Create another class named CardPayment that inherits from Payment.
vi. Implement makePayment() in CardPayment to display:
Payment made using Bank Card
vii. Create objects of both classes and call makePayment().
viii. Explain how the program demonstrates abstraction and polymorphism.
'''
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def makePayment(self):
        pass


class MobileMoneyPayment(Payment):

    def makePayment(self):
        print("Payment made using Mobile Money")


class CardPayment(Payment):

    def makePayment(self):
        print("Payment made using Bank Card")


# Main section
mobile = MobileMoneyPayment()
card = CardPayment()

mobile.makePayment()
card.makePayment()

'''
Explanation:
- Abstraction: The Payment class defines a method that child classes must implement without providing its actual implementation.
- Polymorphism: Both child classes use the same method name, makePayment(), but perform different actions.
'''
