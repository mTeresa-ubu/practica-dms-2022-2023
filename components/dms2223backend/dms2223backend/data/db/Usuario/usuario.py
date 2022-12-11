from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer
from ..base import Base #Base declarativa
from sqlalchemy.orm import relationship

class Usuario(Base):
    
    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(50) ,nullable=False, unique=True)
    preguntas = relationship('Pregunta', back_populates="autor")

    def __init__(self,nombre:str):
        self.nombre = nombre