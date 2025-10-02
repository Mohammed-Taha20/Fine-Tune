from fastapi import FastAPI
from routes import requests

app = FastAPI()

# Register the router
app.include_router(requests.router)
