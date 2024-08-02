import math

#addition
def add(x, y):
    return x + y

# subtraction
def subtract(x, y):
    return x - y

# multiplycation
def multiply(x, y):
    return x * y

# division
def divide(x, y):
    if y == 0:
        return "not divide by zero!"
    else:
        return x / y

# Factorial
def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative number"
    elif x == 0:
        return 1
    else:
        return math.factorial(x)

#calculate power of a number
def power(x, y):
    return x ** y

#square root of a number
def square_root(x):
    if x < 0:
        return "Square root is not defined for negative number"
    else:
        return math.sqrt(x)

#log base 10
def log10(x):
    if x <= 0:
        return "Log is not defined for non-positive numbers"
    else:
        return math.log10(x)

#log base e
def log(x):
    if x <= 0:
        return "Log is not defined for non-positive numbers"
    else:
        return math.log(x)

# Main function
def main():
    print("Welcome to Advanced Scientific Calculator!")
    print("Operations supported:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Factorial (!)")
    print("6. Power (x^y)")
    print("7. Square Root (√x)")
    print("8. Logarithm (log10)")
    print("9. Natural Logarithm (ln)")

    while True:
        choice = input("\nEnter operation number to perform (or 'q' to quit): ")

        if choice == 'q':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice in ['5', '7', '8', '9']:
            try:
                num = float(input("Enter number: "))
                if choice == '5':
                    print(f"Factorial of {num} is {factorial(int(num))}")
                elif choice == '7':
                    print(f"Square root of {num} is {square_root(num)}")
                elif choice == '8':
                    print(f"Log (base 10) of {num} is {log10(num)}")
                elif choice == '9':
                    print(f"Natural log of {num} is {log(num)}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice in ['1', '2', '3', '4', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '6':
                    print(f"{num1} ^ {num2} = {power(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        else:
            print("Invalid choice. Please entr a valid operation numbers.")

if _name_ == "_main_":
    main()
