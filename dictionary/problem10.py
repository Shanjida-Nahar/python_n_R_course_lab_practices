phone_book = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phone_book:
            print(name, ":", phone_book[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        for name, number in phone_book.items():
            print(name, ":", number)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")