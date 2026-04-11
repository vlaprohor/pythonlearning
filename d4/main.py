import requests

def get_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if not response.ok:
        print(f"Error {response.status_code}")
        return None
    else:
        return response.json()
    
def get_id_from_user(data):
    while True:
        try:
            userID = int(input("Isert user ID\n"))
            for item in data:
                if item["userId"] == userID:
                    return userID
            print ("Please insert an existing ID")
        except ValueError:
            print ("Please insert a valid number")

def print_id_tasks(data, userID):
    taskCounter = 0
    completed = 0
    for item in data:
        if item["userId"] == userID:
            taskCounter += 1
            print (f"Task {taskCounter}: {item['title']}")
            if item["completed"]:
                completed += 1
    print (f"Total number of {userID}'s tasks: {taskCounter}\nTotal number of completed {userID}'s tasks: {completed}")

data = get_data()
if data is not None:
    userID = get_id_from_user(data)
    print_id_tasks(data, userID)