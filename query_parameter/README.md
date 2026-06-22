# 🔍 Module 2 — Query Parameters

> **Goal:** Learn how to accept optional filters, search terms, and pagination via URL query strings.

---

## 🧠 Concepts Covered

### What is a Query Parameter?

A query parameter is data passed in the URL **after the `?`** sign. They're used for **filtering, searching, and pagination** — not for identifying resources.

```
http://127.0.0.1:8000/users?name=Nakul
                             ↑
                      query parameter
```

> 💡 **Rule of thumb:** If the parameter is NOT in the path `{}` and NOT a Pydantic model, FastAPI treats it as a **query parameter**.

---

### 1. Single / Optional Query Parameter

```python
@app.get("/users")
def get_users(name: str = None):
    return {"Name": name}
```

| Request | `name` value | Response |
|---|---|---|
| `/users?name=Nakul` | `"Nakul"` | `{"Name": "Nakul"}` |
| `/users` | `None` | `{"Name": null}` |

> Setting `= None` makes the parameter **optional**. Without a default, it becomes **required**.

---

### 2. Default Value Parameter

```python
@app.get("/product")
def get_product(limit: int = 10):
    return {"limit": limit}
```

| Request | `limit` value | Response |
|---|---|---|
| `/product?limit=5` | `5` | `{"limit": 5}` |
| `/product` | `10` (default) | `{"limit": 10}` |

> 💡 **Use case:** Pagination! Default to 10 items per page, but let the client override it.

---

### 3. Multiple Query Parameters

Combine multiple query params with `&`:

```python
@app.get("/items")
def get_items(name: str = None, price: int = 0):
    return {"name": name, "price": price}
```

| Request | Response |
|---|---|
| `/items?name=Pen&price=20` | `{"name": "Pen", "price": 20}` |
| `/items?name=Pen` | `{"name": "Pen", "price": 0}` |
| `/items` | `{"name": null, "price": 0}` |

---

## 🔄 Path Params vs Query Params — Side by Side

```
/users/5          → Path Parameter   → identifies WHICH user
/users?name=Nakul → Query Parameter  → filters/searches users
```

| Feature | Path Parameter | Query Parameter |
|---|---|---|
| Location | In the URL path | After `?` in URL |
| Syntax | `"/users/{id}"` | `def fn(name: str)` |
| Purpose | Identify a specific resource | Filter / sort / paginate |
| Required? | Always required | Can be optional |
| Example | `/users/42` | `/users?name=Nakul` |

---

## 🚀 Run This Module

```bash
cd query_parameter
uvicorn app:app --reload
```

Then test:
- `http://127.0.0.1:8000/users?name=Nakul`
- `http://127.0.0.1:8000/product` (uses default limit=10)
- `http://127.0.0.1:8000/product?limit=3`
- `http://127.0.0.1:8000/items?name=Book&price=100`
- `http://127.0.0.1:8000/docs` → Test interactively

---

## 🔑 Key Takeaways

| Pattern | Code | Behavior |
|---|---|---|
| Required query param | `name: str` | ❌ Error if missing |
| Optional query param | `name: str = None` | ✅ Defaults to `None` |
| Default value | `limit: int = 10` | ✅ Uses `10` if not sent |
| Multiple params | `name: str, price: int` | Use `&` to combine |

---

## 🎯 Interview Quick-Fire

**Q: How does FastAPI know if a parameter is a path param or query param?**
> A: If the parameter name appears in the route path (`/users/{id}`), it's a path param. Otherwise, it's a query param.

**Q: How do you make a query parameter optional?**
> A: Give it a default value: `name: str = None`.

**Q: Can you mix path params and query params?**
> A: Yes! Example: `@app.get("/users/{id}")` with `def get_user(id: int, details: bool = False)` — `id` is a path param, `details` is a query param.

---

[← Previous: Routes](../routes/README.md) | [Back to Main README](../README.md) | [Next: Request Body →](../request_body/README.md)
