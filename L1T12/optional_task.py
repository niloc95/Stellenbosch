#printing a welcome note
print("\nWelcome to my interpretation of SEL1T12 Optional Task 'Optional_task.py' \n")

user_number = 0 
while user_number == 0:
    numbers = int(input("Please enter a number less than 100: \nEnter your number: "))
    if numbers <= 100:
        user_number = 1
if (numbers % 2) == 0:
    print((numbers) * 2, "that's the magic number ")
else:
    print((numbers) * 3, "that's an odd number ")