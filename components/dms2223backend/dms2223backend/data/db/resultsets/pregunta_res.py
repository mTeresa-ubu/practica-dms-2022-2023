from typing import List, Dict, Optional
from datetime import datetime

from dms2223backend.data.db.Usuario import Usuario
from dms2223backend.data.db.Elemento import Pregunta, Respuesta, Comentario
from dms2223backend.data.db.Voto import Voto

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class PreguntaFuncs():

    @staticmethod
    def create(session:Session,pregunta:Pregunta) -> Pregunta:
        session.add(pregunta)
        session.commit()
        return pregunta
        
    @staticmethod
    def get_pregunta(session:Session,qid:int) -> Pregunta:
        stmt = session.query(Pregunta).where(Pregunta.id_pregunta == qid).first()
        return stmt

    @staticmethod
    def list_all(max:Optional[int], session: Session) -> List[Dict]:
       
        stmt = session.query(Pregunta).all()
        return stmt

    

    