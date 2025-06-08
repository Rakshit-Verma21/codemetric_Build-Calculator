#CODEMETRIC : Python Programmer Intern
# Task 1 : Build Calculator
# Create a CMD Calculator to perform basic arithmetic operation


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = "addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "subtraction"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "multiplication"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "division"
            else:
                print("Invalid input. Please select a valid operation.")
                continue

            print(f"The result of the {operation} of {num1} and {num2} is: {result:.2f}")

        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
