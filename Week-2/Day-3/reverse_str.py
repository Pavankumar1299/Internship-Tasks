string = "Programming is great"

chars = list(string)
rev_str = ''.join(c for c in chars[::-1])

print("String: ", string)
print("Reversed str: ", rev_str)