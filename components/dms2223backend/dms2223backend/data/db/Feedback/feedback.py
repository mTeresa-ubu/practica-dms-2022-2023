from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento

Base = declarative_base()

class Feedback(Base):
    __tablename__='feedback'

    id_feedback = Column(String(50), primary_key=True)
    id_elemento = Column(String(50), ForeignKey(Elemento.id_elemento))
    descripcion = Column(Text)
    color_asociado = Column(String(15))#Rojo o verde o blanco

    def __init__(self,id_feedback,id_elemento,descripcion,color_asociado):
        self.id_feedback = id_feedback
        self.id_elemento = id_elemento
        self.descripcion = descripcion
        self.color_asociado = color_asociado