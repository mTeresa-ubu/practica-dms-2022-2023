import enum
from sqlalchemy import Column,String,Text,Boolean,DateTime, \
    ForeignKey, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento
from ..base import Base #Base declarativa

class estado_moderacion(enum.Enum):
    pendiente = 0
    aceptado = 1
    rechazado = 2
    descartado = 3 # Ni se ha leido

class Reporte(Base):
    __tablename__= 'reporte'

    id_reporte = Column(Integer, primary_key=True)
    autor = Column(Integer, ForeignKey("usuario.id_usuario"))
    moderador = Column(Integer , ForeignKey("usuario.id_usuario"))
    id_elemento = Column(Integer, ForeignKey("elemento.id_elemento"))
    
    tipo = Column(String(100))
    razon_reporte = Column(Text)
    resultado_moderacion = Column(String(100))  
    estado = Column(Enum(estado_moderacion), default=estado_moderacion.pendiente)
