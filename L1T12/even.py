#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T12 Compulsory Task1  'even.py' \n")
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