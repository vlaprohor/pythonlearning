def get_option_number():
    valid_options = {"0", "1", "2", "3", "4"}
    while True:
        option = input("Choose an option:\n1 — Show all contacts\n2 - Add contact\n3 - Delete contact by name\n4 - Find contact\n0 - Exit\n")
        if option in valid_options:
            return option
        else:
            print("Please enter a valid option number")

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
