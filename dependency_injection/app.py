'''
It’s just a way to give a function/class the things it needs (dependencies) without hardcoding them inside.
Instead of creating objects or logic inside your function, FastAPI injects them for you automatically.
Keeps code clean and reusable.
Makes testing easier (you can swap dependencies).
Avoids repeating the same setup code everywhere.
'''

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def common_logic():
    return {"message":"Common Logic"}

def get_current_user():
    return {"user":"Nakul"}

# Auth Tokens
def verify_token(token:str=Header(None)):
    if token != 'mysecrettoken':
        raise HTTPException(status_code=401, detail="Invalid Token")
    return {"token":token}


@app.get('/home')
def home(data=Depends(common_logic)):
    return{
        "home":"Home Page",
        "data":data
    }

@app.get('/profiel')
def get_profile(user=Depends(get_current_user)):
    return{
        "profile":"Profile Page",
        "user":user
    }

@app.get('/dashboard')
def dashboard(user=Depends(get_current_user)):
    return user

@app.get('/secure_data')
def secure_data(user=Depends(verify_token)):
    return{"message":"secure Data","user":user}
