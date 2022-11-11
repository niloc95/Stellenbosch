
# Initialize a string variable which prompt the user for input
sentence = str(input ("Please enter your sentence: "))
# Assigned user input to new variable 
str_manip = sentence
# Created a variable the hold the replacement char
char_replace = "@"
# Created a varible to manipulation the user input
replace_string = str_manip.replace(str_manip[-1], char_replace)
# prints the output
print(replace_string, "\n")
# printed the user lenght of the string
print(len(str_manip),"\n")
# printed the last three char in revsere
print(str_manip[:-4:-1],"\n")
# This is a contactation for the first three char in 
# in the string joined with the last two char.
print(str_manip[:3] + str_manip[-2:],"\n")
# Prints each word on a new line. 
print(str_manip.replace(" ", "\n"))