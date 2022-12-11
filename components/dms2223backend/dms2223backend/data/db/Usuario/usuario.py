from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer
from ..base import Base #Base declarativa
from sqlalchemy.orm import relationship

class Usuario(Base):
    
    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(50) ,nullable=False, unique=True)

    elementos = relationship('Elemento', back_populates="autor")
    preguntas = relationship('Pregunta', primaryjoin="Usuario.id_usuario == Pregunta.id_autor")
    respuestas = relationship('Respuesta',  primaryjoin="Usuario.id_usuario == Respuesta.id_autor")
    comentarios = relationship('Comentario',  primaryjoin="Usuario.id_usuario == Comentario.id_autor")

    reportes = relationship('Reporte',  primaryjoin="Usuario.id_usuario == Reporte.id_autor")

    def __init__(self,nombre:str):
        self.nombre = nombre