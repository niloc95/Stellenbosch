#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T18 Compulsory Task1 'student_register.py' \n")

#variable for total number of student registering
student_count = int(input("Please enter the total number of students you wish to register: "))
#creating and opening a file as 'f'
with open('reg_form.txt', 'w+', encoding='utf-8') as f:
    #loop thru the total number of students
    for stu in range(student_count):
        #ask the user for all the student ID's
        id = input ("Please enter student ID number: ")
        #writing to the output file
        f.write(id + "\n")
   
f.close


