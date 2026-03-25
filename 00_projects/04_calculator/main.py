from art import logo

print(logo)


def calculator(num_1, operation, num_2):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "*":
        return num_1 * num_2
    else:
        return num_1 / num_2

over = False
first_time = True

while not over:
    if first_time:
        num_1 = float(input("What's the first number?: "))
    else:
        num_1 = results

    operation = input("+\n-\n*\n/\nPick an operation: ")
    num_2 = float(input("What's the next number?: "))

    if operation not in ["+", "-", "/", "*"]:
        print("Invalid operation")
        over = True
    elif num_2 == 0 and operation == "/":
        print("Error: Division by zero")
        over = True
    else:
        results = round(calculator(num_1, operation, num_2), 2)
        print(f"{num_1} {operation} {num_2} = {results}")
        continue_calculation = input(f"Type 'y' to continue calculating with {results}, or type 'n' to start a new calculation: ").lower()
        if continue_calculation == "y":
            first_time = False
        else:
            over = True
