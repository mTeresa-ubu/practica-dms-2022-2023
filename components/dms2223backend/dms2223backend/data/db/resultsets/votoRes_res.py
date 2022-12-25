from typing import List, Dict, Optional
from dms2223backend.data.db.results import VotoRes

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class VotoResFuncs():

    @staticmethod
    def create(session:Session, username: str,aid: int) -> VotoRes: #Estaba mal, mirar desde el spec lo que necesitamos
       
        if not aid:
            raise ValueError('Id voto respuesta vacío.')
       
        nueva = VotoRes(username, aid) #En el orden del result

        session.add(nueva)
        session.commit()
        return nueva
        
    @staticmethod
    def get_votoRes(session:Session,aid:int) -> VotoRes:
        stmt = session.query(VotoRes).where(VotoRes.aid == aid).first()
        return stmt

    @staticmethod
    def list_all(session: Session) -> List[VotoRes]:
       
        stmt = session.query(VotoRes).all()
        return stmt

    

    