from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import routers

app = FastAPI()

origins = [
    "http://localhost:3000",  # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all (not recommended in prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routers
for router in routers:
    app.include_router(router)
