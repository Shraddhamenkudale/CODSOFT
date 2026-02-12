# Contact Book Application
# CodSoft Internship - Task 4
# Created by: (Your Name)

contacts = []   # This list will store all contact details


def show_menu():
    print("\n====== CONTACT BOOK MENU ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    print("\nYour Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")


def search_contact():
    search_name = input("Enter name to search: ")

    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("Contact Found:")
            print(contact["name"], "|", contact["phone"], "|", contact["email"])
            found = True
            break

    if not found:
        print("Contact not found.")


def update_contact():
    view_contacts()
    if len(contacts) == 0:
        return

    try:
        number = int(input("Enter contact number to update: "))
        if 1 <= number <= len(contacts):
            contacts[number - 1]["name"] = input("Enter new name: ")
            contacts[number - 1]["phone"] = input("Enter new phone: ")
            contacts[number - 1]["email"] = input("Enter new email: ")
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_contact():
    view_contacts()
    if len(contacts) == 0:
        return

    try:
        number = int(input("Enter contact number to delete: "))
        if 1 <= number <= len(contacts):
            removed = contacts.pop(number - 1)
            print(f"Contact '{removed['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")


# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please select between 1 and 6.")
