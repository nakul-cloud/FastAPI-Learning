# 🔌 Module 9 — HTTP Middleware

> **Goal:** Learn how to build global request-response interceptors (Middleware) in FastAPI to run background operations like logging, timing, and security headers.

---

## 🧠 What is Middleware?

A **middleware** is a function that runs **before** every request is processed by the path operation (endpoint) and also **after** the response is generated but before it's sent back to the client.

It acts as a secure, global interceptor layer wrapping your entire application.

```
       [ Client ]
        /      \
    Request   Response
      /          \
[  M I D D L E W A R E  ]  <-- Custom headers, Logging, Gzip
      \          /
    Request   Response
        \      /
     [ FastAPI App ]      <-- Path functions run here
```

---

## 🔍 Concepts Covered

### 1. The HTTP Middleware Decorator

To declare a middleware, decorate an `async` function with `@app.middleware("http")`:

```python
from fastapi import Request

@app.middleware("http")
async def my_middleware(request: Request, call_next):
    # 1. Code to execute BEFORE the endpoint handles the request
    
    response = await call_next(request)
    
    # 2. Code to execute AFTER the endpoint finishes, before sending to client
    
    return response
```

*   **`request`**: The incoming HTTP Request object containing headers, URL, client details, query parameters, etc.
*   **`call_next`**: A function that forwards the `request` to the next step in the pipeline (either another middleware or your final endpoint handler). It returns the `response` object.

---

### 2. Time-Logging Middleware Example

In `app.py`, we implement a logging middleware that calculates how long each API call takes to process:

```python
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware('http')
async def log_middleware(request: Request, call_next):
    # 1. Capture the start time
    start_time = time.time()
    
    # 2. Forward request to endpoint & wait for response
    response = await call_next(request)
    
    # 3. Calculate process time
    process_time = time.time() - start_time
    
    # 4. Log the details to console
    print("Request Received At:", request.url)
    print("Process time:", process_time)
    
    # 5. Send response to client
    return response
```

---

### 3. Middleware vs Dependency Injection (`Depends`)

Both intercept requests, but they differ significantly in application scope:

| Feature | Middleware | Dependency Injection |
|---|---|---|
| **Scope** | **Global** (All endpoints) | **Local** (Per endpoint or per router) |
| **Execution** | Automatic on every request | Explicitly invoked with `Depends(...)` |
| **Input/Output** | Operates on raw `Request` / `Response` | Operates on parsed schemas, models, parameters |
| **Common Uses** | CORS, Gzip compression, IP Blacklisting, global execution timers | DB Sessions, OAuth authorization check, resource-level access |

---

## 🚀 Run This Module

```bash
cd middleware
uvicorn app:app --reload
```

1. Open `http://127.0.0.1:8000/docs` (or load any endpoint).
2. Look at your terminal console. You will see lines printed by the middleware:
   ```text
   Request Received At: http://127.0.0.1:8000/docs
   Process time: 0.0019989013671875
   ```

---

## 🎯 Interview Quick-Fire

**Q: What is `call_next` in FastAPI middleware?**
> A: It is an asynchronous function that takes the HTTP `Request` as input, passes it down the routing pipeline, and returns the HTTP `Response` produced by the corresponding path function.

**Q: Can you edit the request/response headers in middleware?**
> A: Yes! You can inspect and modify request headers *before* calling `call_next(request)`. You can also inject custom headers into `response.headers` *after* calling `call_next`.
> ```python
> response.headers["X-Process-Time"] = str(process_time)
> ```

**Q: What happens if an exception is raised inside the endpoint? Does the middleware still run?**
> A: Yes, but if the exception is not handled by FastAPI's default exception handlers, the middleware might catch the exception, or the pipeline will break. It is best practice to wrap `await call_next(request)` in a try-except block inside middleware if you want to handle unexpected errors gracefully.

---

[← Previous: Dependency Injection](../dependency_injection/README.md) | [Back to Main README](../README.md) | [Next: Database Integration →](../database/README.md)
