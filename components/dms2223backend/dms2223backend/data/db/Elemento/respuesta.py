from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento


class Respuesta(Elemento):
    __tablename__='respuesta'
    id_respuesta = Column(Integer, ForeignKey("elemento.id_elemento") ,primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "respuesta",
    }