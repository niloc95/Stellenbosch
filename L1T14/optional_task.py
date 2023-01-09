#SyntaxError parentheses not closed
user_num = str(input("Enter your number please: "))

# because I used the not equal to "10" the second condition or else statement will never iterate 
if num != 10:
#here is a NameError due to the variable is declared after "num"
    num = int(user_num)
    while num > num:
        print("this is looping infinitely")
#indentation is incorrect thus creating a logic error and looping infinitely  
    num += - 1
else: 
    print("Sorry too low")

    