sentence = "She sells sea shells by the sea shore, " \
            "by the way what she sells"

frequency = {}
words = sentence.split(' ')
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Frequencny of each word:")
print(frequency)