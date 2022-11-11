# BMI calculator - 
print("\nWelcome to the BMI(Body Mass Index) calculator: \n")
weight = float(input("Please enter your weight in 'Kilograms': "))
height = float(input("Please enter your height in 'cm': "))
cms_height = (height / 100)
#Reads user weight, Height
bmi = (weight) / ((cms_height) * (cms_height))

#if statement with three conditions
if (bmi > 30):
    print("Hooray! Your BMI result is ready.")
    print("Your BMI is %0.2f = Obese!" % bmi)
elif (bmi > 25):
    print("Hooray! Your BMI result is ready.")
    print("Your %0.2F = Overweight!" % bmi)
elif (bmi > 18.5 ):
    print("Hooray! Your BMI result is ready.")
    print("Your BMI is %0.2f = Normal!" % bmi)
elif (bmi < 18.5):
    print("Hooray! Your BMI result is ready.")
    print("Your BMI is %0.2f = Under weight! " % bmi )
else: 
    print("Invalid - Please try again")
