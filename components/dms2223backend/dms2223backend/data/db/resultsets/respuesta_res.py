from typing import List, Dict, Optional

from dms2223backend.data.db.results import Respuesta

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class RespuestaFuncs():

    @staticmethod
    def create(session:Session,username: str, body: Dict,qid:int) -> Respuesta: 
        if not body:
            raise ValueError('Campo contenido vacío.')
        nueva = Respuesta(username=username,body=body,qid=qid) 
        session.add(nueva)
        session.commit()
        return nueva
        
    @staticmethod
    def get_respuesta(session:Session,id:int) -> bool:
        respuesta = session.query(Respuesta).where(Respuesta.id == id).first()
        return respuesta

    @staticmethod
    def list_all(session: Session,qid:int) -> List[Dict]:
        respuestas = session.query(Respuesta).where(Respuesta.qid == qid).all()
        return respuestas

    

    