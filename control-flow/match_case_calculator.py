num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

can_print = True
result = 0.0

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            can_print = False
        else:
            result = num1 / num2
    case _:
        print("Invalid operation.")
        can_print = False

if can_print:
    print(f"The result is {result}.")
