from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

# Create

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return{"message":"TODO added",'data':todo}

# Read

@app.get("/todos")
def get_todos():
     return todos

# Reading single data using path params

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    return{"error":"Todo not found"}

# Update 

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todos:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todos
            return{
                "message":"Todo updated",
                "data":updated_todos
            } 
    return {"error":"Todo not found"}


# Delete

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(index)
            return {"message":"Todo deleted"}
    return {"error":"Todo not found"}  