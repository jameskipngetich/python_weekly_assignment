'''
Task 3: Unique Product Categories Using a Set
An online shop receives product categories from different departments. Some categories are
entered more than once. Write a Python program that performs the following tasks:
i. Create a set named categories containing at least six product categories,
including two duplicate categories.
ii. Display the set.
iii. Add a new product category using add().
iv. Remove one category using remove().
v. Display the final set.
vi. Explain how using a set helps the company maintain unique product categories.
'''

# Create a set with product categories
categories = {
    "Electronics",
    "Clothing",
    "Food",
    "Furniture",
    "Electronics",
    "Books"
}

# Display the set
print("Product Categories:", categories)

# Add a new category
categories.add("Sports")

# Remove one category
categories.remove("Food")

# Display final set
print("Final Categories:", categories)
