from fastapi import APIRouter
from typing import List
import api.schemas.login as login_schema
import api.cruds.login as login_crud

router = APIRouter()

@router.get("/user", response_model=List[login_schema.User])
async def get_user():
    return await login_crud.get_user()

@router.post("/user", response_model=login_schema.UserCreateResponse)
async def create_user(user_body: login_schema.UserCreate):
    return await login_crud.create_user(user_body)

@router.put("/user/{user_id}", response_model=login_schema.UserCreateResponse)
async def update_user(user_id: int, user_body: login_schema.UserCreate):
    return await login_crud.update_user(user_id, user_body)

@router.delete("/user/{user_id}")
async def delete_user(user_id: int):
    await login_crud.delete_user(user_id)

@router.get("/user/{user_id}/isActive", response_model=login_schema.UserisActiveResponse)
async def get_isActive(user_id: int):
    return await login_crud.get_isActive(user_id)

@router.put("/user/{user_id}/isActive", response_model=login_schema.UserisActiveResponse)
async def set_isActive(user_id: int):
    await login_crud.set_isActive(user_id)
    return await login_crud.get_isActive(user_id)

@router.delete("/user/{user_id}/isActive", response_model=login_schema.UserisActiveResponse)
async def delete_isActive(user_id: int):
    await login_crud.delete_isActive(user_id)
    return await login_crud.get_isActive(user_id)