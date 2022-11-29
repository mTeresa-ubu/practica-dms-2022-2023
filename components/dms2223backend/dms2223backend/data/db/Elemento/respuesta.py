from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento


Base = declarative_base()

class Respuesta(Base):
    __tablename__='respuesta'

    id_respuesta = Column(String(50), primary_key=True)
    id_elemento = Column(String(50), ForeignKey(Elemento.id_elemento))

    def __init__(self,id_respuesta,id_elemento):
        self.id_respuesta = id_respuesta
        self.id_elemento = id_elemento
