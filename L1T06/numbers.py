# User input request
num_1 = int(input("Please number 1: "))
num_2 = int(input("Please number 2: "))
num_3 = int(input("Please number 3: "))

# task_1 sum of all three numbers
t_out_1 = num_1 + num_2 + num_3
# printing the result 
print(t_out_1)

# task_2 first number minus the second number
t_out_2 = num_1 - num_2
# printing the result 
print(t_out_2)

# task_3 third number multiplied by the first number
t_out_3 = num_3 * num_1
# printing the result
print(t_out_3)

# task_4 sum of all three numbers divided by the third number
t_out_4 = ((num_1 + num_2 + num_3) / 3)
# printing the the result using the remainder modulos with 2 decimal points 
print("%0.2f" %t_out_4) 