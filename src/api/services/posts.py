from fastapi import HTTPException, status, Request
from ..schemas.posts import PostsCreate
from ..utils.cookies import get_cookies
from ..models.posts import PostsModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..utils.security.token_manager import decode_token

def create_post(post: PostsCreate, request: Request, session: Session) -> PostsModel:
    try:
        token_cookie = get_cookies(request, 'token_jwt')
        if not token_cookie:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='O token de autentificação do usuário não foi encontrado.'
            )
        
        user_id = decode_token(str(token_cookie))
        db_post = PostsModel(
            title=post.title,
            content=post.content,
            post_hour=post.hour,
            author=user_id
        )

        session.add(db_post)
        session.commit()
        session.refresh(db_post)

        return db_post
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Houve um erro interno no servidor.'
        )

def list_posts(session: Session):
    try:
        posts = session.query(PostsModel).all()
        if not posts:
            return []
        
        return posts
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Houve um erro interno no servidor.'
        )