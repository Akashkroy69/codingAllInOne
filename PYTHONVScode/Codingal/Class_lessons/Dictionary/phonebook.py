# Create an empty phonebook dictionary
phonebook = {}

# Function to add a contact to the phonebook
def add_contact(phonebook, name, number):
    phonebook[name] = number  # Add the name as the key and the number as the value
    print(f"Added {name} to the phonebook.")

# Function to retrieve a contact's number
def get_contact(phonebook, name):
    if name in phonebook:  # Check if the name exists as a key in the phonebook
        print(f"{name}'s phone number: {phonebook[name]}")
    else:
        print(f"{name} not found in the phonebook.")

# Function to remove a contact from the phonebook
def remove_contact(phonebook, name):
    if name in phonebook:  # Check if the name exists as a key in the phonebook
        del phonebook[name]  # Delete the key-value pair associated with the name
        print(f"Removed {name} from the phonebook.")
    else:
        print(f"{name} not found in the phonebook.")

# Function to list all contacts in the phonebook
def list_contacts(phonebook):
    print("Phonebook Contacts:")
    for name, number in phonebook.items():  # Iterate through the key-value pairs in the phonebook
        print(f"{name}: {number}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Get Contact Number")
    print("3. Remove Contact")
    print("4. List All Contacts")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        add_contact(phonebook, name, number)
    elif choice == '2':
        name = input("Enter contact name to get number: ")
        get_contact(phonebook, name)
    elif choice == '3':
        name = input("Enter contact name to remove: ")
        remove_contact(phonebook, name)
    elif choice == '4':
        list_contacts(phonebook)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
