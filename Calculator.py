def calculator():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice : "))

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if choice == 1:
        result = number1 + number2
        print(f"{number1} + {number2} = {result}")
    elif choice == 2:
        result = number1 - number2
        print(f"{number1} - {number2} = {result}")
    elif choice == 3:
        result = number1 * number2
        print(f"{number1} * {number2} = {result}")
    elif choice == 4:
        if number2 != 0:
            result = number1 / number2
            print(f"{number1} / {number2} = {result}")
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    calculator()