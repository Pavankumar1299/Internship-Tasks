def prime_no(num):
    if num < 2:
        return "Not a prime number"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not a prime number"
    return "Prime number"

num = int(input("Enter a number: "))
print(num, "is a", prime_no(num))