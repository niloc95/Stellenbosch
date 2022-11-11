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