from typing import List, Dict, Optional
from dms2223backend.data.db.results import VotoCom

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class VotoComFuncs():

    @staticmethod
    def create(session:Session, username: str,aid: int) -> VotoCom: #Estaba mal, mirar desde el spec lo que necesitamos
       
        if not aid:
            raise ValueError('Id voto comentario vacío.')
       
        nueva = VotoCom(username, aid) #En el orden del result

        session.add(nueva)
        session.commit()
        return nueva
        
    @staticmethod
    def get_votoCom(session:Session,aid:int) -> VotoCom:
        stmt = session.query(VotoCom).where(VotoCom.aid == aid).first()
        return stmt

    @staticmethod
    def list_all(session: Session) -> List[VotoCom]:
       
        stmt = session.query(VotoCom).all()
        return stmt

    

    