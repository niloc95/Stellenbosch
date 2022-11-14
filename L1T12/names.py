#printing a welcome note
print("\nWelcome to my interpretation of SEL1T12 Compulsory Task 2 'names.py' \n")
# user input
stu_name = input("Please enter student names to build class list: \nYou may break by typing 'stop'. \nNames please: ")
#names array init to blank
names = []
#while variable is not equal to "stop"
while stu_name != "Stop":
    #add item to array
    names.append(stu_name)
    #user enter's stop 
    if stu_name == "Stop":
        # we break the loop
        break
    #this input statement propmts the user to enter more name or stop to finish
    #It also importmant to note that the second input is after the break, becuase i didn't,
    #want to add the "Stop" word to the array.
    
    stu_name = input("'Stop' to finish or next name: ").capitalize()
print(f"Here's your list: {names}")