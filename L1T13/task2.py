#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T13 Compulsory Task2 'task2.py' \n")
# prompting user for input

start_year = int(input("What year do you want to start with?: "))
total_years = int(input("How many years do you want to check?: ")) 


for year in range(start_year, start_year + total_years):

        if year % 4 == 0:       
                print(f"{year} is a leap year") 
        else:
                print (f"{year} isn't a leap year")