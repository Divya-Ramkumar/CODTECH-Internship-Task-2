#Calculator

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input("Enter the operation number (1/2/3/4): "))

# Perform the selected operation
if operation == 1:
    result = addition(num1, num2)
elif operation == 2:
    result = subtraction(num1, num2)
elif operation == 3:
    result = multiplication(num1, num2)
elif operation == 4:
    result = division(num1, num2)
else:
    result = "Error: Invalid operation chosen"

# Display the result to the user
print("The result is:", result)
