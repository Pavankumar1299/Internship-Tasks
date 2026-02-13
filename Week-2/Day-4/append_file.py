file = open("./Week-2/Day-4/demo.txt", "a")
data = "\nI have appended something in 'demo.txt' file,\nAnd i don't know what it is?"
data = file.write(data)
file.close()

print("Data appended successfully.")

file = open("./Week-2/Day-4/demo.txt", "r")
data = file.read()
file.close()

print("The content of file:\n")
print(data)