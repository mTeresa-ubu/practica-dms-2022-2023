from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento
from dms2223backend.data.db.Elemento.respuesta import Respuesta
from dms2223backend.data.db.Feedback.feedback import Feedback


class Comentario(Elemento):
    __tablename__='comentario'

    id_respuesta = Column(Integer, ForeignKey("elemento.id_elemento") ,primary_key=True)
    feedback = Column(Integer,ForeignKey("feedback.id_feedback"))

    __mapper_args__ = {
        "polymorphic_identity": "comentario",
    }