from typing import List
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from App.Core.config import settings
from App.Models import UserModel
from App.Http.requests import UserCreateRequest

from App.Api.admin import admin_api_router

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title=settings.PROJECT_NAME, openapi_url="/api/admin/openapi.json")

# Admin API 
app.include_router(admin_api_router, prefix=settings.API_ADMIN_PREFIX)

# CORSMiddleware
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# config static files & Themes
app.mount("/static", StaticFiles(directory="App/public/static"), name="static")
app.mount("/js", StaticFiles(directory="App/Themes/admin/dist/js"), name="js")
app.mount("/css", StaticFiles(directory="App/Themes/admin/dist/css"), name="css")
AppVue = Jinja2Templates(directory="App/Themes/admin/dist")


@app.on_event("startup")
def startup_event():
    # print(settings)
    pass


@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    app_data = {
        "request": request,
        "app": {
            "name": "App"
        },
    }
    return AppVue.TemplateResponse("index.html", app_data)