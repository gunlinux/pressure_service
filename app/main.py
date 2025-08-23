from fastapi import FastAPI
from app.admin import init_admin
from app.api.endpoints import users
from app.db.session import engine

app = FastAPI()

app.include_router(users.router, prefix='/users', tags=['users'])

init_admin(app, engine)


@app.get('/')
def read_root():
    return {'Hello': 'World'}
