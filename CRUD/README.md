# ✅ Module 5 — CRUD Operations (Create, Read, Update, Delete)

> **Goal:** Build a complete Todo API with all four CRUD operations — the foundation of any real-world API.

---

## 🧠 What is CRUD?

CRUD maps directly to HTTP methods:

| Operation | HTTP Method | Endpoint | What It Does |
|---|---|---|---|
| **C**reate | `POST` | `/todos` | Add a new todo |
| **R**ead | `GET` | `/todos` | Get all todos |
| **R**ead One | `GET` | `/todos/{id}` | Get a specific todo |
| **U**pdate | `PUT` | `/todos/{id}` | Modify a todo |
| **D**elete | `DELETE` | `/todos/{id}` | Remove a todo |

---

## Code Walkthrough

### Data Model

```python
class Todo(BaseModel):
    id: int
    title: str
    completed: bool
```

Storage: `todos = []` (in-memory list — resets on server restart)

---

### CREATE — `POST /todos`

```python
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "TODO added", "data": todo}
```

```bash
# Test:
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Learn FastAPI", "completed": false}'
```

---

### READ ALL — `GET /todos`

```python
@app.get("/todos")
def get_todos():
    return todos
```

---

### READ ONE — `GET /todos/{todo_id}`

```python
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}
```

> Uses **path parameter** + **loop** to find the matching todo.

---

### UPDATE — `PUT /todos/{todo_id}`

```python
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todos: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todos
            return {"message": "Todo updated", "data": updated_todos}
    return {"error": "Todo not found"}
```

> Uses `enumerate()` to get both the index and the item for replacement.

---

### DELETE — `DELETE /todos/{todo_id}`

```python
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted"}
    return {"error": "Todo not found"}
```

---

## 🚀 Run This Module

```bash
cd CRUD
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs` and test the full flow:

1. **POST** → Create a todo
2. **GET** → See it in the list
3. **PUT** → Update it
4. **GET** by ID → Verify the update
5. **DELETE** → Remove it
6. **GET** → Confirm it's gone

---

## 🔑 Key Takeaways

| Concept | What to Remember |
|---|---|
| `@app.post()` | Create data |
| `@app.get()` | Read data |
| `@app.put()` | Update data |
| `@app.delete()` | Delete data |
| `enumerate()` | Get index + item while looping |
| `list.pop(i)` | Remove item at index `i` |
| Path params | Used to identify WHICH resource to read/update/delete |

---

## 🎯 Interview Quick-Fire

**Q: What does CRUD stand for?**
> Create, Read, Update, Delete — the four basic database operations.

**Q: Which HTTP methods map to CRUD?**
> POST → Create, GET → Read, PUT → Update, DELETE → Delete.

**Q: Why use `enumerate()` instead of a regular loop?**
> Because we need the **index** to replace or remove items from the list.

**Q: What's the difference between PUT and PATCH?**
> `PUT` replaces the **entire** resource. `PATCH` updates **only** specific fields.

---

[← Previous: Pydantic Models](../pydantic_models/README.md) | [Back to Main](../README.md)
