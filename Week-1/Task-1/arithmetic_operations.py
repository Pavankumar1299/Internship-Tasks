def arithmetic_operations(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    if num2 != 0:
        div = num1 / num2
    else:
        div = "Can't divide by zero"
    multi = num1 * num2

    print("***Arithmetic Operations***")
    print("Addition: ", add)
    print("Subtraction: ", sub)
    print("Division: ", div)
    print("Multiplication: ", multi)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

arithmetic_operations(num1,num2)