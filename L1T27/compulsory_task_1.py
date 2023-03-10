import operator
# define a dictionary to map operators to their corresponding functions
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

# function to get input from user for two numbers and operator
def get_input():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter operator (+, -, *, /): ")
            if op not in ops:
                raise ValueError("Invalid operator")
            return num1, num2, op
        except ValueError as e:
            print("Error:", e)

# function to perform the calculation and return the result
def calculate(num1, num2, op):
    return ops[op](num1, num2)

# function to write the equation to a text file
def write_equation(num1, num2, op, result):
    with open("equations.txt", "a") as f:
        f.write(f"{num1} {op} {num2} = {result}\n")

# function to read equations from a file and print them out with results
def read_equations():
    while True:
        try:
            filename = input("Enter filename: ")
            with open(filename) as f:
                equations = f.readlines()
            break
        except FileNotFoundError:
            print("Error: file not found")
    for equation in equations:
        try:
            num1, op, num2, result = equation.split()
            num1, num2, result = float(num1), float(num2), float(result)
            print(f"{str(num1)} {str(op)} {str(num2)} = {str(result)}")
        except (ValueError, TypeError):
            print(equation)

# main function to run the program
def main():
    while True:
        try:
            choice = input("Enter '1' to calculate, '2' to read equations from a file, or 'q' to quit: ")
            if choice == "1":
                num1, num2, op = get_input()
                result = calculate(num1, num2, op)
                write_equation(num1, num2, op, result)
                print(f"{num1} {op} {num2} = {result}")
            elif choice == "2":
                read_equations()
            elif choice == "q":
                break
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()