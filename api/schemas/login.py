from typing import Optional
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    id: int = Field(None, description="学籍番号")
    name: Optional[str] = Field(None, example="Taka")
    grade: Optional[int] = Field(None, example=2)
    category: Optional[str] = Field(None, example="Programing")

class User(UserBase):
    isActive: bool = Field(False, description="入室状況")

class UserCreate(UserBase):
    pass

class UserCreateResponse(User):
    pass

class UserisActiveResponse(BaseModel):
    id: int = Field(None, description="学籍番号")
    isActive: bool = Field(False, description="入室状況")