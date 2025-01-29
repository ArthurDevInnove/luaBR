from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.auth import router
from .infra.db.base import Base
from .infra.db.database import engine
from .models.user import UserModel

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

Base.metadata.create_all(bind=engine)

@app.get('/')
async def read_root():
    return 'App is executing'