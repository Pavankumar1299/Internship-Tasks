print("Debugging Program A: The Average Calculator")
def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

my_grades = [85, 90, 78, 92]
print("The average is:", calculate_average(my_grades))

print("\nDebugging Program B: The Infinite Counter")
count = 0
while count <= 10:
    print(count)
    count += 2