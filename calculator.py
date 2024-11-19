def calculator():
    """Performs basic arithmetic operations based on user input."""

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = int(input("Enter choice(1/2/3/4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Invalid input. Please enter a valid choice (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == 4:
        print(num1, "/", num2, "=", divide(num1, num2))

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

calculator()
