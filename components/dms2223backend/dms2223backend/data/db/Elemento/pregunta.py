from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey,Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento

Base = declarative_base()

class Pregunta(Elemento):
    __tablename__='pregunta'
    id_pregunta = Column(Integer, ForeignKey("elemento.id_elemento") ,primary_key=True)
    titulo = Column(String(200))

    __mapper_args__ = {
        "polymorphic_identity": "pregunta",
    }