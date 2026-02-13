class Student:
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept

    def details(self):
        return f"ID: {self.id}, Name: {self.name}, Dept: {self.dept}\n"


data1 = Student("S001", "Pavan", "MCA")
data2 = Student("S002", "Kiran", "MBA")

file =  open("./Week-2/Day-4/Students.txt", "a")
file.write(data1.details())
file.write(data2.details())
file.close()

print("Student records saved.\n")

file = open("./Week-2/Day-4/Students.txt", "r")
data = file.read()
file.close()

print("The content of file:\n")
print(data)
