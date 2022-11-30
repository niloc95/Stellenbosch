#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T15 Compulsory Task1  'alternative.py' \n")

#init string to a string "Hello World"
string = "Hello World"
#create a blank variable to the store the upper and lower case letters
store_string = ""
# looping thru the string using a range and the len methods
for i in range(len(string)):
#if statement is looping thru ever alternative char 
    if i % 2 == 0:
        store_string = store_string + string[i].upper()
    else: # if i % 1 == 0
        store_string = store_string + string[i].lower()
print(store_string)



