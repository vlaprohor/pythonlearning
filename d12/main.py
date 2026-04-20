from fastapi import FastAPI
from fastapi import HTTPException
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
    for item in contacts:
        if item["name"] == contact.name:
            raise HTTPException(status_code=400, detail="Contact already exists")
    contacts.append(contact.dict())
    return contact

@app.get("/contacts/{name}")
def get_contact(name: str):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    raise HTTPException(status_code=404, detail="Contact not found")

@app.put("/contacts/{name}")
def update_contact(name: str, age: int):
    for contact in contacts:
        if contact["name"] == name:
            contact["age"] = age
            return contact
    raise HTTPException(status_code=404, detail="Contact not found")

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    global contacts
    new_contacts = [item for item in contacts if item["name"] != name]
    if len(new_contacts) == len(contacts):
        raise HTTPException(status_code=404, detail="Contact not found")
    contacts = new_contacts
    return {"message" : f"User \"{name}\" successfully deleted"}