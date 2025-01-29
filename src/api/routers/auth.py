from fastapi import APIRouter, Depends
from ..infra.db.session import get_session
from ..services.user import insert_user
from ..schemas.user import UserSchema
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/register')
async def register_user(user: UserSchema, session: Session = Depends(get_session)):
    insert_user(user, session)

    return UserSchema(
        **user.__dict__
    )
