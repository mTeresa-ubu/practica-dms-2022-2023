from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento

Base = declarative_base()

class Voto(Base):
    __tablename__ = 'voto'

    id_voto = Column(String(50), primary_key=True)
    tipo = Column(String(40))
    id_elemento = Column(String(50), ForeignKey(Elemento.id_elemento))
    autor = Column(String(50), ForeignKey(Usuario.id_usuario))

    def __init__(self,id_voto,tipo,id_elemento,autor):
        self.id_voto = id_voto
        self.tipo = tipo
        self.id_elemento = id_elemento
        self.autor = autor
