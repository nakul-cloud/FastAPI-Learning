# 🚦 Module 7 — HTTP Status Codes & Error Handling

> **Goal:** Learn how to return standard HTTP status codes for successful operations and raise clean HTTP exceptions when things go wrong.

---

## 🧠 Concepts Covered

### 1. What are HTTP Status Codes?

HTTP status codes are standard 3-digit numbers returned by servers to inform clients about the result of their request.

| Range | Type | Meaning | Examples |
|---|---|---|---|
| **`2xx`** | **Success** | Request was completed successfully | `200 OK`, `201 Created` |
| **`3xx`** | **Redirection** | Further action needs to be taken | `301 Moved Permanently` |
| **`4xx`** | **Client Error** | The client made a mistake | `400 Bad Request`, `401 Unauthorized`, `404 Not Found` |
| **`5xx`** | **Server Error** | The server failed to fulfill request | `500 Internal Server Error` |

---

### 2. Setting Custom Success Status Codes

By default, FastAPI returns a `200 OK` for successful requests. However, for creation requests, it is a best practice to return a `201 Created` status code.

We can define this in the path decorator using the `status_code` parameter:

```python
from fastapi import status

@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User Created",
        "status": status.HTTP_201_CREATED
    }
```

> 💡 **Tip:** Always use FastAPI's built-in `status` module (e.g. `status.HTTP_201_CREATED`) instead of the raw number `201`. This prevents typos and makes code self-documenting!

---

### 3. Custom Response Structures

Instead of raw entities, APIs often wrap their outputs in a unified envelope structure for consistency across the frontend app:

```python
@app.get("/user")
def get_user():
    return {
        "status": "Success",
        "message": "User Found",
        "data": {
            "name": "Mohit",
            "age": 22,
            "email": "mohit@example.com"
        }
    }
```

---

### 4. Error Handling & Raising `HTTPException`

When something goes wrong (e.g., resource not found, invalid credentials, data conflict), you should stop execution and return a specific HTTP error. In FastAPI, we do this by **raising** `HTTPException`:

```python
from fastapi import HTTPException

@app.get("/user/{id}")
def get_user(id: int):
    if id == 5:
        return {"message": "User Found"}
    else:
        # Raising HTTPException stops execution and returns immediately
        raise HTTPException(status_code=404, detail="User Not Found")
```

When `id` is not `5`, the response will be:
*   **Status Code:** `404 Not Found`
*   **Response Body:**
    ```json
    {
      "detail": "User Not Found"
    }
    ```

---

## 🚀 Run This Module

```bash
cd status_code_responses
uvicorn app:app --reload
```

Test at `http://127.0.0.1:8000/docs`:
1.  **POST `/create_user`**: Check the response headers to see the `201 Created` status.
2.  **GET `/user`**: View the standardized success response envelope.
3.  **GET `/user/{id}`**: 
    *   Enter `5` → Returns `{"message": "User Found"}` with `200 OK`.
    *   Enter `10` → Returns `{"detail": "User Not Found"}` with `404 Not Found`.

---

## 🔑 Key Takeaways

| Concept | Syntax / Usage | Why Use It |
|---|---|---|
| Success Status Code | `@app.post(..., status_code=status.HTTP_201_CREATED)` | Communicates exactly what happened (e.g., resource created). |
| `status` module | `from fastapi import status` | Avoids magic numbers in code. |
| `HTTPException` | `raise HTTPException(status_code=..., detail=...)` | Standardizes error responses with accurate HTTP codes. |

---

## 🎯 Interview Quick-Fire

**Q: Which HTTP status code should be returned when creating a new resource?**
> A: `201 Created`.

**Q: How do you trigger an error response early in a FastAPI path function?**
> A: By using the `raise` keyword with `HTTPException`, specifying the status code and a descriptive detail message.

**Q: What is the benefit of `from fastapi import status`?**
> A: It provides clean, readable aliases for all standard HTTP status codes (e.g., `status.HTTP_404_NOT_FOUND` instead of `404`), reducing magic numbers.

---

[← Previous: Response Models](../response_models/README.md) | [Back to Main README](../README.md)
