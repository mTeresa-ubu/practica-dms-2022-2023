from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer
from ..base import Base #Base declarativa

class Usuario(Base):
    
    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(50) ,nullable=False)

