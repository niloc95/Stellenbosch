def minimum(lst):
    min_value = lst[0] #initialize minimum value to first element of list
    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
    return min_value

def maximum(lst):
    max_value = lst[0] #initialize maximum value to first element of list
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
    return max_value

def average(lst):
    total = 0 #initialize total to 0
    for i in range(len(lst)):
        total += lst[i] #add each value to the total
    return total / len(lst) #divide total by number of values to get average

with open('input.txt') as textFile :
    # Reading the file
    textRead = textFile.read()

#Opening and writing to the output file "output.txt"
text_files = open("output.txt", "x")
text_files = open("output.txt", "w")

#Looping through each line of the file
for line in textRead.split('\n') :
    # Splitting the line by ':' to separate operation and list of numbers
    operations, numbers = line.split(':')
    operations = operations.strip()  
    numbers = list(map(int, numbers.strip().split(","))) #convert comma separated numbers to list of integers

    if operations == 'Avg':
        text_files.write(f'The avg of {numbers} is {average(numbers)}\n')

    if operations == 'Min':
        text_files.write(f'The min of {numbers} is {minimum(numbers)}\n')

    if operations == 'Max' :
        text_files.write(f'The max of {numbers} is {maximum(numbers)}\n')

text_files.close()
text_files = open("output.txt", "r")
print(text_files.read())

#**********************************************************************************************************************#
# # Funcition import
# import statistics

# def minimum(lst):
#     min_value = lst[0] #initialize minimum value to first element of list
#     for i in range(1, len(lst)):
#         if lst[i] < min_value:
#             min_value = lst[i]
#     return min_value

# def maximum(lst):
#     max_value = lst[0] #initialize maximum value to first element of list
#     for i in range(1, len(lst)):
#         if lst[i] > max_value:
#             max_value = lst[i]
#     return max_value

# def average(lst):
#     total = 0 #initialize total to 0
#     for i in range(len(lst)):
#         total += lst[i] #add each value to the total
#     return total / len(lst)

# with open('input.txt') as textFile :
#     # Reading the file
#     textRead = textFile.read()
# #Opening and writing to the output file "out.txt" 
# text_files = open("out.txt", "x")
# text_files = open("out.txt", "w")
# #Looping thru each line of the file
# for line in textRead.split('\n') :
#     operations, numbers = line.split(':')
#     operations = operations.strip()  
#     numbers = map( float, numbers.strip().split(",") )

#     if operations == 'Avg':
#         text_files.write('\nThe value of average of [1,2,3,5,6] is '+str(average(numbers)))

#     if operations == 'Min':
#         text_files.write('The value of min of [1,2,3,5,6] is '+str(min(numbers)))

#     if operations == 'Max' :
#         text_files.write('\nThe value of max of [1,2,3,5,6] is '+str(max(numbers)))

# text_files.close()
# text_files = open("out.txt", "r")
# print(text_files.read())