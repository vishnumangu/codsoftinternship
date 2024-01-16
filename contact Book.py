import json

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print(f'Contact "{name}" added successfully.')

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact['name']} - {contact['phone_number']}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if
                          search_term.lower() in contact['name'].lower() or
                          search_term in contact['phone_number']]
        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("\nMatching Contacts:")
            for i, contact in enumerate(found_contacts, 1):
                print(f"{i}. {contact['name']} - {contact['phone_number']}")

    def update_contact(self, index, name, phone_number, email, address):
        if 1 <= index <= len(self.contacts):
            self.contacts[index - 1] = {
                'name': name,
                'phone_number': phone_number,
                'email': email,
                'address': address
            }
            print(f'Contact {index} updated successfully.')
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            removed_contact = self.contacts.pop(index - 1)
            print(f'Contact {index} deleted successfully: {removed_contact["name"]}')
        else:
            print("Invalid contact index.")

    def save_to_file(self, filename='contacts.json'):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file, indent=2)
        print(f'Contacts saved to {filename}.')

    def load_from_file(self, filename='contacts.json'):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
            print(f'Contacts loaded from {filename}.')
        except FileNotFoundError:
            print(f'File {filename} not found. Starting with an empty contact list.')


def main():
    contact_manager = ContactManager()
    contact_manager.load_from_file()

    while True:
        print("\nContact Management System:")
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact")
        print("5. Delete Contact\n6. Save Contacts to File\n7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter the name or phone number to search: ")
            contact_manager.search_contact(search_term)

        elif choice == '4':
            index = int(input("Enter the contact index to update: "))
            name = input("Enter the new name: ")
            phone_number = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            address = input("Enter the new address: ")
            contact_manager.update_contact(index, name, phone_number, email, address)

        elif choice == '5':
            index = int(input("Enter the contact index to delete: "))
            contact_manager.delete_contact(index)

        elif choice == '6':
            contact_manager.save_to_file()

        elif choice == '7':
            contact_manager.save_to_file()
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
