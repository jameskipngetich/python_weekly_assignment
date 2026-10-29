'''
Supermarket Discount
A supermarket gives customers a 15% discount on purchases of KSh 10,000 or more. Write a
Python program that performs the following tasks:
i. Ask the customer to enter the total purchase amount.
ii. Convert the amount to a floating-point number.
iii. Use a comparison operator to determine whether the purchase amount is at least KSh
10,000.
iv) If the customer qualifies, calculate the discount using:
Discount = 15% × Purchase Amount
v) Calculate the final amount using:
Final Amount = Purchase Amount − Discount
vi. Display the purchase amount, discount and final amount.

'''

purchase_amnt = float(input("Enter the total Purchase amount: kes "))

if ( purchase_amnt >= 10000 ):
    discount = 15/100 * purchase_amnt
else:
    discount = 0

final_amnt = purchase_amnt - discount

print("="*32)
print(f"The Purchase amount: kes {purchase_amnt} \nThe discount is: kes {discount} \nThe Final amount is: kes {final_amnt}")

