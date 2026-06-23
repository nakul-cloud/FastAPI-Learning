# 🗄️ Module 10 — Database Integration (SQLite)

> **Goal:** Learn how to connect your FastAPI application to a persistent SQLite database, create tables, and execute SQL statements.

---

## 🧠 Concepts Covered

### 1. Persistent Storage vs In-Memory List

Up to this point, our apps stored data in a Python list (`todos = []`). 
*   **The Problem:** Every time the server reloaded or restarted, all data was wiped out.
*   **The Solution:** Connect to a relational database like **SQLite** that writes data to a local file (`test.db`), preserving records across restarts.

---

### 2. Setting Up SQLite

Python has built-in support for SQLite via the `sqlite3` module.

```python
import sqlite3

# 1. Connect to the SQLite database file
conn = sqlite3.connect('test.db', check_same_thread=False)

# 2. Create a cursor to execute SQL commands
cursor = conn.cursor()
```

#### Why `check_same_thread=False` is CRITICAL in FastAPI:
By default, SQLite only allows the thread that created the connection to communicate with the database. However, FastAPI is asynchronous and handles requests using **multiple concurrent threads**. 

Setting `check_same_thread=False` allows FastAPI to safely query the SQLite database across different threads.

---

### 3. Creating Tables on Startup

You want to make sure your database tables exist before the API starts accepting traffic. We run a `CREATE TABLE IF NOT EXISTS` statement right after establishing the connection:

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        completed TEXT
    )
""")
# Commit the transaction to save the table structure
conn.commit()
```

---

### 4. Basic SQLite Query Flow

```python
@app.get('/home')
def home():
    return {
        "Message": "SQLite connected"
    }
```

*   **Connection (`conn`)**: Handles database transactions (commit/rollback).
*   **Cursor (`cursor`)**: Executes SQL queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) and fetches query results (`cursor.fetchone()`, `cursor.fetchall()`).

---

## 🚀 Run This Module

```bash
cd database
uvicorn app:app --reload
```

1. Open `http://127.0.0.1:8000/home`.
2. Observe the JSON response: `{"Message": "SQLite connected"}`.
3. Check your `database/` folder. You will see a newly generated file named **`test.db`**. This is your binary database database file!

---

## 🔑 Key SQL commands for SQLite

| Command | Purpose |
|---|---|
| `CREATE TABLE` | Defines new tables and field types. |
| `PRIMARY KEY AUTOINCREMENT` | Automatically assigns a unique ascending integer ID to each record. |
| `conn.commit()` | Saves current transaction modifications to disk. |

---

## 🎯 Interview Quick-Fire

**Q: Why does SQLite need `check_same_thread=False` in FastAPI?**
> A: FastAPI uses multiple threads to process asynchronous requests. By default, SQLite prevents a connection from being shared across multiple threads to avoid conflicts. Setting this to `False` enables thread-sharing, allowing FastAPI to perform operations concurrently.

**Q: What is the purpose of `conn.commit()`?**
> A: It commits the current transaction. In database management, operations like `INSERT`, `UPDATE`, or `DELETE` are queued and not written permanently to disk until a commit is issued.

**Q: What is the difference between a Connection and a Cursor in python's `sqlite3`?**
> A: The Connection object represents the database database engine. The Cursor object is used to execute SQL queries, traverse query results, and fetch rows.

---

[← Previous: Middleware](../middleware/README.md) | [Back to Main README](../README.md)
