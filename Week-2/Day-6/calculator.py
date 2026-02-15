def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("\n*** Calculator ***")
    print("1.Add \n2.Subtract \n3.Multiply \n4.Divide \n5.Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting calculator...")
        break

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", addition(a, b))
    elif choice == 2:
        print("Result:", subtraction(a, b))
    elif choice == 3:
        print("Result:", multiplication(a, b))
    elif choice == 4:
        print("Result:", division(a, b))
