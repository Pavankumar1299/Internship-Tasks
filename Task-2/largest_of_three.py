def largest_of_three(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
num3 = int(input("Enter third num: "))

res = largest_of_three(num1,num2,num3)
print("Largest number is: ", res)