def factorial(num):
    if num < 0:
        return "Enter only positive numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))