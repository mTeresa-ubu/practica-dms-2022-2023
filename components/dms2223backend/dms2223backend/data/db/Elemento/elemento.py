from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario

Base = declarative_base()

class Elemento(Base):
    __tablename__ = 'elemento'

    id_elemento = Column(String(50), primary_key=True)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
    autor = Column(String(50), ForeignKey(Usuario.id_usuario))
    contenido = Column(Text)
    visibilidad = Column(Boolean)#En caso de true es visible en caso de false esta oculto
    def __init__(self,id_elemento,fecha,autor,contenido,visibilidad):
        self.id_elemento = id_elemento
        self.fecha = fecha
        self.autor = autor
        self.contenido = contenido
        self.visibilidad = visibilidad