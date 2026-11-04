'''
Task 2: Inventory Management
A supermarket wants to use a dictionary to manage the quantity of products in stock. Write a
Python program that performs the following tasks:
i. Create a dictionary named inventory containing at least five products and their
quantities.
ii. Display the quantity of a specified product.
iii. Add a new product to the dictionary.
iv. Update the quantity of an existing product.
v. Remove one product from the dictionary.
vi. Display the final inventory.
'''
# Create inventory dictionary
inventory = {
    "Sugar": 20,
    "Rice": 15,
    "Milk": 30,
    "Bread": 25,
    "Cooking Oil": 10
}

# Display quantity of a specified product
print("Sugar quantity:", inventory["Sugar"])

# Add a new product
inventory["Tea"] = 12

# Update quantity of an existing product
inventory["Rice"] = 25

# Remove one product
del inventory["Bread"]

# Display final inventory
print("\nFinal Inventory:")
for product, quantity in inventory.items():
    print(product, ":", quantity)
