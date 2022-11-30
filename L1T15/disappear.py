#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T15 Compulsory Task3 'disppear.py' \n")

#User input
user_string = input("Please your sentence: ")
#User to enter char wishing to remove 
remove_char = input("Please enter the charaters you would like to remove: ")
#temp variable for storing chars
temp_string = ""
for i in user_string:
    if i not in remove_char:
        temp_string = temp_string + i 
#prints the final string with the removed chars
print(temp_string)





#Lorem Ipsum is simply dummy text of the printing and typesetting industry