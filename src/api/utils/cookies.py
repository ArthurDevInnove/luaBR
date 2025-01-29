from fastapi import Response

def set_cookie(response: Response, key: str, value: str, max_age: int = 1209600):
    response.set_cookie(
        key=key,
        value=value,
        max_age=max_age,
        httponly=True,
        secure=True,
        samesite="Lax"
    )