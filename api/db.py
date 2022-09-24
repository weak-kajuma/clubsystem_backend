import motor.motor_asyncio

Client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:tepic2022@mongo/')
db = Client.clubsystem