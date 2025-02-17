from fastapi import Response, Request

def set_cookie(response: Response, key: str, value: str, max_age: int = 1209600):
    r = response.set_cookie(
        key=key,
        value=value,
        max_age=max_age,
        httponly=False,
        secure=False,
        samesite="Lax",
    )

    return r

def get_cookies(request: Request, key: str):
    cookie = request.cookies.get(key)
    if not cookie:
        return None
    return cookie