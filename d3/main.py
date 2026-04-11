import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if response.ok:
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Completed: {data['completed']}")
else:
    print(f"Error {response.status_code}")