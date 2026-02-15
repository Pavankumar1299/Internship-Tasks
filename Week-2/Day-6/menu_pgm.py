total = 0

while True:
    print("\n*** MENU ***")
    print("1. Idly        - ₹30")
    print("2. Dosa        - ₹40")
    print("3. Uttappa     - ₹50")
    print("4. Puri-Baji   - ₹60")
    print("5. Pay Bill & Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Here is your Idly, Sir")
        total += 30

    elif choice == 2:
        print("Here is your Dosa, Sir")
        total += 40

    elif choice == 3:
        print("Here is your Uttappa, Sir")
        total += 50

    elif choice == 4:
        print("Here is your Puri-Baji, Sir")
        total += 60

    elif choice == 5:
        if total != 0:
            print("\nPlease pay your bill")
            print("Total Amount: ₹", total)
            print("Thank you! Visit again")
            break
        else:
            print("You have to order something, Sir")

    else:
        print("Invalid choice, please try again!")
5