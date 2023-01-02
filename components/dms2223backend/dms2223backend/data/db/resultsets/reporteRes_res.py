from typing import List, Dict, Optional
from dms2223backend.data.db.results import ReporteRes
from dms2223backend.data.reportstatus import ReportStatus

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class ReporteResFuncs():

    @staticmethod
    def create(session:Session, username: str, reason: str, aid: int) -> ReporteRes: #Estaba mal, mirar desde el spec lo que necesitamos
        if not reason:
            raise ValueError('Campo razón vacío.')
        if not aid:
            raise ValueError('Id reporte comentario vacío.')
       
        nueva = ReporteRes(username, reason, aid, ReportStatus.PENDING) #En el orden del result

        session.add(nueva)
        session.commit()
        return nueva
        
    @staticmethod
    def get_reporteRes(session:Session, arid:int) -> ReporteRes:
        stmt = session.query(ReporteRes).where(ReporteRes.id == arid).first()
        return stmt

    @staticmethod
    def list_all(session: Session) -> List[ReporteRes]:
       
        stmt = session.query(ReporteRes).all()
        return stmt

    

    