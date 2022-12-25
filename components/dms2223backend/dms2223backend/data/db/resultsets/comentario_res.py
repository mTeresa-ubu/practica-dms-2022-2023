from typing import List, Dict, Optional

from dms2223backend.data.db.results import Comentario
from dms2223backend.data.sentiment import  Sentiment

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class ComentarioFuncs():

    @staticmethod
    def create(session:Session, username: str, body: str, aid: int, sentiment: Sentiment) -> Comentario: 
        if not body:
            raise ValueError('Campo contenido vacío.')
        if not sentiment:
            raise ValueError('Campo sentimiento vacío.')

        nueva = Comentario(username,body,aid, sentiment, oculto=False) 
        

        session.add(nueva)
        session.commit()
        return nueva
        
    @staticmethod
    def get_comentario(session:Session,aid:int) -> Comentario:
        stmt = session.query(Comentario).where(Comentario.aid == aid).first()
        return stmt

    @staticmethod
    def list_all(session: Session,aid:int) -> List[Dict]:
        stmt = session.query(Comentario).where(Comentario.aid == aid).all()
        return stmt

    

    