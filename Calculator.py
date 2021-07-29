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


statement1 = "Do you want to continue the program y/n"
statement2 = "Terminating..."
statement3 = "Invalid Input"
print("Select operation.")
print("1.Add  2.Subtract  3.Multiply  4.Divide  5.Exponents")
print("6.SinO  7.CosO  8.Tan0  9.Square Root  10.Logarithm ")
print("11.Quit/Terminate")

while True:
    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4', '5'):
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
                break

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
                break

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
                break

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
                break

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
                break
    elif choice in ('6', '7', '8'):
        num1 = float(input("Enter the angle: "))

        if choice == '6':
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
                break
        elif choice == '7':
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
                break

        elif choice == '8':
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
                break

    elif choice == '11':
        print(statement2)
        break

    else:
        print(statement3)
