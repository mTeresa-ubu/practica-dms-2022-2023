from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey,Integer
from sqlalchemy.ext.declarative import declarative_base
from dms2223backend.data.db.Usuario.usuario import Usuario

Base = declarative_base()

class Elemento(Base):
    __tablename__ = 'elemento'

    id_elemento = Column(Integer, primary_key=True)
    fecha = Column(DateTime)
    autor = Column(Integer, ForeignKey(Usuario.id_usuario))
    contenido = Column(Text)
    visibilidad = Column(Boolean) #En caso de true es visible en caso de false esta oculto

    __mapper_args__ = {
        "polymorphic_identity": "elemento",
        "polymorphic_on": type,
    }