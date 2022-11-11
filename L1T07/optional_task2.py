# Variable declaration as a boolean value
temp_ver = True
weekend = True
sunny_check = True

# Prompts for user input which evaluate to Yes or No
temperture = input("Is the temperture higher than 20 degrees: \n(Yes or No): " )
# if statement to the check the user input against the variable
if temperture == "Yes": 
    temp_ver = False
# assigning a string value to the variable 
    temp_ver = "short-sleeved shirt"

# Prompts for user input where evaluate to Yes or No
weekend_check = input("Is it the weekend \n(Yes or No): ")
# if statement to the check the user input against the variable
if weekend_check == "Yes": 
    weekend = False
# assigning a string value to the variable
    weekend = "shorts"

# Prompts for user input where evaluate to Yes or No
sunny_day = input("Is it a sunny day \n(Yes or No): ")
# if statement to the check the user input against the variable
if sunny_day == "Yes":
    sunny_check = False
# assigning a string value to the variable
    sunny_check = "sun cap"


if temp_ver == True:
# assigning a string value to the variable
    temp_ver = "long-sleeved shirt"

if weekend == True:
# assigning a string value to the variable
    weekend = "jeans"

if sunny_check == True: 
# assigning a string value to the variable    
    sunny_check = "raincoat"

# Final print statement based on the asnwer / input from user
print("Wearing the following items based on the weather will make good sense:\n","You should wear a "+ temp_ver,"with a pair of " + weekend,"and you may want to carry a " + sunny_check)


