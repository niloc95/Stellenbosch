#Variable initializing
num1 = 2988566
num2 = 579898
num3 = 9789

#if statement to check if num1 is great than num2
if num1 < num2:
    print(num2, "is greater then num1")
else: 
    print(num1, "is less then num2")

#if statement to check if num1 is odd or even
if (num1 % 2 == 0): 
    print(num1, "is even")
else:
    print(num1, "is odd")

#using python function min and max to sort in order from highest to lowest. 
sort_c = min(num1, num2, num3)
sort_a = max(num1, num2, num3)
sort_b = (num1 + num2 + num3) - (sort_c) - (sort_a)
# prints the sort. 
print("value in a sorted order from highest to lowest: ", sort_a, sort_b, sort_c)


#note to self printing lowest to highest.
sort_c = max(num1, num2, num3)
sort_a = min(num1, num2, num3)
sort_b = (num1 + num2 + num3) - (sort_c) - (sort_a)
# prints the sort. 
print("value in a sorted order from lowest to highest: ", sort_a, sort_b, sort_c)