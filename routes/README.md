# 📍 Module 1 — Routes & Path Parameters

> **Goal:** Learn how to create API endpoints and handle dynamic URLs.

---

## 🧠 Concepts Covered

### 1. What is a Route?

A **route** (or endpoint) is a URL path that your API responds to. Each route is tied to a **function** that runs when the URL is hit.

```python
@app.get("/")        # Route = "/"
def home():          # Handler function
    return {"message": "Hello World"}
```

> 💡 The `@app.get("/")` decorator tells FastAPI: "When someone visits `/`, run this function."

---

### 2. Multiple Routes

You can define as many routes as you want. Each handles a different URL:

```python
@app.get("/")           # → http://127.0.0.1:8000/
def home():
    return {"message": "Hello World"}

@app.get("/about")      # → http://127.0.0.1:8000/about
def about():
    return {"message": "About Page"}

@app.get("/users")      # → http://127.0.0.1:8000/users
def users():
    return {"users": ["Mohit", "Ramesh", "Suresh"]}
```

---

### 3. Dynamic Routes (Path Parameters)

Instead of creating a separate route for every user, you use **`{curly braces}`** to capture dynamic values from the URL:

```python
@app.get("/users/{id}")
def get_user(id: int):      # ← FastAPI auto-converts "id" to int
    return {"id": id}
```

**How it works:**

| Request URL | `id` value | Response |
|---|---|---|
| `/users/1` | `1` | `{"id": 1}` |
| `/users/42` | `42` | `{"id": 42}` |
| `/users/abc` | ❌ Error | Auto validation error (not an int) |

> 💡 **Type hint `id: int`** does TWO things:
> 1. **Validates** — Rejects non-integer values automatically
> 2. **Converts** — Turns the string from URL into a Python `int`

---

## 🚀 Run This Module

```bash
cd routes
uvicorn app:app --reload
```

Then test:
- `http://127.0.0.1:8000/` → Home
- `http://127.0.0.1:8000/about` → About
- `http://127.0.0.1:8000/users` → All users
- `http://127.0.0.1:8000/users/101` → Dynamic user
- `http://127.0.0.1:8000/docs` → Swagger UI

---

## 🔑 Key Takeaways

| Concept | Syntax | Example |
|---|---|---|
| Static route | `@app.get("/path")` | `@app.get("/about")` |
| Dynamic route | `@app.get("/path/{param}")` | `@app.get("/users/{id}")` |
| Type validation | `param: type` | `id: int` |
| HTTP method | `.get()`, `.post()`, `.put()`, `.delete()` | `@app.get(...)` |

---

## 🎯 Interview Quick-Fire

**Q: What is a path parameter?**
> A: A variable part of the URL (e.g., `/users/{id}`) that FastAPI extracts and passes to your function.

**Q: What happens if I send `/users/abc` when the param is typed as `int`?**
> A: FastAPI automatically returns a **422 Unprocessable Entity** error with a clear validation message. You don't need to write any validation code!

**Q: What's the difference between a path parameter and a query parameter?**
> A: Path params are part of the URL path (`/users/5`). Query params come after `?` (`/users?id=5`). See Module 2 for details.

---

[← Back to Main README](../README.md) | [Next: Query Parameters →](../query_parameter/README.md)
