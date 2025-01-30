from fastapi import APIRouter, Depends, Request
from ..infra.db.session import get_session
from ..schemas.posts import PostsCreate
from sqlalchemy.orm import Session
from ..services.posts import create_post, list_posts

posts_router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@posts_router.post('/create')
async def create(post: PostsCreate, request: Request, session: Session = Depends(get_session)):
    post_db = create_post(post, request, session)

    return post_db

@posts_router.get('/show')
async def show(session: Session = Depends(get_session)):
    posts = list_posts(session)

    return posts