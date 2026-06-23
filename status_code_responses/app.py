'''
Custom Exception is userdefined exception which is used in specific buisness logic error   
HTTPException is built in FastApi ,to handle custom exception 
Global Exception Handler is used to handle the exception in the entire application it can also raise the HTTPException.
---> benifits of Global Exception Handler 
    1. DRY (Don't Repeat Yourself)
    2. Consistent Error Handling
    3. Centralized Error Management
    4. Better User Experience
    5. Scalabel API design
'''


from pydantic_models.app import User
from fastapi import FastAPI,status,HTTPException,Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


# Global erorr Handler 

class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request:Request,exc:UserNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"status":"error","message":f"User {exc.name} Not Found"}
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name!="Mohit":
        raise UserNotFoundException(name)
    return{"name":name}

# Custom status code

@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return{
        "message":"User Created",
        "status":status.HTTP_201_CREATED
    }
    
# Custom Response   

@app.get("/user")
def get_user():
    return{
        "status":"Success",
        "message":"User Found",
        "data":{
            "name":"Mohit",
            "age":22,
            "email":"[EMAIL_ADDRESS]"
        }
    }

# Error Handling 

@app.get("/user/{id}")
def get_user(id:int):
    if id!=1:
        raise HTTPException(status_code=404,detail="User Not Found")
        
    return{
        "id":1,
        "name":"Mohit",
        "age":22,
        "email":"[EMAIL_ADDRESS]"
    }

    # Custom excpetion Error Handling


