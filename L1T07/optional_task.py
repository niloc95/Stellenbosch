#prompt user for input used a flaot 
int_num = float(input("Please enter your number and we will confirm if your number is odd or even: "))
# if statement testing for odd or even
# tried both modulos opeartor and / division 
# however divsion wont work, Therefore the modulos operator works
# Divide the number by two and if there is a remainder the number is odd.  
if (int_num % 2) == 0:
    print(int_num, "Brilliant your number is even!" )

if (int_num % 2 ) == 1: 
    print (int_num, "Your number is odd!")
