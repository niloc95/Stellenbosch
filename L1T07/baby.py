# Import the datetime function
import datetime
#defines today's date using the date function
today = datetime.date.today()
# prompt use for input
dob_year = int(input("Please your DOB year: "))
# storing the current year in year
year = today.year
# age verifcation 
ent_age = 18
# calc the today's year against the user DOB year
age = year - dob_year
# My if statement 
if ent_age <= age:
    print("Congrats you are old enough:", + age)
if ent_age >= age: 
    print("Oh no, few many years to go youngster give it time:", + age)
