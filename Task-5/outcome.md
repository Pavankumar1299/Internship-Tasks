# Internship Python Tasks – Day 5

## Task 1: Arithmetic Operations using Functions
### Problem 1: Check if a number is even or odd
**Expected Outcome:**
The program should identify whether the number is even or odd.

**Actual Outcome:**
O**utput was “Odd”, which is correct for the given input.

### Problem 2: Find the largest of three numbers
**Expected Outcome:**
The program should print the largest number among the three.

**Actual Outcome:**
O**utput was 25, which is the correct largest value.

### Problem 3: Reverse a string
**Expected Outcome:**
The string should be reversed.

**Actual Outcome:**
O**utput was “nohtyP”, which matches the expected result.

### Problem 4: Count vowels in a string
**Expected Outcome:**
The program should count the number of vowels in the string.

**Actual Outcome:**
O**utput was 5, which is correct.

### Problem 5: Check if a number is prime
**Expected Outcome:**
The program should check whether the number is prime.

**Actual Outcome:**
O**utput was “Prime”, which is correct.

### Problem 6: Check if a number is prime
**Expected Outcome:**
The program should check whether the number is prime.

**Actual Outcome:**
O**utput was “Prime”, which is correct.

## Task 2: Debugging & Program Correction
### Debugging Program A: The Average Calculator

Given Program:
```
def calculate_average(grades):
    total = 0
    for grade in grades:
        total =+ grade
    return total / len(grade)

my_grades = [85, 90, 78, 92]
print("The average is: " + calculate_average(my_grades))
```

Issue Identified:
The program does not correctly add all the grades, and it also tries to calculate the average using a value that does not represent the full list. This causes incorrect results or runtime errors.

Corrected Program:
```
def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

my_grades = [85, 90, 78, 92]
print("The average is:", calculate_average(my_grades))
```

**Expected Outcome:**
The program should calculate and display the correct average of all grades in the list.

**Actual Outcome:**
The program successfully displayed 86.25, which is the correct average.

### Debugging Program B: The Infinite Counter

Given Program:
```
count = 0
while count != 10:
    print(count)
    count += 2
```

Issue Identified:
The loop condition does not guarantee that the loop will stop at the desired point. This makes the loop run endlessly instead of stopping at the required limit.

Corrected Program:
```
count = 0
while count <= 10:
    print(count)
    count += 2
```

**Expected Outcome:**
The program should print all even numbers up to 10 and then stop.

**Actual Outcome:**
The program printed 0, 2, 4, 6, 8, 10 and terminated correctly.

# Outcome
Practicing logical ### problems and debugging helped improve my understanding of Python syntax, conditional logic, and loops.
