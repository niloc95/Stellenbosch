#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T13 Compulsory Task1  'task1.py' \n")
# prompting user for input
user_multipier = int(input("Please enter the multiplication table you wish to learn?: "))

for x in range(1, 13):
    print(x, "x", user_multipier, "=", (x * user_multipier) )
