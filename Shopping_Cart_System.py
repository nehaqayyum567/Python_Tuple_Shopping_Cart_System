#Develop a Python program that simulates a simple shopping cart 
# where users can order items, check availability, 
# and calculate the total bill.
# Requirements:
# Store Items:
# Maintain a tuple or list of available items with their prices.
# Example: ("Burger", 250), ("Pizza", 500), ("Fries", 150)
# User Input:
# Allow the user to enter the names of items they want to order.
# Support multiple orders in one run.
# Check Availability:
# If the item exists in the menu → confirm and add its price to the bill.
# If the item does not exist → display “Not available.”
# Bill Calculation:
# Calculate the total bill by summing the prices of ordered items.
# (Optional Bonus) Add a discount code feature (e.g., DISCOUNT10 → 10% off).
# Output:
# Display ordered items with their prices.
# Show the total bill clearly.
# End with a thank‑you message.


#Store Items:

# Maintain a tuple or list of available items with their prices.

menu = (
    ("Burger", 900),
    ("Pizza", 1500),
    ("Nuggets", 900)
)

#User Input:
# Allow the user to enter the names of items they want to order.
# Support multiple orders in one run.

item_name1 = input("Enter 1st name of item:")
item_name2 = input("Enter 2nd name of item:")
item_name3 = input("Enter 3rd name of item:")

# Check Availability:
bill = 0

if(item_name1 == "Burger"):
    print("Burger added (900)")
    bill += 900
elif(item_name1 == "Pizza"):
    print("Pizza added (1500)")
    bill += 1500
elif(item_name1 == "Nuggets"):
    print("Nuggets added (900)")
    bill += 900
else:
    print(item_name1,"Not Available")
    
if(item_name2 == "Burger"):
    print("Burger added (900)")
    bill += 900
elif(item_name2 == "Pizza"):
    print("Pizza added (1500)")
    bill += 1500
elif(item_name2 == "Nuggets"):
    print("Nuggets added (900)")
    bill += 900
else:
    print(item_name2,"Not Available")
    
if(item_name3 == "Burger"):
    print("Burger added (900)")
    bill += 900
elif(item_name3 == "Pizza"):
    print("Pizza added (1500)")
    bill += 1500
elif(item_name3 == "Nuggets"):
    print("Nuggets added (900)")
    bill += 900
else:
    print(item_name3,"Not Available")
    
    
    
#Discount

discount_code = input("Enter discount code:")
if(discount_code == "discount10"):
    discount = bill * 0.10
    bill -=  discount
    print("Discount applied", discount)
    
#Output
print("Total Bill is:", bill)
print("Thank You")
