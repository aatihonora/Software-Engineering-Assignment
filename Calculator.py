# Assignment for Software Engineering by Behram Akhtar (2K19/CSM/17) and Ghullam Sarwar (2K19/CSM/27)

# I am going to make some basic operation function as I am not very good at python can you make the complex ones (
# Ghullam Sarwar)

import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exponents(x, y):
    return x ** y


def percentage(x, y):
    quotient = x / y
    return quotient * 100


statement1 = "Do you want to continue the program y/n"
statement2 = "Terminating..."
statement3 = "Invalid answer"
print("Select operation.")
print("1.Add  2.Subtract  3.Multiply  4.Divide  5.Exponents  6.Percentage")
print("7.Sin0  8.Cos0  9.Tan0  10.Square Root  11.Logarithm  12.Anti-Logarithm")
print("13.Quit/Terminate")

while True:
    print("Select operation.")
    print("1.Add  2.Subtract  3.Multiply  4.Divide  5.Exponents  6.Percentage")
    print("7.Sin0  8.Cos0  9.Tan0  10.Square Root  11.Logarithm  12.Anti-Logarithm")
    print("13.Quit/Terminate")
    choice = input("Enter the choice (1 to 13): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

        elif choice == '5':
            print(num1, "^", num2, "=", exponents(num1, num2))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

        elif choice == '6':
            print(f"Percentage of {num1 / num2} =", percentage(num1, num2))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

    elif choice in ('7', '8', '9'):
        num1 = float(input("Enter the angle: "))

        if choice == '7':
            degree = num1 * 0.0174532925
            print(f"Sin0 {num1}° =", round(math.sin(degree), 4))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

        elif choice == '8':
            degree = num1 * 0.0174532925
            print(f"Cos0 {num1}° =", round(math.cos(degree), 4))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

        elif choice == '9':
            degree = num1 * 0.0174532925
            print(f"Tan0 {num1}° =", round(math.tan(degree), 4))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

    elif choice in ('10', '11', '12'):
        num1 = float(input("Enter the value: "))

        if choice == '10':
            print(f"Square root of {num1} =", math.sqrt(num1))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

        elif choice == '11':
            print(f"Logarithm of {num1} =", math.log(num1, 10))
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

        elif choice == '12':
            print(f"Anti-Logarithm of {num1} =", 10 ** num1)
            print(statement1)
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print(statement2)
                break
            else:
                print(statement3)

    elif choice == '13':
        print("Terminating...")
        break

    else:
        print("Invalid Input")
