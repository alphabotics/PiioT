from fastapi import APIRouter, Depends, HTTPException
from App.Http.responses.user_response import (
    UserItemResponse, UserPaginationResponse
)
from App.Database.repositories.user_repository import UserRepository

router = APIRouter()


@router.get("/", response_model=UserPaginationResponse)
async def read_users():
    userRepository = UserRepository()
    users = userRepository.paginate()
    return users


@router.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}


@router.put("/{item_id}", 
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "foo":
        raise HTTPException(status_code=403, detail="You can only update the item: foo")
    return {"item_id": item_id, "name": "The Fighters"}