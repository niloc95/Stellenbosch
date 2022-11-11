print("\nWelcome to my interpretation of SEL1T12 Compulsory Task 1  'even.py' \n")
# prompting user for input
int_num = int(input("Please enter your number and we will only print the even number: "))
# setting i to 0
i = 0 
# if i is greater or equal to user input
# while i is not equal to user input loop
while i <= int_num:
    # if i can be divided by 2 it is even
    if (i % 2) == 0:
        #print all the even numbers
        print(i, "is even!")
    # increment by 1
    i += 1
# loop till condition is false "int_num"

###################################################################################################

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

###################################################################################################

#printing a welcome note
print("\nWelcome to my interpretation of SEL1T12 Compulsory Task 3 'while.py' \n")
# user input
number = float(input("Please enter your number:  "))
#numbers array init to blank
numbers = []
#while variable is not equal to -1
while number != -1:
    #add items to array
    numbers.append(number)
    #user enter's -1 
    if number == -1:
        # we break the loop
        break
    #this input statement propmts the user to enter more numbers or -1 to break
    #It also importmant to note that the second input is after the break, becuase I didn't, -1 should not be included in the array.
    number = float(input("To break the loop enter '-1' or enter next number: "))
    # calc the avg of the array.
    numbers_avg = float(sum(numbers) / len(numbers))
#print the result with a format. 
print("The avgerage of your numbers are %0.2f" %numbers_avg)