import copy
#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T20 Compulsory Task1 'cafe.py' \n")
#list menu items
menu = ['Starters', 'Mains', 'Deserts', 'Drinks']
# Dictionary items
stock = {'Starters': 4,
         'Mains': 4,
         'Deserts': 2,
         'Drinks': 8,
         }
# dictionary prices for menu items
price = {'Starters': 45,
         'Mains': 34,
         'Deserts': 20,
         'Drinks': 9,
         }

#init variable total stock = 0
total_stock = 0

# loop to add the total stock on hand
for item in menu:
    qty = stock[item]
    total_cost = price[item]

    total_stock = total_stock + qty * total_cost

# print totals
    print('Total stock we holding: R', total_stock )