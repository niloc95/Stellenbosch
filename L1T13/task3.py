#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T13 Compulsory Task3  'task3.py' \n")

# Python range 
#Create a while loop that will display count down from 20 to 0.
myRange = range(1, 21)
# Used the reversed function to print 20 to 0
for n in reversed(myRange):
    if (n % 2 == 0):
     print("Even number: ", n)
    elif (n % 2 == 1):
     print("Odd number: ", n)


#Printing all even number between 1 and 20
x = [1, 20]
i = 1

while i <= 19:
    if i % 2 == 0:
      print(i, "this is even")
    i += 1  

#Loop pattern printing stars
#stars = int(input("Please the enter the number row wish to see "))
stars = 5  
# outer loop to handle number of rows  
for outer in range(0, stars):  
    # inner loop to handle number of columns  
    # values is changing according to outer loop  
        for inner in range(0, outer + 1):  
            # printing stars  
            print("*", end = " ")
        # ending line after each row  
        print("\r")


#Finally, write the code to compute the greatest common divisor (GCD, or
#highest common factor) of two positive integers.

num_1 = int(input('Please input the first integer:'))
num_2 = int(input('Please input the second integer:'))
 
for i in range(1, num_2 + 1):
    if num_1 % i == 0 and num_2 % i == 0:
        gcd = i
print(gcd)