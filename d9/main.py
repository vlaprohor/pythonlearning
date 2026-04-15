import os
import json

def check_file():
    if not os.path.exists("contacts.txt") or os.stat("contacts.txt").st_size == 0:
        with open("contacts.txt", "w") as file:
            file.write("[]")
            return
    else:
        return

def load_contacts():
    with open ("contacts.txt", "r") as file:
        contacts = json.load(file)
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file)
        
def get_option_number():
    valid_options = {"0", "1", "2", "3", "4"}
    while True:
        option = input("Choose an option:\n1 — Show all contacts\n2 - Add contact\n3 - Delete contact by name\n4 - Find contact\n0 - Exit\n")
        if option in valid_options:
            return option
        else:
            print("Please enter a valid option number")

def show_all_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found")
        return
    for item in contacts:
        print(f"Name: {item['name']}. Age: {item['age']}")

def get_user_information():
    name = input("Enter name\n")
    while True:
        try:
            age = int(input("Enter your age\n"))
            if age >= 0:
                break
            else:
                print("Please enter a valid age")
        except ValueError:
            print("Please enter a number")
    return (name, age)

def add_contact(contacts, contact):
    for item in contacts:
        if item["name"] == contact[0]:
            print("Contact with this name already exists")
            return contacts
    data = {"name": contact[0], "age": contact[1]}
    contacts.append(data)
    return contacts

def delete_contact(contacts, name):
    new_contacts = [item for item in contacts if item["name"] != name]
    if len(new_contacts) == len(contacts):
        print(f'User "{name}" is not found')
        return contacts
    print(f"User \"{name}\" successfully deleted")
    return new_contacts

def find_contact(contacts, name):
    for item in contacts:
        if item["name"] == name:
            print(f"Name: {item['name']}. Age: {item['age']}")
            return
    print(f"User \"{name}\" is not found")

check_file()
contacts = load_contacts()
while True:
    option = get_option_number()
    if option == "0":
        break
    elif option == "1":
        show_all_contacts(contacts)
    elif option == "2":
        contact = get_user_information()
        contacts = add_contact(contacts, contact)
        save_contacts(contacts)
    elif option == "3":
        name = input("Enter contact name to delete\n")
        contacts = delete_contact(contacts, name)
        save_contacts(contacts)
    elif option == "4":
        name = input("Enter contact name to find\n")
        find_contact(contacts, name)