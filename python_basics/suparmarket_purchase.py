# A program to receive and calculate customer purchase details

CustomerName = input("Enter your Name: ")
ProductName = input("Enter the Product Name: ")
QuantityPurchased = int(input("Enter quantity purchased: "))
PricePerItem = float(input("Enter price per item: Kes "))

# Calculate total cost by multiplying PricePerItem by QuantityPurchased
TotalCost = QuantityPurchased * PricePerItem

print("#"*40)
print("#"*8+"Zinazo Pendwa Supamarket"+"#"*8)
print(f"Customer Name: {CustomerName}")
print(f"Product Name: {ProductName}")
print(f"Quantity: {QuantityPurchased}")
print(f"Price per Item: Kes {PricePerItem:.3f}")
print(f"Total Cost: Kes {TotalCost:.3f}")
print("#"*40)

