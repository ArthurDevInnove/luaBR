from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from ..schemas.user import UserCreate, UserLogin
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models.user import UserModel
from ..utils.security.hasher import hash_password, check_password
from ..utils.security.token_manager import create_token
from ..utils.cookies import set_cookie



def get_by_email(email: str, session: Session) -> UserModel:
    user = session.query(UserModel).filter(UserModel.email == email).first() 
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Usuário não encontrado.'
            )
    return user
    

def get_by_password(password: str, session: Session):
    try:
        user = session.query(UserModel).filter(UserModel.password == password).first()
        if not user:
            raise HTTPException(status_code=404, detail='Credenciais inválidas.')
        return user
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail='Erro interno.')

def insert_user(user: UserCreate, session: Session) -> UserModel:
    try:
        user.password = hash_password(user.password)
        db_user = UserModel(
            **user.model_dump()
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    
    except IntegrityError as e:
        session.rollback()
        error_message = str(e.orig)

        if "email" in error_message:
            raise HTTPException(status_code=409, detail='Email em uso!')
        elif "name" in error_message:
            raise HTTPException(status_code=409, detail='Nome de usuário em uso!')
        else:
            raise HTTPException(status_code=409, detail='Violação de restrição única!')
    
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f'Erro interno. {str(e)}')
    
    finally:
        session.close()

def authenticate_user(user_login: UserLogin, session: Session, response: Response) -> UserModel:
    user = get_by_email(user_login.email, session)
    if not check_password(user_login.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciais inválidas.'
        )
    
    token = create_token(user.id)
    set_cookie(
        response, 'token_jwt', token
    )
    return user