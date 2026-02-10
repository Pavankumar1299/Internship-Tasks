num = int(input("Enter a number: "))

print("Pattern: 1")
for i in range(num):
    for j in range(i+1):
        print("*", end = " ")
    print()

print("\nPattern: 2")
for i in range(num, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()

print("\nPattern: 3")
for i in range(num):
    print(" " * (num - i - 1), end="")
    for j in range(i+1):
        print("*", end = " ")
    print()