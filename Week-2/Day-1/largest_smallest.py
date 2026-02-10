# numbers = [21,78,3,10,99,11,34]
numbers = [12,23,74,40,89,11,24]
smallest = numbers[0]
largest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i

print("Smallest: ", smallest)
print("Largest: ", largest)