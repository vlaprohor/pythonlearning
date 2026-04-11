import requests

def get_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if not response.ok:
        print(f"Error {response.status_code}")
    else:
        return response.json()

def get_number_from_user(i):
    while True:
        try:
            n = int(input("How many tasks to show?\n"))
            if 1 <= n <= i:
                break
            else:
                print(f"Please enter a number between 1 and {i}")
        except ValueError:   
            print("Please enter a valid number")
    return n

def print_first_n_tasks(data, n):
    print(f"First {n} tasks:")
    for i in range(n):
        print(f"Task {i+1}: {data[i]['title']}")

def count_completed(data):
    print("\nCompleted tasks:")
    count = 0
    for item in data:
        if item['completed']:
            print(item['title'])
            count += 1
    print(f"\nTotal completed tasks: {count}")

data = get_data()
if data is not None:
    n = get_number_from_user(len(data))
    print_first_n_tasks(data, n)
    count_completed(data)