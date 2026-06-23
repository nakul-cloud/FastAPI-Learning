# 🚦 Module 7 — HTTP Status Codes & Error Handling

> **Goal:** Learn how to use standard HTTP status codes, raise default HTTP Exceptions, and build Global Custom Exception Handlers to return clean, consistent error responses.

---

## 🧠 Concepts Covered

### 1. HTTP Status Codes Overview

HTTP status codes inform clients about the result of their API requests.

| Range | Type | Meaning | Examples |
|---|---|---|---|
| **`2xx`** | **Success** | The request was completed successfully | `200 OK`, `201 Created` |
| **`3xx`** | **Redirection** | Further action is needed | `301 Moved Permanently` |
| **`4xx`** | **Client Error** | The client made a mistake in their request | `400 Bad Request`, `404 Not Found` |
| **`5xx`** | **Server Error** | The server encountered a bug | `500 Internal Server Error` |

---

### 2. Custom Success Status Codes

FastAPI defaults to returning `200 OK` for successful requests. For actions that create data (like registration or uploads), you should explicitly set the status code to `201 Created`:

```python
from fastapi import status

@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User Created",
        "status": status.HTTP_201_CREATED
    }
```

---

### 3. Built-in Error Handling (`HTTPException`)

For standard error scenarios (like missing records), you can raise FastAPI's built-in `HTTPException`. This immediately interrupts the execution of the request and sends the specified status code and error details back to the client:

```python
from fastapi import HTTPException

@app.get("/user/{id}")
def get_user(id: int):
    if id != 1:
        raise HTTPException(status_code=404, detail="User Not Found")
    return {
        "id": 1,
        "name": "Mohit",
        "age": 22,
        "email": "mohit@example.com"
    }
```

---

### 4. Global Custom Exception Handlers (Advanced)

If you have specific business logic rules (e.g., *UserNotFound*, *PaymentRequired*, *ItemOutOfStock*), throwing raw `HTTPExceptions` everywhere can make your path code messy. 

Instead, you can define **Custom exceptions** and register a **Global Exception Handler** to catch them:

```python
from fastapi import Request
from fastapi.responses import JSONResponse

# 1. Define a custom Python exception class
class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

# 2. Register the global exception handler
@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "status": "error",
            "message": f"User {exc.name} Not Found"
        }
    )

# 3. Raise your custom exception inside path functions
@app.get("/user/{name}")
def get_user(name: str):
    if name != "Mohit":
        raise UserNotFoundException(name)
    return {"name": name}
```

---

### 🌟 Benefits of Global Exception Handlers

1.  **DRY (Don't Repeat Yourself):** You don't have to write HTTP response formatting logic multiple times.
2.  **Consistent Error Format:** Ensures every error returned by your API shares the exact same JSON structure (e.g., `{"status": "error", "message": "..."}`).
3.  **Centralized Management:** Easy to update the error formats or add logging in one place.
4.  **Better User Experience:** Provides clear, descriptive messages to the frontend.
5.  **Scalable API Design:** Keep route handlers focused solely on business logic.

---

## 🚀 Run This Module

```bash
cd status_code_responses
uvicorn app:app --reload
```

### Test Scenarios:

1.  **POST `/create_user`**: Check the response headers. The HTTP Status Code is **`201 Created`**.
2.  **GET `/user`**: Returns a custom success envelope structure.
3.  **GET `/user/{id}` (Standard HTTPException)**:
    *   `GET /user/1` → Returns user data (`200 OK`).
    *   `GET /user/99` → Returns `{"detail": "User Not Found"}` (`404 Not Found`).
4.  **GET `/user/{name}` (Global Exception Handler)**:
    *   `GET /user/Mohit` → Returns `{"name": "Mohit"}` (`200 OK`).
    *   `GET /user/Rohan` → Returns `{"status": "error", "message": "User Rohan Not Found"}` (`404 Not Found`). Notice how this structure matches our custom JSONResponse!

---

## 🔑 Key Takeaways

| Code Element | Type | Purpose |
|---|---|---|
| `status.HTTP_...` | Named Constant | Clean HTTP code names (e.g. `status.HTTP_201_CREATED`). |
| `HTTPException` | Built-in Class | Standard way to exit route functions with error responses. |
| `@app.exception_handler()` | Decorator | Ties a custom Python exception to a specific JSON response. |
| `JSONResponse` | Class | Returns raw JSON content and status codes directly from handlers. |

---

## 🎯 Interview Quick-Fire

**Q: What is the benefit of a Global Exception Handler in FastAPI?**
> A: It allows you to write custom Python exceptions inside your business logic and define a single handler that maps them to standardized, clean JSON responses globally. This separates error formatting from your core API logic.

**Q: What is the difference between `HTTPException` and a Custom Exception Handler?**
> A: `HTTPException` is a built-in utility class to throw basic errors with a `detail` string. Custom Exception Handlers let you catch custom exceptions and structure the response envelope exactly as you want (e.g. including error codes, debug information, or tracking IDs).

**Q: How do you return a specific HTTP status code for a successful request?**
> A: Set the `status_code` parameter in the path decorator: `@app.get("/items", status_code=status.HTTP_201_CREATED)`.

---

[← Previous: Response Models](../response_models/README.md) | [Back to Main README](../README.md) | [Next: Dependency Injection →](../dependency_injection/README.md)
