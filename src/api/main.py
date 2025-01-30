from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .infra.db.base import Base
from .infra.db.database import engine

def setup_app():
    app = FastAPI()
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)
    Base.metadata.create_all(bind=engine)

    from .routers.auth import auth_router
    from .routers.posts import posts_router
    app.include_router(auth_router)
    app.include_router(posts_router)

    return app