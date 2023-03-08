#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T29 Compulsory Task2 \n")
# Define an Adult class with the constructor and the can_drive method
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
    
    def can_drive(self):
        print(f"{self.name} is old enough to drive.")
# Define a Child class that inherits from the Adult class and overrides the can_drive method
class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")
# Get input from the user for name, age, hair colour, and eye colour
name = input("Enter name: ")
age = int(input("Enter age: "))
hair_colour = input("Enter hair colour: ")
eye_colour = input("Enter eye colour: ")
#Call the can_drive method of the person object
if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)

person.can_drive()
#The code takes input from the user for name, age, hair colour, and eye colour. Based on the age, 
# the code creates an object of either the Adult or the Child class and calls the can_drive method of that object. 
# The Adult class has a can_drive method that prints that the person is old enough to drive, 
# while the Child class overrides the can_drive method to print that the person is too young to drive.