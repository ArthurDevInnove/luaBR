from ..security.token_manager import decode_token
from ..cookies import get_cookies
from fastapi import Request

def check_current_user(request: Request):
    cookie = get_cookies(request, 'token_jwt')
    user_id = decode_token(cookie)

    return user_id