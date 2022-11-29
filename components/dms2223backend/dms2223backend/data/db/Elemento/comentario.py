from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento
from dms2223backend.data.db.Elemento.respuesta import Respuesta
from dms2223backend.data.db.Feedback.feedback import Feedback

Base = declarative_base()

class Comentario(Base):
    __tablename__='comentario'

    id_comentario = Column(String(50), primary_key=True)
    id_elemento = Column(String(50), ForeignKey(Elemento.id_elemento))
    feedback = Column(String(50),ForeignKey(Feedback.id_feedback))
    id_respuesta = Column(String(50), ForeignKey(Respuesta.id_respuesta))

    def __init__(self,id_comentario,id_elemento,feedback,id_respuesta):
        self.id_comentario = id_comentario
        self.id_elemento = id_elemento
        self.feedback = feedback
        self.id_respuesta = id_respuesta