import jwt
import datetime
from dotenv import load_dotenv
from os import getenv

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")


def create_token(user_id):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    payload = {"sub": str(user_id), "exp": expiration_time}
    token = jwt.encode(payload, f"{SECRET_KEY}", algorithm="HS256")

    return token


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = int(payload.get("sub"))

        return user_id
    except Exception as e:
        raise e


def validate_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"token_status": "valid", "payload": payload}
    except jwt.ExpiredSignatureError:
        return {"token_status": "invalid", "message": "Assinatura expirada."}
    except jwt.InvalidSignatureError:
        return {"token_status": "invalid", "message": "Assinatura inválida."}
