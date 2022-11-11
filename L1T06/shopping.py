#import the module
import math

# prompt user to enter products 
prod_1 = str(input("Please enter name of product 1: "))
prod_2 = str(input("Please enter name of product 2: "))
prod_3 = str(input("Please enter name of product 3: "))

# prompt user to prices 
price_1 = float(input("Please enter price 1: "))
price_2 = float(input("Please enter price 2: "))
price_3 = float(input("Please enter price 3: "))

# adding the value of the three product prices
total_sum = price_1 + price_2 + price_3
total_price = [price_1, price_2, price_3]

# calc for the average, using the a float varible
price_avg = float(sum(total_price) / len(total_price))

# printing the average and rounding the float
print(round(price_avg))
# finish step 
print ("The Total of " + prod_1 +", " + prod_2 + "and " + prod_3, "is R{}".format(total_sum) + " and the average price of the items is R{}" .format(price_avg))