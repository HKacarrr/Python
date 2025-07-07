from fastapi import FastAPI
from API.Core.ExceptionHandler import global_exception_handler
# from fastapi.requests import Request
from API.Product.Product import router

app = FastAPI()

app.add_exception_handler(Exception, global_exception_handler)

app.include_router(router)