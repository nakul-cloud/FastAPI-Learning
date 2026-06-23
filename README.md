# ⚡ FastAPI Learning — From Zero to API Hero

> **A hands-on, module-by-module FastAPI course.**
> Each folder is a self-contained lesson. Read the code → run it → tweak it → own it.

---

## 📚 What Is FastAPI?

FastAPI is a **modern, high-performance** Python web framework for building APIs.

| Feature | Why It Matters |
|---|---|
| **Fast** | Built on Starlette & Uvicorn — one of the fastest Python frameworks |
| **Type Hints** | Uses Python type hints for auto-validation & auto-docs |
| **Auto Docs** | Swagger UI (`/docs`) and ReDoc (`/redoc`) generated automatically |
| **Async Ready** | Native `async/await` support for high-concurrency apps |
| **Pydantic** | Built-in data validation via Pydantic models |

---

## 🗂️ Project Structure

```
FastAPI-Learning/
│
├── routes/                 # 📍 Module 1 — Routes & Path Parameters
│   ├── app.py
│   └── README.md
│
├── query_parameter/        # 🔍 Module 2 — Query Parameters
│   ├── app.py
│   └── README.md
│
├── request_body/           # 📦 Module 3 — Request Body & Validation
│   ├── app.py
│   └── README.md
│
├── pydantic_models/        # 🧱 Module 4 — Pydantic Models & Nesting
│   ├── app.py
│   └── README.md
│
├── CRUD/                   # ✅ Module 5 — Full CRUD Operations
│   ├── app.py
│   └── README.md
│
├── response_models/        # 📤 Module 6 — Response Models & Data Filtering
│   ├── app.py
│   └── README.md
│
├── status_code_responses/  # 🚦 Module 7 — HTTP Status Codes & Error Handling
│   ├── app.py
│   └── README.md
│
├── dependency_injection/   # 💉 Module 8 — Dependency Injection (Depends)
│   ├── app.py
│   └── README.md
│
├── middleware/             # 🔌 Module 9 — HTTP Middleware
│   ├── app.py
│   └── README.md
│
├── database/               # 🗄️ Module 10 — Database Integration (SQLite)
│   ├── app.py
│   └── README.md
│
├── .agents/SKILLS.md       # 🗺️ Learning roadmap & resource links
└── README.md               # ← You are here
```

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.8+
- `pip` or a virtual environment tool

### 2. Setup

```bash
# Clone the repo
git clone https://github.com/nakul-cloud/FastAPI-Learning.git
cd FastAPI-Learning

# Create & activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install fastapi uvicorn pydantic
```

### 3. Run Any Module

Every module follows the same pattern — `cd` into the folder and run:

```bash
cd routes
uvicorn app:app --reload
```

Then open your browser:

| URL | What It Shows |
|---|---|
| `http://127.0.0.1:8000` | Your API response |
| `http://127.0.0.1:8000/docs` | 📄 Swagger UI (interactive docs) |
| `http://127.0.0.1:8000/redoc` | 📘 ReDoc (alternative docs) |

> 💡 **Tip:** The `--reload` flag auto-restarts the server when you save changes. Perfect for learning!

---

## 📖 Module-by-Module Learning Path

### Module 1 → [`routes/`](./routes/)
**What you'll learn:** Creating your first API, defining multiple endpoints, and dynamic path parameters.

---

### Module 2 → [`query_parameter/`](./query_parameter/)
**What you'll learn:** Optional parameters, default values, and combining multiple query params.

---

### Module 3 → [`request_body/`](./request_body/)
**What you'll learn:** Sending JSON data via POST requests, Pydantic validation, and Dict vs Pydantic.

---

### Module 4 → [`pydantic_models/`](./pydantic_models/)
**What you'll learn:** Pydantic BaseModel, field types, and nested models for complex data.

---

### Module 5 → [`CRUD/`](./CRUD/)
**What you'll learn:** Full Create-Read-Update-Delete operations on an in-memory Todo list.

---

### Module 6 → [`response_models/`](./response_models/)
**What you'll learn:** Restricting/filtering outbound data, Request vs Response schemas, and hiding sensitive fields (e.g. passwords).

