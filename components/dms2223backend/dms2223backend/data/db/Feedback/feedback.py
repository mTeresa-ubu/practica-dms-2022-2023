from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento

Base = declarative_base()

class Feedback(Base):
    __tablename__='feedback'

    id_feedback = Column(Integer, primary_key=True)
    descripcion = Column(Text)
    color_asociado = Column(String(100))
