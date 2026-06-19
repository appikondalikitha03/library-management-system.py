import random

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Show Random Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == "2":
        if contacts:
            print("\nContact List:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")
        else:
            print("No contacts available.")

    elif choice == "3":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print(f"Phone Number: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        if contacts:
            random_name = random.choice(list(contacts.keys()))
            print("\nRandom Contact:")
            print(f"Name: {random_name}")
            print(f"Phone: {contacts[random_name]}")
        else:
            print("No contacts available.")

    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice! Try Again.")