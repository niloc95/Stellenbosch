#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T17 Compulsory Task 'compulsorytask.py' \n")

#opening the txt file with the read access modifer
file_dob = open('DOB.txt', 'r+')
#delcaring a variable to read the line in the file
lines_dob = file_dob.readlines()
#printing the first row heading
print("\n\033[1m"+"Name"+" \033[0m")
#statement to split the names 
for row_name in lines_dob:
    names = row_name.split(',')
    print(names[0])

#statement to split the birthday 
print("\n\033[1m"+"Birthday"+" \033[0m")
for row_dob in lines_dob:
    dob = row_dob.split(',')
    print(dob[1].strip('\n'))

file_dob.close()