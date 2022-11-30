#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T15 Optional Task 'optional.py' \n")

word = input("Please enter your word so we can check if it's a palindrome or not \nYour word: ")

if word == word[::-1]:
    print (word, "is a palindrome:")
else: 
    print (word ,"is not a palindrome:")




