def save_user(name, age):
    with open("user.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")

def load_user():
    try:
        with open("user.txt", "r") as file:
            data = file.read()
            print("Saved data:\n" + data)
    except FileNotFoundError:
        print("No saved data found")

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

save_user(name, age)
load_user()