text = "Programmig is great"
frequency = {}

for c in text.lower():
    if c.isalpha():
        frequency[c] = frequency.get(c, 0) + 1

for c, count in frequency.items():
    print(c, ": ", count)