def show_all_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found")
        return
    for item in contacts:
        print(f"Name: {item['name']}. Age: {item['age']}")

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