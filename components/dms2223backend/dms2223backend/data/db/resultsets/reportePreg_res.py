from typing import List, Dict, Optional
from dms2223backend.data.db.results import ReportePreg
from dms2223backend.data.reportstatus import ReportStatus

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class ReportePregFuncs():

    @staticmethod
    def create(session:Session, username: str, reason: str, aid: int) -> ReportePreg: #Estaba mal, mirar desde el spec lo que necesitamos
        if not reason:
            raise ValueError('Campo razón vacío.')
        if not aid:
            raise ValueError('Id reporte comentario vacío.')
       
        nueva = ReportePreg(username, reason, aid, ReportStatus.PENDING) #En el orden del result

        session.add(nueva)
        session.commit()
        return nueva
        
    @staticmethod
    def get_reportePreg(session:Session,aid:int) -> ReportePreg:
        stmt = session.query(ReportePreg).where(ReportePreg.id == aid).first()
        return stmt

    @staticmethod
    def list_all(session: Session) -> List[ReportePreg]:
       
        stmt = session.query(ReportePreg).all()
        return stmt

    

    