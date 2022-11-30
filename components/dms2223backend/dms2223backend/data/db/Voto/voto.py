import enum
from sqlalchemy import Column,String,Text,Boolean,DateTime, \
    ForeignKey,Integer,Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento
from ..base import Base #Base declarativa

class tipo_voto(enum.Enum):
    positivo = 1
    negativo = 0

class Voto(Base):
    __tablename__ = 'voto'

    id_voto = Column(Integer, primary_key=True)
    id_elemento = Column(Integer, ForeignKey("elemento.id_elemento"))
    autor = Column(Integer, ForeignKey("elemento.id_usuario"))

    tipo = Column(Enum(tipo_voto))


