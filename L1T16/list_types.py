#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T16 Compulsory Task1 'list types.py' \n")

#list with names
friends_names = ["Peter", "Paul", "Mark"]
#print statement for first and last name with len function.
print(friends_names[0], "&",friends_names[2],"\nThere are", len(friends_names), "names in your list")
#print(len(friends_names))

#Ages list
friends_ages = ["4","13","14"]
# init a temp variable to 0  
ages = 0
# while ages less then friends_names add the corresponding ages.
while ages < len (friends_names):
    print(friends_names[ages], friends_ages[ages])
    ages += 1
 