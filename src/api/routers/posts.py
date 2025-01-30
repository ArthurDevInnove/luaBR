from fastapi import APIRouter, Depends, Request
from ..infra.db.session import get_session
from ..schemas.posts import PostsCreate, PostsEdit
from sqlalchemy.orm import Session
from ..services.posts import create_post, list_posts, edit_post, delete_post

posts_router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@posts_router.get('/show')
async def show(session: Session = Depends(get_session)):
    posts = list_posts(session)

    return posts

@posts_router.post('/create')
async def create(post: PostsCreate, request: Request, session: Session = Depends(get_session)):
    post_db = create_post(post, request, session)

    return post_db

@posts_router.put('/edit/{post_id}')
async def edit(post_id: int, new_post: PostsEdit, session: Session = Depends(get_session)):
    post = edit_post(post_id, new_post, session)
    return post

@posts_router.delete('/delete/{post_id}')
async def delete(post_id: int, session: Session = Depends(get_session)):
    delete_post(post_id, session)