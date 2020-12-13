from fastapi import APIRouter
from App.Api.admin.endpoints import users

admin_api_router = APIRouter()
admin_api_router.include_router(users.router, prefix="/users", tags=["users"])