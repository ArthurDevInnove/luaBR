from fastapi import APIRouter
from ..schemas.user import UserSchema
from ..models.user import USER_MODEL

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/register')
async def register_user(user: UserSchema):
    id = len(USER_MODEL) + 1
    USER_MODEL[id] = user

    return {'add_user': user}
