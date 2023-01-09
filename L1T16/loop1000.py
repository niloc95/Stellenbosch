#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T16 Compulsory Task2 'loop1000.py' \n")

# Using the range function to print 1 to 1000
num1k = list(range(1,1001))
print(num1k)
#Statement for all even number from 1 to  a 1000
for i in (num1k): 
    if (i % 2 == 0): 
        print(i, "This is an even number")
    #if (i % 2 == 1):
    #    print(i, "is odd")