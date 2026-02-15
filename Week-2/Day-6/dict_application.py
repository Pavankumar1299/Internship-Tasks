dictionary = {}

def add_word():
    word = input("Enter word: ")
    meaning = input("Enter meaning: ")
    dictionary[word] = meaning
    print("Word added!")

def search_word():
    word = input("Enter word to search in dictionary: ")
    if word in dictionary:
        print("Meaning of word:", dictionary[word])
    else:
        print("Word not found.")

while True:
    print("\n*** Menu ***")
    print("1.Add Word \n2.Search Word \n3.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_word()
    elif choice == 2:
        search_word()
    elif choice == 3:
        break
    else:
        print("Invalid choice")
