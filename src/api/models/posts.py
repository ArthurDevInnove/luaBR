from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..infra.db.base import Base

class PostsModel(Base):
    __tablename__ = 'posts_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(90), nullable=False)
    content = Column(Text(20000), nullable=False)
    post_hour = Column(DateTime, nullable=False)
    author = Column(ForeignKey('user_model.id'), nullable=False)
    author_name = Column(String(20), nullable=False)
    
    author_reference = relationship('UserModel', backref='posts', lazy=True)