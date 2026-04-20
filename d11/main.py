from fastapi import FastAPI
from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    age: int

app = FastAPI()

contacts = []

@app.get("/contacts")
def get_contacts():
    return contacts

@app.post("/contacts")
def add_contact(contact: Contact):
    contacts.append(contact.dict())
    return {"message": "Contact added"}

@app.get("/contacts/{name}")
def get_contact(name: str):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return {"message": "Contact not found"}

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    global contacts
    new_contacts = [item for item in contacts if item["name"] != name]
    if len(new_contacts) == len(contacts):
        return {"message" : f"User \"{name}\" is not found"}
    contacts = new_contacts
    return {"message" : f"User \"{name}\" successfully deleted"}