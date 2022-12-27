from typing import List, Dict
from dms2223backend.data.db import Schema
from sqlalchemy.orm.session import Session  # type: ignore

from dms2223backend.data.db.resultsets.reporteCom_res import ReporteComFuncs
from dms2223backend.data.db.resultsets.reportePreg_res import ReportePregFuncs
from dms2223backend.data.db.resultsets.reporteRes_res import ReporteResFuncs

from sqlalchemy import select

#Rober Lastras

class ServicioReporte(): 

    def list_reportsCom(schema:Schema) -> List:
        '''Devuelve una lista de los reportes de comentarios
        '''
        session: Session = schema.new_session()
        reportes = ReporteComFuncs.list_all(session)
        schema.remove_session()

        return reportes
    
    @staticmethod
    def create_reportCom(schema:Schema, username: str, reason: str, aid: int) -> Dict:
        """Crea un reporte de comentario con los parametros pasados y devuelve un diccionario con el reporte en cuestión.
        """
        #Creamos una sesion
        session: Session = schema.new_session()
        
        rep = ReporteComFuncs.create(session, username, reason, aid)
        rep:Dict = {
            "qid":rep.qid,
            "reason":rep.reason,
            "timestamp":rep.timestamp,
            "aid":rep.aid,
            "owner":{"username":rep.username}
        }

        #Cerramos la sesion
        schema.remove_session() 

        return rep
    
    '''
    @staticmethod
    def get_reportCom(schema:Schema, aid:int) -> Dict:
        """Obtiene los datos de un reporte se debe usar para la visualizacion
            en lista de reporte, no contiene los votos de las respuestas 
        """
        session: Session = schema.new_session()

        rep = ReporteComFuncs.create(session, aid)
        rep:Dict = {
            "qid":rep.qid,
            "reason":rep.reason,
            "timestamp":rep.timestamp,
            "aid":rep.aid,
            "owner":{"username":rep.username}
        }

        schema.remove_session()
        return rep
    '''
    
    def list_reportsPreg(schema:Schema) -> List:
        '''Devuelve una lista de los reportes de preguntas
        '''
        session: Session = schema.new_session()
        reportes = ReportePregFuncs.list_all(session)
        schema.remove_session()

        return reportes
    
    @staticmethod
    def create_reportPreg(schema:Schema, username: str, reason: str, aid: int) -> Dict:
        """Crea un reporte de pregunta con los parametros pasados y devuelve un diccionario con el reporte en cuestión.
        """
        #Creamos una sesion
        session: Session = schema.new_session()
        
        rep = ReportePregFuncs.create(session, username, reason, aid)
        rep:Dict = {
            "qid":rep.qid,
            "reason":rep.reason,
            "timestamp":rep.timestamp,
            "aid":rep.aid,
            "owner":{"username":rep.username}
        }

        #Cerramos la sesion
        schema.remove_session() 

        return rep
    
    def list_reportsRes(schema:Schema) -> List:
        '''Devuelve una lista de los reportes de respuestas
        '''
        session: Session = schema.new_session()
        reportes = ReporteResFuncs.list_all(session)
        schema.remove_session()

        return reportes
    
    @staticmethod
    def create_reportRes(schema:Schema, username: str, reason: str, aid: int) -> Dict:
        """Crea un reporte de respuesta con los parametros pasados y devuelve un diccionario con el reporte en cuestión.
        """
        #Creamos una sesion
        session: Session = schema.new_session()
        
        rep = ReporteResFuncs.create(session, username, reason, aid)
        rep:Dict = {
            "qid":rep.qid,
            "reason":rep.reason,
            "timestamp":rep.timestamp,
            "aid":rep.aid,
            "owner":{"username":rep.username}
        }

        #Cerramos la sesion
        schema.remove_session() 

        return rep