def add_record():
    name = input("Enter name: ")
    age = input("Enter age: ")
    record = name + "," + age

    try:
        with open("./Week-2/Day-6/records.txt", "r") as f:
            records = f.read()
    except FileNotFoundError:
        records = ""

    if record in records:
        print("Data already found!")
    else:
        with open("./Week-2/Day-6/records.txt", "a") as f:
            f.write(record + "\n")
        print("Record saved!")


def view_records():
    try:
        with open("./Week-2/Day-6/records.txt", "r") as f:
            print("\nRecords:")
            print(f.read())
    except FileNotFoundError:
        print("No records found.")

while True:
    print("\n1.Add Record 2.View Records 3.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_record()
    elif choice == 2:
        view_records()
    elif choice == 3:
        break
    else:
        print("Invalid choice")
