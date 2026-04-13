import os
def load_user():
    try:
        with open("user.txt", "r") as file:
            return True
    except FileNotFoundError:
        return None

def save_user():
    name = input("Enter your name\n")
    while True:
        try:
            age = int(input("Enter your age\n"))
            if age >= 0:
                break
            else:
                print("Please enter a valid age")
        except ValueError:
            print("Please enter a number")
    with open("user.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")

def delete_user():
    if os.path.exists("user.txt"):
        os.remove("user.txt")
        print("Data deleted")
    else:
        print("No saved data found")

def get_option_number():
    valid_options = {"0", "1", "2", "3"}
    while True:
        option = input("Choose an option:\n1 — Show user data\n2 - Update user data\n3 - Reset user data\n0 - Exit\n")
        if option in valid_options:
            return option
        else:
            print("Please enter a valid option number")

def show_user():
    try:
        with open("user.txt", "r") as file:
            data = file.read()
            print("Saved data:\n" + data)
    except FileNotFoundError:
        print("No saved data found")

if not load_user():
    save_user()
while True:
    option = get_option_number()
    if option == "0":
        break
    elif option == "1":
        show_user()
    elif option == "2":
        save_user()
    elif option == "3":
        delete_user()