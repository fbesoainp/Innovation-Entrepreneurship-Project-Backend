from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import routers.compliance

app = FastAPI()

app.include_router(routers.compliance.router)

origins = [
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
