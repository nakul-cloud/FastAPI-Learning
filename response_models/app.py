from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Hiding necessary things and showing only what is needed to frontend

class User(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel):
    name:str
    age:int

@app.post("/user",response_model=UserResponse)
def get_user(user:User):
      return{
        "name":"Mohit",
        "age":22,
        "password":"12345"
      }
    

'''
Request models means where we defined input data --from client we send data
Response models means where we defined output data --to client we send data

'''