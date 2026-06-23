from fastapi import FastAPI, HTTPException, Depends, status
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password Hashing Setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 Bearer token helper (specifies the endpoint Uvicorn/Swagger uses to fetch tokens)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Hashed password storage for demonstration (usually pulled from DB)
# Hashed value of password "12345"

fake_user_db={
    'admin':{
        'username':'admin',
        'hashed_password':pwd_context.hash('12345')
    }
}
# Hash Password
def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Token Creation

def create_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expiry})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Login API (Generates Token using OAuth2 form validation)
@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # OAuth2PasswordRequestForm receives data from request body form data
    user =fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user['hashed_password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid Credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # "sub" is the standard JWT payload key for subject (the user identity)
    token = create_token({"sub": form_data.username})
    
    # OAuth2 spec requires returning 'access_token' and 'token_type'
    return {"access_token": token, "token_type": "bearer"}

# Token Verify Dependency
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Decode and verify token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid Token")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")

# Dashboard API (Protected Route)
@app.get('/secure')
def secure_data(current_user: str = Depends(get_current_user)):
    return {
        "message": "Secure Data",
        "user": current_user
    }
