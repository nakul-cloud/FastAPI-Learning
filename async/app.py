'''
async is non blocking approach where we can do multiple tasks at the same time 
in single thread without blocking the main thread .  
'''


import time
import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():
    await asyncio.sleep(10)
    return {"message":"Task Completed After 10 second"}