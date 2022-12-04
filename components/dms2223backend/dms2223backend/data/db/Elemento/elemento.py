from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey,Integer
from sqlalchemy.ext.declarative import declarative_base
from dms2223backend.data.db.Usuario.usuario import Usuario
from ..base import Base #Base declarativa

from datetime import datetime

class Elemento(Base):
    __tablename__ = 'elemento'

    id_elemento = Column(Integer, primary_key=True)
    fecha = Column(DateTime)
    autor = Column(Integer, ForeignKey(Usuario.id_usuario))
    contenido = Column(Text)
    visibilidad = Column(Boolean) #En caso de true es visible en caso de false esta oculto
    type = Column(String(50)) #Especifica el tipo de elemento que es

    __mapper_args__ = {
        "polymorphic_identity": "elemento",
        "polymorphic_on": type,
    }

    def __init__(self,
        contenido:str,
        fecha:datetime,
        autor:int,
        visibilidad:bool
        ):
        self.contenido = contenido
        self.fecha = fecha
        self.autor = autor
        self.visibilidad = visibilidad