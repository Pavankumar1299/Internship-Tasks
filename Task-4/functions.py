def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("Addition:", addition(x, y))
print("Subtraction:", subtraction(x, y))
print("Multiplication:", multiplication(x, y))
print("Division:", division(x, y))