import os
import json

def load_contacts():
    if not os.path.exists("contacts.txt") or os.stat("contacts.txt").st_size == 0:
        with open("contacts.txt", "w") as file:
            file.write("[]")
    with open ("contacts.txt", "r") as file:
        contacts = json.load(file)
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file)