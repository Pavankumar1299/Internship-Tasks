print("***logical Python problems***")
print("Problem 1: Check if a number is even or odd")
num = 7
if num % 2 == 0:
    print("Number is: Even")
else:
    print("Number is: Odd")

print("\nProblem 2: Reverse a string")
text = "Python"
reversed_text = text[::-1]
print(reversed_text)

print("\nProblem 3: Check if a number is prime")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = 31
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")

print("\nProblem 4: Find the largest of three numbers")
a, b, c = 10, 25, 15
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)


print("\nProblem 5: Count vowels in a string")
text = "Internship at Axilex"
count = 0
for ch in text:
    if ch in "aeiouAEIOU":
        count += 1
print(count)

print("\nProblem 6: Check whether key exists in an array")
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return True
    return False

key = 8
arr = [1,3,4,5,7,8,11]
if linear_search(arr, key):
    print("Key is present")
else:
    print("Key is not present")



