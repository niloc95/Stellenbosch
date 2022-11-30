# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#SyntaxError animal = str("lion")
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16
#variable was missing the f-string format 
#syntaxError missing the parenteses
full_spec = (f"This is a {animal}. It is a {number_of_teeth} tooth and it has {animal_type} teeth")

#syntaxError missing the parenteses
print (full_spec)

