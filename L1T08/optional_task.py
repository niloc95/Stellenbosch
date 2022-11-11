#Declare Variable
fixed_sales_salary = 2000
manager_rate = 40
commission = 1.08

# Print welcome message 
print("Welcome to my basic salary calculator\n")

#Determine if user is a Sales person or manager, using an integate variable 
type_emp = int(input("Are you a Sales Person or Manager?:\n1 - Sales Person \n2 - Manager\nEnter your selection: "))

# 1 is received we know its a sales person
if (type_emp == 1):
# Than prompt sales person to enter their total sales for the month
    t_sales = float(input("Please enter total sales made for the month: "))
# Cal the total salary, sales + gross * 8% commission
    type_emp = (t_sales + fixed_sales_salary) * commission
# print result with format in Rands with 2 decimal point
    print("Your earning is as follows:\n", "Total Sales R %0.2f" %t_sales,"Excluding Commission\n", "Gross Salary R %0.2f" %fixed_sales_salary,"Excluding Commission\n",  "Total Salary R %0.2f" %type_emp, "Including Commission")
else: 
# 2 is received we know its a cheap manager     
    if (type_emp == 2):
# Than prompt manager to enter total hours worked for the month
        t_hours = float(input("Please enter total hours worked: "))
# Calc total salary 
        type_emp = (t_hours * manager_rate)
# print result with format in Rands with 2 decimal point         
        print("Great Mr Manager your salary for this month is:\n","Total hours %0.2f\n" %t_hours, "Total Salary R %0.2f" %type_emp)



