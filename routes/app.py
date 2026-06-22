from fastapi import FastAPI


app = FastAPI()


# Multiple Routes

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message":"About Page"}

@app.get("/users")
def users():
    return{
        'users':['Mohit',"Ramesh","Suresh"]
    }

# mdynamic routes


@app.get("/users/{id}")
def get_user(id:int):
    return{"id":id}