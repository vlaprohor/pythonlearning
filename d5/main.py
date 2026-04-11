import requests

def get_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if not response.ok:
        print(f"Error {response.status_code}")
        return None
    else:
        return response.json()
    
def get_id_from_user(data):
    valid_ids = {item["userId"] for item in data}
    while True:
        try:
            user_id = int(input("Insert user ID\n"))
            if user_id in valid_ids:
                return user_id
            print ("Please insert an existing ID")
        except ValueError:
            print ("Please insert a valid number")

def get_option_number():
    valid_options = {"0", "1", "2", "3"}
    while True:
        option = input("Choose an option:\n1 — Show all tasks\n2 - Show completed tasks\n3 - Show stats\n0 - Exit\n")
        if option in valid_options:
            return option
        else:
            print("Please enter a valid option number")

def print_id_tasks(user_tasks):
    for i, item in enumerate(user_tasks, start=1):
        print (f"Task {i}: {item['title']}")
    
def print_id_completed_tasks(user_tasks):
    completed = 0
    for item in user_tasks:
        if item["completed"]:
            completed += 1
            print (f"Completed task {completed}: {item['title']}")

def print_id_stats(user_tasks, user_id):
    task_counter = len(user_tasks)
    completed = sum(1 for item in user_tasks if item["completed"])
    print (f"Total number of {user_id}'s tasks: {task_counter}\nTotal number of completed {user_id}'s tasks: {completed}\nTotal number of {user_id}'s tasks in work: {task_counter - completed}")

data = get_data()
if data is not None:
    user_id = get_id_from_user(data)
    user_tasks = [item for item in data if item["userId"] == user_id]
    while True:
        option = get_option_number()
        if option == "0":
            break
        elif option == "1":
            print_id_tasks(user_tasks)
        elif option == "2":
            print_id_completed_tasks(user_tasks)
        elif option == "3":
            print_id_stats(user_tasks, user_id)