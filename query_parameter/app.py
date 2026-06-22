from fastapi import FastAPI

app=FastAPI()


# Single/optional Query Parameter


@app.get("/users")
def get_users(name:str=None):
    return{"Name":name}


# Default Value Parameter

@app.get("/product")
def get_product(limit:int=10):
    return{"limit":limit}


# Multiple Query Parameter

@app.get("/items")
def get_items(name:str = None,price:int = 0):
    return{"name":name,"price":price}