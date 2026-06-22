# 🧱 Module 4 — Pydantic Models & Nested Models

> **Goal:** Deep-dive into Pydantic — the validation engine behind FastAPI.

---

## 🧠 What is Pydantic?

Pydantic is a Python library for **data validation using type hints**. It ensures your data is clean, typed, and structured **before** your code processes it.

- ✅ Auto-converts incoming data to correct types
- ✅ Auto-validates fields
- ✅ Auto-generates clear error messages

---

## Concepts Covered

### 1. Basic Pydantic Model

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/create_user")
def create_user(user: User):
    return {"message": "User Created", "data": user}
```

**Valid request:**
```json
{ "name": "Nakul", "age": 22, "email": "nakul@example.com" }
```

**Invalid request (missing field):**
```json
{ "name": "Nakul" }
```
→ Returns **422** with: `"age" field required`, `"email" field required`

---

### 2. Nested Models

Real-world data is hierarchical. Pydantic handles this with **model nesting**:

```python
class Address(BaseModel):
    city: str
    pincode: int

class Person(BaseModel):
    name: str
    age: int
    address: Address       # ← Nested model!
```

**Request body for nested model:**
```json
{
  "name": "Nakul",
  "age": 22,
  "address": {
    "city": "Mumbai",
    "pincode": 400001
  }
}
```

> 💡 FastAPI validates the **inner model too** — if `pincode` isn't an int, you get a clear error.

---

### Visual: Flat vs Nested

```
❌ Flat (messy for complex data):
{ "name": "Nakul", "age": 22, "city": "Mumbai", "pincode": 400001 }

✅ Nested (clean & organized):
{
  "name": "Nakul",
  "age": 22,
  "address": {
    "city": "Mumbai",
    "pincode": 400001
  }
}
```

---

## 🚀 Run This Module

```bash
cd pydantic_models
uvicorn app:app --reload
```

Test at `http://127.0.0.1:8000/docs`:
- `POST /create_user` → Basic model
- `POST /create_person` → Nested model

---

## 🔑 Key Takeaways

| Concept | What to Remember |
|---|---|
| `BaseModel` | Inherit from it to create a validated data schema |
| Type hints | `name: str` → auto-validated |
| Nested models | Use one model as a field type inside another |
| Validation | Happens automatically on every request |
| Error messages | Auto-generated, clear, and developer-friendly |

---

## 🎯 Interview Quick-Fire

**Q: What is Pydantic?**
> A data validation library using Python type hints. FastAPI uses it to validate request bodies.

**Q: What are nested models?**
> When a Pydantic model contains another model as a field — e.g., `Person` has an `Address`.

**Q: Does Pydantic validate nested models too?**
> Yes! Every level of nesting is fully validated.

---

[← Previous: Request Body](../request_body/README.md) | [Back to Main](../README.md) | [Next: CRUD →](../CRUD/README.md)
