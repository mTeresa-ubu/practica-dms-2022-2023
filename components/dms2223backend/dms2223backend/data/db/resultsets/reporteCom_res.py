from typing import List, Dict, Optional
from dms2223backend.data.db.results import ReporteCom
from dms2223backend.data.reportstatus import ReportStatus

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class ReporteComFuncs():

    @staticmethod
    def create(session:Session, username: str, reason: str, cid: int) -> ReporteCom:
        if not reason:
            raise ValueError('Campo razón vacío.')
        if not cid:
            raise ValueError('Id reporte comentario vacío.')
       
        nueva = ReporteCom(username, reason, cid, ReportStatus.PENDING)

        session.add(nueva)
        session.commit()
        return nueva
        
    @staticmethod
    def get_reporteCom(session:Session, crid:int) -> ReporteCom:
        stmt = session.query(ReporteCom).where(ReporteCom.id == crid).first()
        return stmt

    @staticmethod
    def list_all(session: Session) -> List[ReporteCom]:
       
        stmt = session.query(ReporteCom).all()
        return stmt

    

    