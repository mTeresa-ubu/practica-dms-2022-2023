from sqlalchemy import Column,String,Text,Boolean,DateTime,ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dms2223backend.data.db.Usuario.usuario import Usuario
from dms2223backend.data.db.Elemento.elemento import Elemento
from dms2223backend.data.db.Elemento.respuesta import Respuesta
from dms2223backend.data.db.Feedback.feedback import Feedback


class Comentario(Elemento):
    __tablename__='comentario'

    id_comentario= Column(Integer, ForeignKey("elemento.id_elemento") ,primary_key=True)
    id_respuesta = Column(Integer, ForeignKey("respuesta.id_respuesta"))
    feedback = Column(Integer,ForeignKey("feedback.id_feedback"))

    __mapper_args__ = {
        "polymorphic_identity": "comentario",
    }

    def __init__(self,
        contenido:str,
        fecha:datetime,
        autor:int,
        visibilidad:bool,
        feedback:int
        ):
        super().__init__(contenido=contenido,fecha=fecha,autor=autor,visibilidad=visibilidad)
        self.feedback = feedback

    def __repr__(self) -> str:        
        return  f"Comentario(id_comentario={self.id_comentario!r}, \
        contenido={self.contenido!r}, \
        fecha={self.fecha!r}, \
        autor={self.autor!r},\
        visibilidad={str(self.visibilidad)!r} \
        feedback={self.feedback} \
        )"