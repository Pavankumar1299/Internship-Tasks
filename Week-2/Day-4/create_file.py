file = open("./Week-2/Day-4/demo.txt", "a")

file.write("I have created a new file \n" \
"using Python File Handling operations")

file.close()
print("File created and data written.")

file = open("./Week-2/Day-4/demo.txt", "r")
data = file.read()
file.close()

print("The content of file:\n")
print(data)