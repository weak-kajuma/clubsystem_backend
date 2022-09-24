from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from api.routers import login

app = FastAPI(root_path="/clubsystem/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(login.router)
