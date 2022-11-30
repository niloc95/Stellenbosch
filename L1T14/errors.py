# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.


# print the missing the brackets - Syntax error
# Indentation error
print ("Welcome to the error program")
# print the missing the brackets - Syntax error
# Indentation error
print ("\n")
# assignment operator error 
ageStr = 24.5 #I'm 24 years old.
age = float(ageStr)
#typeError trying to add string with an Integer. 
print("I'm", age , "years old.")
#typeError: variable init ot a string 
three = 3

answerYears = age + three
#syntaxError missing the parenteses
print ("The total number of years:" , answerYears)
#NameError answer is not defined
answerMonths = answerYears * 12
#syntaxError missing the parenteses
print ("In 3 years and 6 months, I'll be ", answerMonths, " months old")