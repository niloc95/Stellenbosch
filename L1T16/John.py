#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T16 Compulsory Task3 'John.py' \n")

name = ""
storednames = []
while name != "John":
    name = input ("Please enter your names: ")
    storednames.append(name)
print("Incorrect Names: ",storednames[0:-1])