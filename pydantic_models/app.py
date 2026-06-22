'''
-->The Pydantic library in Python is used for data validation and data parsing using Python type hints. 
-->It ensures that data structures like classes, dictionaries or API inputs contain valid and correctly typed data before being processed. 
-->Pydantic automatically converts and validates incoming data, helping developers write cleaner, more reliable code.

'''


from re import A
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str

@app.post("/create_user")
def create_user(user:User):
    return{
        "message":"User Created",
        "data":user
    }

# nested models
'''
-->Nested models allow Pydantic to handle hierarchical or complex data structures cleanly.     
-->It helps in organizing data in a logical and readable way.

'''

class Address(BaseModel):
    city:str
    pincode:int

class Person(BaseModel):
    name:str
    age:int
    address:Address


@app.post("/create_person")
def create_person(person:Person):
    return Person