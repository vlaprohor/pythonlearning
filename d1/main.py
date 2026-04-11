name = input("What's your name?\n")
print(f"Hello, {name}!")
while True:
    try:
        age = int(input("How old are you?\n"))
        break
    except ValueError:
        print("Looks like you entered NOT a number. Please, enter number")
print(f"Cool! You will be {age + 1} in one year!")