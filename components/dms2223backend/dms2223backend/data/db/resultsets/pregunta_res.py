from typing import List,Optional
from dms2223backend.data.db.results import Pregunta

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class PreguntaFuncs():

    @staticmethod
    def create(session:Session, body:str, title:str, username: str) -> Pregunta: #Estaba mal, mirar desde el spec lo que necesitamos
        if not title:
            raise ValueError('Campo título vacío.')
        if not body:
            raise ValueError('Campo contenido vacío.')
        nueva = Pregunta(body,title,username,oculto=False) #En el orden del result

        session.add(nueva)
        session.commit()
        return nueva
        
    @staticmethod
    def get_pregunta(session:Session,qid:int) -> Pregunta:
        stmt = session.query(Pregunta).where(Pregunta.qid == qid).first()
        return stmt
        pass

    @staticmethod
    def list_all(session: Session) -> List[dict]:
        stmt = session.query(Pregunta).all()
        return stmt
        pass

    

    