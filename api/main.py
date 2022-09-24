from fastapi import FastAPI
from api.routers import login

app = FastAPI()
app.include_router(login.router)