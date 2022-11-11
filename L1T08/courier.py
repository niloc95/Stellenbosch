#Variable for categories 
# Option 1 - Method of Transport
air_freight = 0.36
ground_freight = 0.25

#Option 2 - Insurance type
full_insurance = 50.00
limited_insurance = 25.00

#Option 3 - Gift
yes_gift = 15.00
no_gift = 0.00

#Option 4 - Shipping Service
priority = 100.00
std_priority = 20.00

#prompt user for input
price = float(input("Please enter the price of the package: "))
distance = float(input("Please enter the distance of the delivery in kms: "))


#user to choose options
print("Please choose your shipping preferences: \n")
freight = input("Would you like to send your parcel via Air or Ground?:\nYes - Air Shipping(R0.36/km) \nNo - Standard Ground Shipping(R0.25/km) \nEnter your selection: \n")
if (freight == "Yes"):
    freight = air_freight
    print(freight)
else: 
    if (freight == "No"):
        freight = ground_freight
        print(freight)


insurance = input("Would you like insurance?:\nYes - Full Insurance Cover(R50.00) \nNo - Limited Insrance Cover (R25.00)\nEnter your selection: \n")
if (insurance == "Yes"):
    insurance = full_insurance
    print(insurance)
else: 
    if (insurance == "No"):
        insurance = limited_insurance
        print(insurance)

gift = input("Would you like gift add to your parkage:\nYes - I want a Gift(R15.00) \nNo - I don't want gift(R0.00)\nEnter your selection: \n")
if (gift == "Yes"):
     gift = yes_gift
else: 
    if (gift == "No"):
        gift = no_gift
    


service = input("What service do you perfer?\nYes - Priority Service(R100.00)\nNo - Standard Delivery(R20.00)\nEnter your selection: \n")
if (service == "Yes"):
    service = priority
else: 
    if (service == "No"):
        service = std_priority
       
#assign a new variable to calulate the total cost
package_cost = price + distance*freight + insurance + gift + service


print("The cost of your package will be: R%0.2f" %package_cost)



# print(price, distance)