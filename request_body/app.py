from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int


# real world scenario and data validation using pydantic

@app.post("/user")
def user(user:User):
    return{"message":"User created","data":user}

'''
--> Difference between Dict and Pydantic 
-   dict has no validation while pydantic has auto validation
-   dict is flexible and pydantic is structured
-   error handling is manual in dict and pydanitc has auto error handling

'''