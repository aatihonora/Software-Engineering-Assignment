# Assignment for Software Engineering by Behram Akhtar (2K19/CSM/17) and Ghullam Sarwar (2K19/CSM/27)

# I am going to make some basic operation function as I am not very good at python can you make the complex ones (
# Ghullam Sarwar)
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


print("Select operation.")
print("1.Add  2.Subtract  3.Multiply  4.Divide  5.Exponents")
print("6.Quit/Terminate")

while True:
    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            print("Do you want to continue the program y/n")
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print("Terminating...")
                break
            else:
                print("Invalid answer")
                break

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            print("Do you want to continue the program y/n")
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print("Terminating...")
                break
            else:
                print("Invalid answer")
                break

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            print("Do you want to continue the program y/n")
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print("Terminating...")
                break
            else:
                print("Invalid answer")
                break

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            print("Do you want to continue the program y/n")
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print("Terminating...")
                break
            else:
                print("Invalid answer")
                break

        elif choice == '5':
            print(num1, "^", num2, "=", exponents(num1, num2))
            print("Do you want to continue the program y/n")
            answer = input()
            if answer.lower() == 'y':
                continue
            elif answer.lower() == 'n':
                print("Terminating...")
                break
            else:
                print("Invalid answer")
                break

    elif choice == '6':
        print("Terminating...")
        break

    else:
        print("Invalid Input")
        continue
