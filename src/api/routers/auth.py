from fastapi import APIRouter, Depends, Response
from ..infra.db.session import get_session
from ..services.user import insert_user, authenticate_user
from ..schemas.user import UserCreate, UserLogin
from sqlalchemy.orm import Session

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@auth_router.post('/register')
async def register_user(user: UserCreate, session: Session = Depends(get_session)):
    insert_user(user, session)

    return UserCreate(
        **user.__dict__
    )

@auth_router.post('/login')
async def login(response: Response, user_login: UserLogin, session: Session = Depends(get_session)):
    user = authenticate_user(user_login, session, response)

    return user
