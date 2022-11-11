# importing the math module
import math

# prompting the use for input
side1 = int(input("Please enter the lenght of side 1 in meters: "))
side2 = int(input("Please enter the lenght of side 2 in meters: "))
side3 = int(input("Please enter the lenght of side 3 in meters: "))

# calc the total perimeter of the triangle
total_perim = (side1 + side2 + side3) / 2

# calc total area using a float
area = float((total_perim * (total_perim-side1) * (total_perim-side2) * (total_perim-side3)) ** 0.5)

# printing using the math.trunc function
print ("The area of your triangle is", + math.trunc(area), "Square Meters")

# printing usng the f-string notation "%O placeholder 
# .2 is for decimal points
print ("The area of your triangle is %0.2fm" %area)

