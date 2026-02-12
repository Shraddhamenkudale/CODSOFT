# Calculator Program

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


while True:
    print("\n====== SIMPLE CALCULATOR ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an operation (1-5): ")

    if choice == "5":
        print("Calculator closed. Thank you!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                print("Result:", result)

            elif choice == "2":
                result = subtract(num1, num2)
                print("Result:", result)

            elif choice == "3":
                result = multiply(num1, num2)
                print("Result:", result)

            elif choice == "4":
                result = divide(num1, num2)
                print("Result:", result)

        except ValueError:
            print("Please enter valid numeric values.")
    else:
        print("Invalid choice. Please select between 1 and 5.")
