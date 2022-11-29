from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento


Base = declarative_base()

class Reporte(Base):
    __tablename__= 'reporte'

    id_reporte = Column(String(50), primary_key=True)
    tipo = Column(String(40))
    autor = Column(String(50), ForeignKey(Usuario.id_usuario))
    razon_reporte = Column(Text)
    moderador = Column(String(50), ForeignKey(Usuario.id_usuario))
    resultado_moderacion = Column(String(20))
    id_elemento = Column(String(50), ForeignKey(Elemento.id_elemento))
    estado = Column(String(20))

    def __init__(self,id_reporte,tipo,autor,razon_reporte,moderador,resultado_moderacion,id_elemento,estado):
        self.id_reporte = id_reporte
        self.tipo = tipo
        self.autor = autor
        self.razon_reporte = razon_reporte
        self.moderador = moderador
        self.resultado_moderacion =  resultado_moderacion
        self.id_elemento = id_elemento
        self.estado = estado
