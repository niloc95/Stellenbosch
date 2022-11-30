 
#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T13 Optional Task  'optional_task.py' \n")

#prompts user for input
user_num = input("Enter your number please: ")

#casting the variable 
num = int(user_num)
#if num is greater or equals to 10 keep looping 
if num >= 10:
# while is greater than 0 loop
    while num > 0:
        print("this is the num", user_num)
        num += - 1
# if num is less than 10 
else: 
    print("Sorry too low")