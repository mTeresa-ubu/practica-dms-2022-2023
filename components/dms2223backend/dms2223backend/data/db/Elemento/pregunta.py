from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento

Base = declarative_base()

class Pregunta(Base):
    __tablename__='pregunta'

    id_pregunta = Column(String(50), primary_key=True)
    id_elemento = Column(String(50), ForeignKey(Elemento.id_elemento))
    titulo = Column(String(100))

    def __init__(self,id_pregunta,id_elemento,titulo):
        self.id_pregunta = id_pregunta
        self.id_elemento = id_elemento
        self.titulo = titulo
    
