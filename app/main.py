from fastapi import FastAPI
from app.routes import requests

app = FastAPI()

# Register the router
app.include_router(requests.router)
