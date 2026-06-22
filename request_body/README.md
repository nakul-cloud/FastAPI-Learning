# 📦 Module 3 — Request Body & Data Validation

> **Goal:** Learn how to receive JSON data from clients using POST requests with Pydantic validation.

---

## 🧠 Concepts Covered

### What is a Request Body?

When a client sends data **TO** your API, that data travels in the **request body** — usually as JSON.

```
Client sends → POST /user
Body: { "name": "Nakul", "age": 22 }
```

> 💡 **GET** requests have no body. **POST/PUT/DELETE** carry data in the body.

---

### Defining a Request Body with Pydantic

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def user(user: User):
    return {"message": "User created", "data": user}
```

**Flow:** Client sends JSON → Pydantic validates → Creates User object → Your code runs.

Bad data like `{ "age": "not-a-number" }` → auto **422 error**. No try-except needed!

---

### Dict vs Pydantic

| Feature | `dict` | Pydantic `BaseModel` |
|---|---|---|
| Validation | ❌ Manual | ✅ Automatic |
| Type safety | ❌ None | ✅ Enforced |
| Error handling | ❌ You code it | ✅ Auto 422 errors |
| Swagger docs | ❌ Not visible | ✅ Auto-shown |

---

## 🚀 Run This Module

```bash
cd request_body
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs` → Try `POST /user` with `{"name": "Nakul", "age": 22}`

---

## 🎯 Interview Quick-Fire

**Q: Why Pydantic over dicts?** → Auto validation, type enforcement, auto error handling.

**Q: What HTTP methods have a body?** → `POST`, `PUT`, `PATCH`.

**Q: What error code for invalid body?** → **422 Unprocessable Entity**.

---

[← Previous: Query Parameters](../query_parameter/README.md) | [Back to Main](../README.md) | [Next: Pydantic Models →](../pydantic_models/README.md)
