# ⏳ Module 12 — Async / Await & Concurrency

> **Goal:** Understand asynchronous programming in FastAPI, how `async/await` works under the hood, and how to write non-blocking API endpoints.

---

## 🧠 Concepts Covered

### 1. What is Async / Await?

In traditional web frameworks, each incoming request blocks the execution thread until it completes. If a database query takes 3 seconds, that thread is stuck and cannot serve other users.

FastAPI is built on **ASGI (Asynchronous Server Gateway Interface)**, which supports **asynchronous concurrency** using a single execution thread.

*   **`async def`**: Declares that a function is a coroutine and can yield control when waiting for I/O operations (like database queries, file reading, or external API calls).
*   **`await`**: Tells the Python Event Loop: *"I am waiting for this slow operation to complete. You can go ahead and execute other tasks in the meantime."*

---

### 2. Async Non-Blocking vs Blocking Sleep

Compare these two mechanisms:

```python
# ❌ BLOCKING (Time Sleep)
import time
def get_data():
    time.sleep(10)  # Blocks the entire server thread! No other request can run.
    return {"data": "done"}

# ✅ NON-BLOCKING (Asyncio Sleep)
import asyncio
async def get_data():
    await asyncio.sleep(10)  # Pauses this route but lets other requests process!
    return {"data": "done"}
```

---

### 3. Understanding the Event Loop

FastAPI runs on an **Event Loop**. Think of it like a waiter in a restaurant:
*   **Blocking (Sync):** The waiter takes your order, walks to the kitchen, and stands there waiting 10 minutes for your food to cook. No other tables can get their orders taken.
*   **Non-Blocking (Async):** The waiter takes your order, gives it to the kitchen, and immediately goes to take orders from other tables. When your food is ready, the waiter returns to serve you.

---

## 🚀 Run This Module

```bash
cd async
uvicorn app:app --reload
```

### Let's Prove Async is Non-Blocking:

1. Open **two separate tabs** in your browser pointing to `http://127.0.0.1:8000/`.
2. Hit Enter on Tab 1, and immediately hit Enter on Tab 2.
3. **If it was blocking:** Tab 2 would wait for Tab 1 to finish (10 seconds) + its own processing (10 seconds) = 20 seconds total.
4. **Because it is async:** Both requests run concurrently. Both will complete and return their response at almost the exact same time (10 seconds total)!

---

## 🔑 Key Takeaways

| Concept | Explanation |
|---|---|
| **Event Loop** | The manager that schedules and executes asynchronous tasks. |
| `async def` | Marks a function as a coroutine (non-blocking capable). |
| `await` | Passes control back to the event loop during slow I/O tasks. |
| **Concurrency** | Handling multiple requests at the same time using a single thread. |

---

## 🎯 Interview Quick-Fire

**Q: When should I use `async def` instead of standard `def` in FastAPI?**
> A: Use `async def` when your endpoint performs asynchronous I/O operations (like querying a database using an async driver, calling external APIs using `htpx`, or reading files async). If your code performs heavy CPU-bound computation or uses blocking sync drivers (like standard `psycopg2` or `sqlite3`), use standard `def` — FastAPI will automatically run it in a separate threadpool to avoid blocking the event loop.

**Q: Does `async` make my code run faster?**
> A: It doesn't speed up a single database query. Instead, it allows the server to handle **thousands of concurrent users** on a single thread by not letting idle waiting block other requests. It improves system *throughput*, not individual function *latency*.

**Q: What happens if I write `time.sleep(10)` inside an `async def` route?**
> A: It will block the entire Event Loop. Since it is blocking, no other async routes will run, completely defeating the purpose of using `async def`. Always use `await asyncio.sleep(...)` or run sync code in standard `def` functions.

---

[← Previous: JWT Authentication](../auth/README.md) | [Back to Main README](../README.md)
