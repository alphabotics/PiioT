from fastapi import APIRouter, Depends, HTTPException, Response, status
from App.Http.responses.user_response import (
    UserItemResponse, UserPaginationResponse
)
from App.Http.requests.user_request import (
    UserCreateRequest, UserUpdateRequest
)
from App.Database.repositories.user_repository import UserRepository

router = APIRouter()

userRepository = UserRepository()
    
@router.get("/", response_model=UserPaginationResponse)
async def read_users(per_page: int=10, page: int=1):
    users = userRepository.paginate(per_page, page)
    return users


@router.get("/{id}", response_model=UserItemResponse)
async def read_user(id: int):
    user = userRepository.find(id)
    return user


@router.post("/", response_model=UserItemResponse, status_code=status.HTTP_201_CREATED)
async def create_user(request: UserCreateRequest):
    user = userRepository.create(request)
    # return request
    return user


@router.put("/{id}", response_model=UserItemResponse)
async def update_user(id: int, request: UserUpdateRequest):
    user = userRepository.update(id, request)
    return user


@router.delete("/{id}")
async def delete_item(id: int, response: Response):
    is_deleted = userRepository.delete(id)
    if is_deleted is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        message = 'User {id} is not found!'.format(id=id)
    elif is_deleted == True:
        message = 'Delete user successfully'
    return {
        'message': message
    }
    