
string = input("Enter a string: ")
vowels = "aeiou"

vowels_cnt = 0
consonants_cnt = 0
for c in string.lower():
    if c.isalpha():
        if c in vowels:
            vowels_cnt += 1
        else:
            consonants_cnt += 1

# print("String: ", string)
print("\nVowels: ", vowels_cnt)
print("Consonants: ", consonants_cnt)