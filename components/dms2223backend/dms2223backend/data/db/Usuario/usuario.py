from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column
 
Base = declarative_base()

class Usuario(Base):
    
    __tablename__ = 'usuario'

    id_usuario = Column(String(50), primary_key=True)
    nombre = Column(String(50) ,nullable=False ,unique=True)

    def __init__(self,id_usuario,nombre):
        self.id_usuario=id_usuario
        self.nombre= nombre
