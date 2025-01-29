from fastapi import APIRouter
from ..schemas.user import UserSchema

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/register')
async def register_user(user: UserSchema):
    return {'add_user': user}
