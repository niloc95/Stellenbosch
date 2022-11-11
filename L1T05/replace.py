
# initialize a string variable  
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

# Printed the string, with .replace for "!" to Blank
print(sentence.replace("!", " ")[0:43] +".")
# assigned new variable with the formatted parameters 
new_sentence = sentence.upper().replace("!", " ")
# printed the new variable
print(new_sentence[0:43] +".")
# to remove the blank space between the "DOG . to DOG." 
newer_sentence = new_sentence[0:43] +"."
# printed using the Slice notation
print(newer_sentence[::-1])
