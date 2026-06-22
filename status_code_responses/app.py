from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel

app = FastAPI()

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
    if id==5:
        return {"message":"User Found"}
    else:
        raise HTTPException(status_code=404,detail="User Not Found")