---

### Module 7 → [`status_code_responses/`](./status_code_responses/)
**What you'll learn:** Standardizing response envelopes, setting HTTP success codes (e.g. `201 Created`), raising standard `HTTPException` for client errors, and registering Global Custom Exception Handlers (`@app.exception_handler`).

---

### Module 8 → [`dependency_injection/`](./dependency_injection/)
**What you'll learn:** Reusable operations using `Depends`, auth checks, fetching headers, and DI vs Middleware.

---

### Module 9 → [`middleware/`](./middleware/)
**What you'll learn:** Custom request-response interception logic, accessing headers globally, calculating process time, and CORS concepts.

---

### Module 10 → [`database/`](./database/)
**What you'll learn:** SQLite connection setup, thread safety using `check_same_thread=False`, executing query executions, and schema initialization.

---

## 🧠 FastAPI Cheat Sheet (Interview Quick-Revision)

### Core Concepts at a Glance

```python
from fastapi import FastAPI, status, HTTPException, Depends, Header
from pydantic import BaseModel

app = FastAPI()

# ── Dependency injection function ──
def get_db_session():
    # Setup connection
    return "session"

# ── GET with path parameter & Dependency Injection ──
@app.get("/items/{item_id}")
def read_item(item_id: int, session=Depends(get_db_session)):
    return {"item_id": item_id, "session": session}

# ── GET with query parameter ──
@app.get("/search")
def search(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit}

# ── POST with request body, response model & custom status ──
class Item(BaseModel):
    name: str
    price: float
    secret_key: str

class ItemResponse(BaseModel):
    name: str
    price: float

@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    if item.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be positive")
    return item
```

### How FastAPI Decides Parameter Type

| Where is it? | FastAPI treats it as |
|---|---|
| In the **path** → `"/users/{id}"` | **Path Parameter** |
| Declared with `Depends(...)` | **Injected Dependency** |
| A **Pydantic model** in function args | **Request Body** |
| Everything else | **Query Parameter** |

### HTTP Status Code Ranges

| Status Code Range | Category | Purpose / Common Example |
|---|---|---|
| **`2xx`** | **Success** | `200 OK` (Standard success), `201 Created` (Resource created) |
| **`3xx`** | **Redirection** | `301 Moved Permanently` |
| **`4xx`** | **Client Error** | `400 Bad Request`, `401 Unauthorized`, `404 Not Found` |
| **`5xx`** | **Server Error** | `500 Internal Server Error` (Bug on server-side) |

### DI vs Middleware Comparison

| Aspect | Dependency Injection (`Depends`) | Middleware |
|---|---|---|
| **Scope** | Route / Router specific | Global (every request) |
| **Granularity** | Highly detailed (parsed types, context) | Low detailed (raw request/response objects) |
| **Use cases** | DB connections, Authenticated user object | Logging, CORS, Gzip compression, timers |

---

## 🔗 Learning Resources

| Resource | Link |
|---|---|
| 📹 Video Tutorial | [YouTube — FastAPI Full Course](https://www.youtube.com/watch?v=fxRCoEUmq8s) |
| 📄 Official Docs | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) |
| 📗 GeeksforGeeks | [FastAPI Tutorial](https://www.geeksforgeeks.org/fastapi-tutorial/) |
| 🐍 Python Reference | [W3Schools Python](https://www.w3schools.com/python/) |
| ✍️ Medium Articles | [Medium #fastapi](https://medium.com/tag/fastapi) |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-2D2D2D?style=for-the-badge)

---

## 📝 How to Use This Repo for Revision

1. **Before an interview** — Read each folder's `README.md` for concept summaries.
2. **Quick code reference** — Check the cheat sheet above.
3. **Hands-on practice** — Run each module, hit the `/docs` endpoint, and test APIs live.
4. **Extend it** — Add your own modules as you learn (middleware, auth, database, etc.).

---

<p align="center">
  <b>Made with ❤️ while learning FastAPI</b><br>
  <i>Keep building. Keep shipping. 🚀</i>
</p>
