# 💉 Module 8 — Dependency Injection (DI)

> **Goal:** Learn how to declare, reuse, and inject dependencies into path operation functions using FastAPI's powerful `Depends` class.

---

## 🧠 What is Dependency Injection?

**Dependency Injection** is a software design pattern where a function or class receives the external resources (dependencies) it needs, rather than creating them internally.

Instead of writing repetitive logic for authentication, database sessions, or configuration inside every path operation, you define them once as functions and tell FastAPI to "inject" them.

### Why Use Dependency Injection?
1. **DRY (Don't Repeat Yourself):** Share database sessions, security tokens, or common logic across multiple routes.
2. **Loosely Coupled Code:** Makes it incredibly easy to swap dependencies.
3. **Easy Testing:** You can override dependencies with mocks during unit testing.

---

## 🔍 Concepts Covered

### 1. Basic Dependency Injection (`Depends`)

FastAPI uses `Depends()` to declare a dependency on a path operation function.

```python
from fastapi import FastAPI, Depends

app = FastAPI()

# 1. Define the dependency function
def common_logic():
    return {"message": "Common Logic"}

# 2. Inject it using Depends
@app.get('/home')
def home(data=Depends(common_logic)):
    return {
        "home": "Home Page",
        "data": data
    }
```

---

### 2. Sharing User Sessions / Auth State

A very common use case is fetching the currently logged-in user:

```python
def get_current_user():
    return {"user": "Nakul"}

@app.get('/profile')
def get_profile(user=Depends(get_current_user)):
    return {
        "profile": "Profile Page",
        "user": user
    }

@app.get('/dashboard')
def dashboard(user=Depends(get_current_user)):
    return user
```
If you ever need to change how the current user is fetched (e.g., from DB instead of hardcoded), you only modify `get_current_user()`. The routes remain untouched!

---

### 3. Route Security & Verification (Headers Validation)

Dependencies can read request elements like **headers**, cookies, or query parameters, and raise `HTTPException` if validation fails:

```python
from fastapi import Header, HTTPException

# Dependency: checks for a custom HTTP header
def verify_token(token: str = Header(None)):
    if token != 'mysecrettoken':
        raise HTTPException(status_code=401, detail="Invalid Token")
    return {"token": token}

@app.get('/secure_data')
def secure_data(user=Depends(verify_token)):
    return {"message": "secure Data", "user": user}
```

*   If the request headers contain `token: mysecrettoken` → `verify_token` returns the token, and `secure_data` runs successfully.
*   Otherwise → Returns `401 Unauthorized` automatically.

---

## 🔄 Dependency Injection vs Middleware

Both allow you to run code before your endpoint handler runs, but they serve different purposes:

| Feature | Dependency Injection (`Depends`) | Middleware |
|---|---|---|
| **Scope** | Route-specific (applied per route or router) | Global (runs for every single request) |
| **Granularity** | Highly specific (access route context, schemas, type hints) | Generic (deals with raw request/response objects) |
| **Return Types** | Returns typed Python objects directly to the handler | Returns raw HTTP Response object |
| **Best For** | DB sessions, Auth/Permissions, parsed headers | Logging, CORS headers, gzip compression, rate limiting |

---

## 🚀 Run This Module

```bash
cd dependency_injection
uvicorn app:app --reload
```

Test at `http://127.0.0.1:8000/docs`:
1.  **GET `/home`**: Observe the injected message from `common_logic`.
2.  **GET `/profile` & `/dashboard`**: Verify both share the same `get_current_user` dependency.
3.  **GET `/secure_data`**: Try executing it:
    *   Without headers → returns `401 Unauthorized`.
    *   In Swagger UI, click **Try it out**, fill the header input parameter `token` with `mysecrettoken` → returns `200 OK`.

---

## 🎯 Interview Quick-Fire

**Q: What is `Depends` in FastAPI?**
> A: It is a class/function decorator that allows you to specify a dependency for a route function, which FastAPI resolves and injects at runtime.

**Q: Can a dependency depend on other dependencies (Nested Dependencies)?**
> A: Yes! FastAPI fully supports nested dependencies. If Dependency A depends on Dependency B, FastAPI resolves B first, passes it to A, and then passes A to the endpoint.

**Q: How do you override dependencies for testing?**
> A: FastAPI allows you to override dependencies using the `app.dependency_overrides` dictionary:
> ```python
> app.dependency_overrides[get_current_user] = test_user_mock
> ```

---

[← Previous: Status Codes & Error Handling](../status_code_responses/README.md) | [Back to Main README](../README.md) | [Next: Middleware →](../middleware/README.md)
