# shopping_cart.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)
# pprint(products)

#
# INFO CAPTURE
#

total_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier:") #> "9" (string)
    #> "DONE""
    if selected_id == "DONE":
        break
    elif selected_id != "DONE" and not selected_id.isdigit():
        print("Please input a numerical product identifier. Thanks!")
        # Source for selected_id.isdigit(): https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
    elif int(selected_id) < 1 or int(selected_id) > 20:
        print("Hey, are you sure that product identifier is correct? Please try again!")
    else:
       # matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
       # matching_product = matching_products[0]
       # total_price = total_price + matching_product["price"]
       # #print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))
        selected_ids.append(selected_id)

#
# INFO DISPLAY
# 

#print(selected_ids)
 
print("----------------------------------------------------------")

print("MEENA'S GARDEN-FRESH GROCER'S MARKET: RECEIPT OF PURCHASE")
print("3735 M ST NW, Washington, D.C. 20007")
print("e: https://www.meenasmarket.com")
print("p: 201.468.1698")
print("Hours of Operation: M-F, 10 am - 10 pm")

print("-------------------------------------------=---------------")

import datetime
now = datetime.datetime.now()
print ("TIME OF CHECKOUT: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

print("----------------------------------------------------------")

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    #print("SELECTED PRODUCT:  " + matching_product["name"] + " " + "($" + str(matching_product["price"]) + ")")

    individual_price = str(matching_product["price"])
    k = float(individual_price)
    #print(f"PRICE: ${k:,.2f}")

    print("SELECTED PRODUCT:  " + matching_product["name"] + " " + "($" + f"${k:,.2f}" + ")")

print("----------------------------------------------------------")

print(f"SUBTOTAL: ${total_price:,.2f}")

f = float(total_price)
tax = 0.0875
total_plus_tax = f * tax
print(f"AFTER-TAX TOTAL: ${total_plus_tax:,.2f}")

overall = total_price + tax
print(f"TOTAL PLUS TAX: ${overall:,.2f}")

print("----------------------------------------------------------")

print("THANKS FOR SHOPPING! WE HOPE TO SEE YOU AGAIN SOON. ENJOY YOUR FARM-FRESH FOOD, AND CHECK OUR WEBSITE FOR DELICIOUS RECIPE IDEAS!")

print("----------------------------------------------------------")