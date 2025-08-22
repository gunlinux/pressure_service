from fastapi import FastAPI
from app.api.endpoints import users, pressure

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(pressure.router, prefix="/pressure", tags=["pressure"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
