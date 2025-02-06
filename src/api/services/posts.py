from fastapi import HTTPException, status, Request
from ..schemas.posts import PostsCreate, PostsEdit
from ..utils.cookies import get_cookies
from ..models.posts import PostsModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..utils.security.token_manager import decode_token
from ..utils.check_owner import check_owner
from .user import get_by_id

def get_post_by_id(id: int, session: Session) -> PostsModel:
    try:
        post = session.query(PostsModel).filter(PostsModel.id == id).first()
        if not post:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Post não encontrado.'
            )
        return post
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Houve um erro interno no servidor.'
        )

def create_post(post: PostsCreate, request: Request, session: Session) -> PostsModel:
    try:
        token_cookie = get_cookies(request, 'token_jwt')
        if not token_cookie:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='O token de autentificação do usuário não foi encontrado.'
            )
        
        
        user_id = decode_token(str(token_cookie))
        author = get_by_id(user_id, session)

        db_post = PostsModel(
            title=post.title,
            content=post.content,
            post_hour=post.hour,
            author=user_id,
            author_name=author.name
        )

        session.add(db_post)
        session.commit()
        session.refresh(db_post)

        return db_post
    
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Houve um erro interno no servidor.'
        )
    
    finally:
        session.close()
    
def edit_post(post_id: int, new_post: PostsEdit, session: Session, user_id: int):
    try:
        db_post = get_post_by_id(post_id, session)
        check_owner(db_post.author, user_id)
        db_post.title = new_post.title
        db_post.content = new_post.content

        session.commit()
        return db_post
    
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Houve um erro interno no servidor.'
        )
    
    finally:
        session.close()

def delete_post(post_id: int, session: Session, user_id: int):
    try:
        post = get_post_by_id(post_id, session)
        check_owner(post.author, user_id)

        session.delete(post)
        session.commit()

    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Houve um erro interno no servidor.'
        )
    
    finally:
        session.close()


def list_posts(session: Session):
    try:
        posts = session.query(PostsModel).all() 
        if not posts:
            return []
        
        return posts
    
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Houve um erro interno no servidor.'
        )