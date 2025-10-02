from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import requests
import os

app = FastAPI()

# Register compare router
app.include_router(requests.router)

# Path to "view" folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "view"))

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "view")), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
