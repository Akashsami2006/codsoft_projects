import json
import os
from prettytable import PrettyTable

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """Save contacts to JSON file"""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def display_menu():
    """Display the main menu"""
    print("\nContact Management System")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    """Add a new contact"""
    print("\nAdd New Contact")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts = load_contacts()
    
    # Check if contact already exists
    for contact in contacts:
        if contact['phone'] == phone:
            print("\nContact with this phone number already exists!")
            return
    
    new_contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    contacts.append(new_contact)
    save_contacts(contacts)
    print("\nContact added successfully!")

def view_contacts():
    """View all contacts in a formatted table"""
    contacts = load_contacts()
    
    if not contacts:
        print("\nNo contacts found!")
        return
    
    table = PrettyTable()
    table.field_names = ["Name", "Phone", "Email", "Address"]
    table.align = "l"
    
    for contact in contacts:
        table.add_row([
            contact['name'],
            contact['phone'],
            contact['email'],
            contact['address']
        ])
    
    print("\nAll Contacts:")
    print(table)

def search_contact():
    """Search contacts by name or phone"""
    search_term = input("\nEnter name or phone number to search: ").strip().lower()
    contacts = load_contacts()
    results = []
    
    for contact in contacts:
        if (search_term in contact['name'].lower() or 
            search_term in contact['phone']):
            results.append(contact)
    
    if not results:
        print("\nNo matching contacts found!")
        return
    
    table = PrettyTable()
    table.field_names = ["Name", "Phone", "Email", "Address"]
    table.align = "l"
    
    for contact in results:
        table.add_row([
            contact['name'],
            contact['phone'],
            contact['email'],
            contact['address']
        ])
    
    print("\nSearch Results:")
    print(table)

def update_contact():
    """Update existing contact details"""
    phone = input("\nEnter phone number of contact to update: ").strip()
    contacts = load_contacts()
    found = False
    
    for contact in contacts:
        if contact['phone'] == phone:
            found = True
            print("\nCurrent Contact Details:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            
            print("\nEnter new details (leave blank to keep current value):")
            name = input(f"Name [{contact['name']}]: ").strip() or contact['name']
            new_phone = input(f"Phone [{contact['phone']}]: ").strip() or contact['phone']
            email = input(f"Email [{contact['email']}]: ").strip() or contact['email']
            address = input(f"Address [{contact['address']}]: ").strip() or contact['address']
            
            # Check if new phone number already exists (if changed)
            if new_phone != phone:
                for c in contacts:
                    if c['phone'] == new_phone and c != contact:
                        print("\nContact with this phone number already exists!")
                        return
            
            contact.update({
                'name': name,
                'phone': new_phone,
                'email': email,
                'address': address
            })
            
            save_contacts(contacts)
            print("\nContact updated successfully!")
            break
    
    if not found:
        print("\nContact not found!")

def delete_contact():
    """Delete a contact"""
    phone = input("\nEnter phone number of contact to delete: ").strip()
    contacts = load_contacts()
    
    for i, contact in enumerate(contacts):
        if contact['phone'] == phone:
            print("\nContact to be deleted:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            
            confirm = input("\nAre you sure you want to delete this contact? (y/n): ").lower()
            if confirm == 'y':
                del contacts[i]
                save_contacts(contacts)
                print("\nContact deleted successfully!")
            return
    
    print("\nContact not found!")

def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nExiting Contact Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()