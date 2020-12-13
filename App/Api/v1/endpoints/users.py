from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/")
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]


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