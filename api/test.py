import asyncio
from api.db import db

async def find_many(collection):
    n = await collection.count_documents({})
    return await collection.find().to_list(length=n)

async def db_insert():
    await db.test.drop()
    for i in range(1000):
        for n in range(1000):
            await db.test.insert_one({"id": i, "number": n})
    result = await find_many(db.test)
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(db_insert())