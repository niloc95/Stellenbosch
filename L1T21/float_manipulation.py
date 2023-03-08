import math
import statistics
user_num = []
# I am the user to enter the how many number he or she will like to calulate.
user_num_range = int(input("Please enter your 10 numbers, whole number and decimals: "))
# using a for loop init from 0 to the user range
for i in range(0, user_num_range):
    # asking the user to enter a float or int.
     user_float = float(input())
    # i am appendind to the list 
     user_num.append(user_float)
#Find the total of all the numbers and print the result.
total_sum = sum(user_num)
print("Total of the list is: " + str(total_sum))
#Find the index of the maximum and print the result.
print("This is the index of the max float: ", (user_num.index(max(user_num))))
##Find the index of the minimum and print the result.
print("This is the index of the min float: ", (user_num.index(min(user_num))))
#Calculate the average of the numbers and round off to 2 decimal places.
average = total_sum / user_num_range
print("The average of the list is:  %.2f" % average)
#Find the median number and print the result.
med_result = statistics.median(user_num)
print("Median of list is : " + str(med_result))

# Dear Armand, Thank you for that, herewith is the updated / revised version. 