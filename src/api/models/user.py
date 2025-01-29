from sqlalchemy import Column, Integer, String, Text
from ..infra.db.base import Base

class UserModel(Base):
    __tablename__ = 'user_model'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    description = Column(Text(700), nullable=True)