num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print("Answer:", num1 + num2)
elif op == '-':
    print("Answer:", num1 - num2)
elif op == '*':
    print("Answer:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Answer:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")