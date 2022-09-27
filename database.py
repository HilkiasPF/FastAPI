from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base


engine = create_engine("sqlite:///./data.db", echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    nome: str = Column(String(50))
    age: int = Column(Integer)

Base.metadata.create_all(engine)