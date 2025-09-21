num1 = (input("Enter a number:"))
num2 = (input("Enter another number: "))
operator = input("Choose the operation (+, -, *, /):")
match num1 and num2 and operator:
    case '+':
        print(f"The result is {num1 + num2}")
    case '-':
        print(f"The result is {num1 - num2}")
    case '*':
        print(f"The result is {num1 * num2}")
    case '/':
        print (f"The result is {num1 / num2}")
    case _:
        print("Cannot divide by zero.")
