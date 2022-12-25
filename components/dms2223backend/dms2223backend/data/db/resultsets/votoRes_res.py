from typing import List, Dict, Optional
from dms2223backend.data.db.results import Voto

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class VotoResFuncs():

    @staticmethod
    def create(session:Session,eid: int, tipo: str) -> Voto:
       
        nueva = Voto(eid, tipo='respuesta') 

        session.add(nueva)
        session.commit()
        return nueva
        
    @staticmethod
    def get_pregunta(session:Session,eid:int) -> Voto:
        stmt = session.query(Voto).where(Voto.eid == eid).first()
        return stmt

    @staticmethod
    def list_all(session: Session,eid:int) -> List[Voto]:
        stmt = session.query(Voto).where(Voto.eid == eid).all()
        return stmt

    

    