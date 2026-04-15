import storage
import logic
import ui

contacts = storage.load_contacts()
while True:
    option = ui.get_option_number()
    if option == "0":
        break
    elif option == "1":
        logic.show_all_contacts(contacts)
    elif option == "2":
        contact = ui.get_user_information()
        contacts = logic.add_contact(contacts, contact)
        storage.save_contacts(contacts)
    elif option == "3":
        name = input("Enter contact name to delete\n")
        contacts = logic.delete_contact(contacts, name)
        storage.save_contacts(contacts)
    elif option == "4":
        name = input("Enter contact name to find\n")
        logic.find_contact(contacts, name)