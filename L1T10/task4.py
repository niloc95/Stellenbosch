#prints a welcome message
print("\nWelcome to Task 4, L1T10\n")
#User to enter time for each event
num = int(input("Please enter your magic number: "))

# if statement to check
# 2 * 5 = 10 first condition

if num % 10 == 0:
    print("Divisible by 2 and 5", num)

elif num % 2 == 0:
    print("divisible by 2 not divisible by 5")

elif num % 5 == 0:
    print("divisible by 5 not divisible by 2")

else:
    print("not divisible by 2 not divisible by 5", num)