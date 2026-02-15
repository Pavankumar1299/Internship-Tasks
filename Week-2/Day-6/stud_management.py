students = {}

def add_student():
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    students.update({roll: {"roll": roll, "name": name, "marks": marks}})
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    for _, s in students.items():
        print(s)

def update_student():
    roll = int(input("Enter roll number to update: "))
    if roll in students:
        students[roll]["name"] = input("Enter new name: ")
        students[roll]["marks"] = float(input("Enter new marks: "))
        print("Student updated!")
        return
    print("Student not found.")

def delete_student():
    roll = int(input("Enter roll number to delete: "))
    if roll in students:
        students.pop(roll)
        print("Student deleted!")
        return
    print("Student not found.")

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
