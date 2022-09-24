from api.db import db
import api.schemas.login as login_schema

async def find_many(c):
    n = await c.count_documents({})
    return await c.find().to_list(length=n)

async def get_user():
    return await find_many(db.users)


async def create_user(user_body: login_schema.UserCreate):
    ub = user_body.dict()
    ub["isActive"]: login_schema.User = False
    await db.users.insert_one(ub)
    return login_schema.User(**ub)

async def update_user(user_id: int, user_body: login_schema.UserCreate):
    await db.users.update_one({"id": user_id},{"$set": user_body.dict()})
    return await db.users.find_one({"id": user_id})

async def delete_user(user_id: int):
    await db.users.delete_one({"id": user_id})

async def get_isActive(user_id: int):
    res = await db.users.find_one({"id": user_id})
    print(res)
    return login_schema.UserisActiveResponse(**res)

async def set_isActive(user_id: int):
    await db.users.update_one({"id": user_id},{"$set": {"isActive": True}})

async def delete_isActive(user_id: int):
    await db.users.update_one({"id": user_id},{"$set": {"isActive": False}})