from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from ..schemas.user import UserSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.user import UserModel


def insert_user(user: UserSchema, session: Session):
    try:
        db_user = UserModel(
            **user.__dict__
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return {'status': 'success'}
    
    except IntegrityError as e:
        session.rollback()

        error_message = str(e.orig)

        if "email" in error_message:
            raise HTTPException(status_code=409, detail='Este email já está em uso.')
        elif "name" in error_message:
            raise HTTPException(status_code=409, detail='Este nome de usuário já está em uso!')
        else:
            raise HTTPException(status_code=409, detail='Violação de restrição única. Verifique os dados informados!')
    
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f'Houve algum erro interno no banco de dados. {str(e)}')
    
    finally:
        session.close()