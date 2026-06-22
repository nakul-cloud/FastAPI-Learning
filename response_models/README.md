# 📤 Module 6 — Response Models & Data Filtering

> **Goal:** Learn how to control and filter the data returned by your API endpoints using response models, ensuring security and efficiency.

---

## 🧠 Concepts Covered

### 1. What is a Response Model?

A **response model** defines the exact structure and validation schema for the data that the API returns to the client.

By default, an endpoint might return whatever dictionary or object you return from the function. But in a real-world scenario, you want to limit what fields are sent back to the frontend (e.g., hiding password hashes, internal database IDs, or audit timestamps).

In FastAPI, we use the `response_model` parameter in the path decorator:

```python
@app.post("/user", response_model=UserResponse)  # ← Declared here!
def get_user(user: User):
    return { ... }
```

---

### 2. Request Models vs Response Models

This is a **critical concept** in backend design:

*   **Request Model:** Defines the structure of **incoming** data (data from the client to the server). Usually includes fields like raw passwords, setup details, etc.
*   **Response Model:** Defines the structure of **outgoing** data (data from the server to the client). Usually filters out sensitive or unnecessary fields.

```
       [ Client ]
        /      \
  Request       Response
  (Input)       (Output)
   /              \
[ User ]   →   [ UserResponse ]
  - name         - name
  - age          - age
  - password     (password filtered!)
```

---

### 3. Code Breakdown: Filtering Sensitive Data

In `app.py`, we define two separate schemas:

```python
from pydantic import BaseModel

# 1. The input schema (Request Model) - includes password
class User(BaseModel):
    name: str
    age: int
    password: str

# 2. The output schema (Response Model) - excludes password
class UserResponse(BaseModel):
    name: str
    age: int
```

Then we register `response_model=UserResponse` on the route decorator:

```python
@app.post("/user", response_model=UserResponse)
def get_user(user: User):
    # Even though we return the password here:
    return {
        "name": "Mohit",
        "age": 22,
        "password": "12345"
    }
    # FastAPI automatically filters it out because of response_model=UserResponse!
```

#### The Result:
The client only receives:
```json
{
  "name": "Mohit",
  "age": 22
}
```

---

## 🚀 Run This Module

```bash
cd response_models
uvicorn app:app --reload
```

1. Open `http://127.0.0.1:8000/docs`
2. Test the `POST /user` endpoint.
3. Supply a request body containing a password:
   ```json
   {
     "name": "Nakul",
     "age": 22,
     "password": "mysecretpassword"
   }
   ```
4. Observe the response. Notice that the password field is **completely removed** from the output JSON!

---

## 🔑 Key Takeaways

| Term / Parameter | Purpose |
|---|---|
| `response_model` | Specifies the schema used to validate and serialize the outgoing response. |
| **Data Filtering** | Automatically drops any keys/fields not defined in the response model. |
| **Data Conversion** | Converts output data types (e.g. converting a database ORM object to a clean JSON dict). |
| **Security** | Prevents accidental leaks of sensitive details (passwords, tokens, internal keys). |

---

## 🎯 Interview Quick-Fire

**Q: Why should we use `response_model` in FastAPI?**
> A: It guarantees data validation for outputs, automatically filters out fields that shouldn't be exposed, and documents the response structure in Swagger UI.

**Q: What is the main difference between Request Models and Response Models?**
> A: Request Models validate data coming *into* the API. Response Models shape and validate data going *out of* the API.

**Q: If my function returns a dictionary with 10 keys, but `response_model` only has 3 fields, what will the client receive?**
> A: The client will receive only those 3 fields. FastAPI automatically filters out the extra 7 fields.

---

[← Previous: CRUD](../CRUD/README.md) | [Back to Main README](../README.md) | [Next: Status Codes & Error Handling →](../status_code_responses/README.md)
