import enum
from sqlalchemy import Column,String,Text,Boolean,DateTime, \
    ForeignKey, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento
from dms2223backend.data.db.Elemento.pregunta import Pregunta
from dms2223backend.data.db.Elemento.respuesta import Respuesta
from dms2223backend.data.db.Elemento.comentario import Comentario
from ..base import Base #Base declarativa
from sqlalchemy.orm import relationship

class estado_moderacion(enum.Enum):
    pendiente = 0
    aceptado = 1
    rechazado = 2
    descartado = 3 # Ni se ha leido

class Reporte(Base):
    __tablename__= 'reporte'

    id_reporte = Column(Integer, primary_key=True)
    id_autor = Column(Integer, ForeignKey("usuario.id_usuario"))
    moderador = Column(Integer , ForeignKey("usuario.id_usuario"))
    
    autor = relationship("Usuario",
        back_populates="reportes",
        primaryjoin="Reporte.id_autor == Usuario.id_usuario")

    tipo = Column(String(100))
    razon_reporte = Column(Text)
    resultado_moderacion = Column(String(100))  
    estado = Column(Enum(estado_moderacion), default=estado_moderacion.pendiente)

    def __init__(
        self,
        autor:Usuario,
        tipo:str,
        razon:str
        ):
        self.autor = autor
        self.elemento = Elemento
        self.tipo = tipo
        self.razon = razon

class ReportePregunta(Reporte):
    id_pregunta = Column(Integer, ForeignKey("pregunta.id_pregunta"))
    pregunta = relationship("Pregunta",
        back_populates="reportes")
    
    def __init__(
        self,
        autor:Usuario,
        tipo:str,
        razon:str,
        pregunta: Pregunta
        ):
        self.autor = autor
        self.elemento = Elemento
        self.tipo = tipo
        self.razon = razon
        self.pregunta = pregunta

class ReporteRespuesta(Reporte):
    id_respuesta = Column(Integer, ForeignKey("respuesta.id_respuesta"))
    pregunta = relationship("Pregunta",
        back_populates="reportes")
    
    def __init__(
        self,
        autor:Usuario,
        tipo:str,
        razon:str,
        respuesta: Respuesta
        ):
        self.autor = autor
        self.elemento = Elemento
        self.tipo = tipo
        self.razon = razon
        self.respuesta = respuesta

class ReporteComentario(Reporte):
    id_comentario = Column(Integer, ForeignKey("comentario.id_comentario"))
    pregunta = relationship("Pregunta",
        back_populates="reportes")
    
    def __init__(
        self,
        autor:Usuario,
        tipo:str,
        razon:str,
        comentario: Comentario
        ):
        self.autor = autor
        self.elemento = Elemento
        self.tipo = tipo
        self.razon = razon
        self.comentario = comentario
    