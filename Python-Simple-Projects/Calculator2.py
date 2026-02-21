def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_continue = True
    num1 = float(input("Enter the first number: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Enter the second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 5)
            calculator()

calculator()

