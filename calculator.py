num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

operator = input("Choose (+, -, *, /): ")

if operator == "+":
    print("Answer =", num1 + num2)

elif operator == "-":
    print("Answer =", num1 - num2)

elif operator == "*":
    print("Answer =", num1 * num2)

elif operator == "/":
    print("Answer =", num1 / num2)

else:
    print("Invalid Operator")