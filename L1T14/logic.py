#prompts user for input
user_num = input("Enter your number please: ")

 
num = int(user_num)
# because I used the not equal to 10 the second condition else statement will never interate 
if num != 10:

    while num > 0:
        print("this is looping infinitely")
#indentation is incorrect thus creating a logic error and looping infinitely  
    num += - 1
else: 
    print("Sorry too low")

