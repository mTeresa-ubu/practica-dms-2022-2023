from typing import List
from dms2223backend.data.db.results import Comentario
from dms2223backend.data.sentiment import  Sentiment
from sqlalchemy.orm.session import Session  # type: ignore

class ComentarioFuncs():

    @staticmethod
    def create(session:Session, username: str, body: str, aid: int, sentiment: Sentiment) -> Comentario: 
        if not body:
            raise ValueError('Campo contenido vacío.')

        nuevo = Comentario(username, body, aid, sentiment) 
        session.add(nuevo)
        session.commit()

        return nuevo


    @staticmethod
    def get_comentario(session:Session, id:int) -> Comentario:

        comentario = session.query(Comentario).where(Comentario.id == id).first()

        return comentario


    @staticmethod
    def list_all(session: Session,aid:int) -> List[Comentario]:

        comentarios = session.query(Comentario).where(Comentario.aid == aid).all()

        return comentarios

    

    