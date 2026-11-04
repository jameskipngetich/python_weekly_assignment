'''
Task 3: Product Management
An online shop wants to manage products using Python classes. Write a Python program that
performs the following tasks:
i. Create a class named Product with:
• Product name
• Product code
• Price
• Quantity
ii. Include the following methods:
• setProductDetails() → to assign product information.
• calculateStockValue() → to calculate:
Stock Value = Price × Quantity
• displayProductDetails() → to display product information and stock value.
iii. In the main section:
• Create a Product object.
• Set the product details.
• Calculate the stock value.
. Display products
'''

class Product:

    def setProductDetails(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    def calculateStockValue(self):
        return self.price * self.quantity

    def displayProductDetails(self):
        print("Product Name:", self.name)
        print("Product Code:", self.code)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Stock Value:", self.calculateStockValue())


# Main section
product = Product()

product.setProductDetails("Laptop", "P001", 50000, 5)

product.displayProductDetails()
