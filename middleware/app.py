'''
Middleware is a function that is called before the request is processed by the FastAPI application and after the response is sent to the client.
Middleware are used to perform tasks such as authentication,logging,rate limiting,etc.
It is a secure layer between request and response (Client and server)
Middleware is global and can be used in any endpoint ,dependency injection is per route and specific api 
'''

from fastapi import FastAPI ,Request
import time

app = FastAPI()

'''
call_next is used to send the request to the next middleware or endpoint
'''

# @app.middleware("http")
# async def my_middleware(request:Request,call_next):
#     print("request Recieved")

#     respone = await call_next(request)

#     print("Response Generated")
#     return respone

# ------------------------------------------------------------------------
# Logging Middleware

@app.middleware('http')
async def log_middleware(request:Request,call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time()- start_time
    print("Request Recieved At:",request.url)
    print("Process time:",process_time)
    return response
