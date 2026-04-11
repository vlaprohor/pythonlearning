numbers = []
for i in range(5):
    while True:
        try:
            k=int(input(f"Insert number #{i+1}\n"))
            break
        except ValueError:
            print("Please enter a valid number")
    numbers.append(k)
print(numbers)
print(sum(numbers))
print(sum(numbers)/len(numbers))