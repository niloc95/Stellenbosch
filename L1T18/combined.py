#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T18 Compulsory Task2 'combined.py' \n")

#assigning a variable to the text file
numbers1 = 'numbers1.txt'
numbers2 = 'numbers2.txt'
all_numbers = 'all_numbers.txt'

# opening and reading the first text file
f_num1 = open (numbers1, 'r')
set_num_1 = f_num1.read().split() 

# opening and reading the second text file
f_num2 = open (numbers2, 'r')
set_num_2 = f_num2.read().split()

# file to store write value
f_all = open(all_numbers, 'w')

# temp variables  
temp_file_1 = 0
temp_file_2 = 0

# open the file checks both file content and write in ascending order
while temp_file_1 < len(set_num_1) and temp_file_2 < len(set_num_2):
    data_set_1 = int(set_num_1[temp_file_1])
    data_set_2 = int(set_num_2[temp_file_2])
    if data_set_1 <= data_set_2:
        # writes the lowest int to file all_numbers.txt
        f_all.write(str(data_set_1) + '\n' )
        temp_file_1 += 1 #increments the index 

    elif data_set_1 > data_set_2:
        f_all.write(str(data_set_2) + '\n')
        temp_file_2 += 1 #increments the index
# write the remaining items to the temp variable.txt
while temp_file_1 < len(set_num_1):
    f_all.write(str(set_num_1[temp_file_1]) + '\n')
    temp_file_1 += 1
# write the remaining items to the all_numbers.txt
while temp_file_2 < len(set_num_2):
    f_all.write(str(set_num_2[temp_file_2]) + '\n')
    temp_file_2 += 1

print('All done, Please check all_numbers.txt')
#finally closes all the files. 
f_all.close()
f_num1.close()
f_num2.close()