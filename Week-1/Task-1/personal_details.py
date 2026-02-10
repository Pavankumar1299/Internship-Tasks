class Personal_Details():
    def __init__(self, name, age, institute, branch, sem):
        self.name = name
        self.age = age
        self.institute = institute
        self.branch = branch
        self.sem = sem

    def display_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Institute: ", self.institute)
        print("Branch: ", self.branch)
        print("Sem: ", self.sem)

obj1 = Personal_Details("Pavankumar", 27, "KLS Gogte Institute of Technology", "MCA", 4)
# obj2 = Personal_Details("Sudeep", 24, "KLS Gogte Institute of Technology", "MCA", 3)

obj1.display_details()
# obj2.display_details()