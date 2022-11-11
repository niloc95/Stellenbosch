
# Importing math Library
import math

print("\nWelcome Hyper Builders, note all calculation are in meters\n")
#User to enter the shape of build they want to build
type_building = input("Please choose one of the buliding shapes you prefer: \nSquare Structure\nRectangle Structure\nCircle Structure, \nPlease enter the type: ").capitalize()


#Variables initializing
area = 0
# pi = 3.14
# using the math Libaurary
calc_pi = (math.pi)

#if statement based on user choices

if type_building == ("Square"):
    length = float(input("Please advise the height you wish to build?: "))
    #calculates if the user enters square
    area = length ** 2
    print("The require foundation area for a",type_building.capitalize(), "shaped building will be %0.2f square meters" %area)
elif type_building == ("Rectangle"):
    #else calculates rectangle
    length = float(input("Please advise the height you wish to build?: "))
    width = float(input("Please advise the width you wish to build?: "))
    area = length * width
    print("The require foundation area for a",type_building.capitalize(), "shaped building will be %0.2f square meters" %area)
elif type_building == ("Circle"):
    #else calculates a circle
    radius = float(input("What will the radius length be?: "))
    area = calc_pi * (radius ** 2) 
    print("The require foundation area for a",type_building.capitalize(), "shaped building will be %0.2f square meters" %area)
else: 
    #prints if the user enters an invalid building
    print("Sorry, only a 'Square, Rectangle or Circle'")

    
