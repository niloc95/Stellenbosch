# prompt user for input
num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")
# print the user input 
print (num1, num2)

# now I swapped the varibles, however I needed to store one of the variables before printing
 
swap = num1 # num1 = input from user
num1 = num2 # num1 is now swapped with num2
num2 = swap # num2 is now num1 which was been held by swap
print (num1, num2)
