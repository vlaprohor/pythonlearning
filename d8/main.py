import os
import json

def check_file():
    if not os.path.exists("contacts.txt") or os.stat("contacts.txt").st_size == 0:
        with open("contacts.txt", "w") as file:
            file.write("[]")
            return
    else:
        return
        
def get_option_number():
    valid_options = {"0", "1", "2", "3"}
    while True:
        option = input("Choose an option:\n1 — Show all contacts\n2 - Add contact\n3 - Delete contact by name\n0 - Exit\n")
        if option in valid_options:
            return option
        else:
            print("Please enter a valid option number")

def show_all_contacts():
    if os.stat("contacts.txt").st_size == 0:
        print("No contacts found")
        return
    with open ("contacts.txt", "r") as file:
        contacts = json.load(file)
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

def add_contact(contact):
    name = contact[0]
    age = contact[1]
    data = {"name": name, "age": age}
    with open("contacts.txt", "r") as file:
        contacts = json.load(file)
    contacts.append(data)
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file)

def delete_contact():
    name = input("Enter contact name to delete\n")
    with open ("contacts.txt", "r") as file:
        contacts = json.load(file)
    new_contacts = [item for item in contacts if item["name"] != name]
    if len(new_contacts) == len(contacts):
        print(f'User "{name}" is not found')
        return
    with open("contacts.txt", "w") as file:
        json.dump(new_contacts, file)
    print(f"User \"{name}\" successfully deleted")

check_file()
while True:
    option = get_option_number()
    if option == "0":
        break
    elif option == "1":
        show_all_contacts()
    elif option == "2":
        add_contact(get_user_information())
    elif option == "3":
        delete_contact()