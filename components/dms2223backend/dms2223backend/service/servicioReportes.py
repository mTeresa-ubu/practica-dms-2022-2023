from typing import List, Dict
from dms2223backend.data.db import Schema
from sqlalchemy.orm.session import Session  # type: ignore

from dms2223backend.data.db.resultsets.reporteCom_res import ReporteComFuncs
from dms2223backend.data.db.resultsets.reportePreg_res import ReportePregFuncs
from dms2223backend.data.db.resultsets.reporteRes_res import ReporteResFuncs
from dms2223backend.data.reportstatus import ReportStatus
from dms2223backend.service.serviciopreguntas import PreguntasServicio
from dms2223backend.service.servicioComentario import servicioComentario
from dms2223backend.service.servicioRespuestas import ServicioRespuestas

#Rober Lastras

class ServicioReporte():

    # Reportes para comentarios

    def list_reportsCom(schema:Schema) -> List:
        '''Devuelve una lista con los datos de los reportes de comentarios
        '''
        session: Session = schema.new_session() #Creamos una sesion
        reports = ReporteComFuncs.list_all(session)

        list_rep: List = []
        for rep in reports:
            list_rep.append(
                {
                "id":rep.id,
                "cid":rep.cid,
                "reason":rep.reason,
                #"timestamp":rep.timestamp,
                'status': rep.status.name,
                "owner":{"username":rep.username}
                }
            )

        schema.remove_session() #Cerramos la sesion

        return list_rep
    
    @staticmethod
    def create_reportCom(schema:Schema, username: str, reason: str, cid: int) -> Dict:
        """Crea un reporte de comentario con los parametros pasados y devuelve un diccionario con el reporte en cuestión.
        """
        session: Session = schema.new_session()
        
        rep = ReporteComFuncs.create(session, username, reason, cid)
        rep:Dict = {
            "id":rep.id,
            "cid":rep.cid,
            "reason":rep.reason,
            #"timestamp":rep.timestamp,
            'status': rep.status.name,
            "owner":{"username":rep.username}
        }

        schema.remove_session() 
        return rep
    
    @staticmethod
    def get_reportCom(schema:Schema, crid:int) -> Dict:
        """Devuelve los datos de un reporte de comentario
        """
        session: Session = schema.new_session()

        rep = ReporteComFuncs.get_reporteCom(session, crid)
        rep:Dict = {
            "id":rep.id,
            "cid":rep.cid,
            "reason":rep.reason,
            #"timestamp":rep.timestamp,
            'status': rep.status.name,
            "owner":{"username":rep.username}
        }

        schema.remove_session()
        return rep
    
    @staticmethod
    def change_status_reportCom(schema: Schema, crid: int, status: str):
        """Cambia el estado de un reporte de comentario
        """
        session: Session = schema.new_session()

        rep: ReporteComFuncs = ReporteComFuncs.get_reporteCom(session, crid)

        rep.status = ReportStatus[status]
        if status == 'ACCEPTED':
            servicioComentario.ocultarCom(schema, rep.cid)

        session.add(rep)
        session.commit()

        schema.remove_session()


    # Reportes para preguntas
    
    def list_reportsPreg(schema:Schema) -> List:
        '''Devuelve una lista con los datos de los reportes de preguntas
        '''
        session: Session = schema.new_session()
        reports = ReportePregFuncs.list_all(session)

        list_rep: List = []
        for rep in reports:
            list_rep.append(
                {
                "id":rep.id,
                "qid":rep.qid,
                "reason":rep.reason,
                #"timestamp":rep.timestamp,
                'status': rep.status.name,
                "owner":{"username":rep.username}
                }
            )

        schema.remove_session()

        return list_rep
    
    @staticmethod
    def create_reportPreg(schema:Schema, username: str, reason: str, qid: int) -> Dict:
        """Crea un reporte de pregunta con los parametros pasados y devuelve un diccionario con el reporte en cuestión.
        """
        session: Session = schema.new_session()
        
        rep = ReportePregFuncs.create(session, username, reason, qid)
        rep:Dict = {
            "id":rep.id,
            "qid":rep.qid,
            "reason":rep.reason,
            #"timestamp":rep.timestamp,
            'status': rep.status.name,
            "owner":{"username":rep.username}
        }

        schema.remove_session() 
        return rep

    @staticmethod
    def get_reportPreg(schema:Schema, qrid:int) -> Dict:
        """Devuelve los datos de un reporte de pregunta
        """
        session: Session = schema.new_session()

        rep = ReportePregFuncs.get_reportePreg(session, qrid)
        rep:Dict = {
            "id":rep.id,
            "qid":rep.qid,
            "reason":rep.reason,
            #"timestamp":rep.timestamp,
            'status': rep.status.name,
            "owner":{"username":rep.username}
        }

        schema.remove_session()
        return rep    

    @staticmethod
    def change_status_reportPreg(schema: Schema, qrid: int, status: str):
        """Cambia el estado de un reporte de pregunta
        """
        session: Session = schema.new_session()

        rep: ReportePregFuncs = ReportePregFuncs.get_reportePreg(session, qrid)

        rep.status = ReportStatus[status]
        if status == 'ACCEPTED':
            PreguntasServicio.ocultarPreg(schema, rep.qid)

        session.add(rep)
        session.commit()

        schema.remove_session()


    # Reportes para respuestas

    def list_reportsRes(schema:Schema) -> List:
        '''Devuelve una lista con los datos de los reportes de respuestas
        '''
        session: Session = schema.new_session()
        reports = ReporteResFuncs.list_all(session)
        
        list_rep: List = []
        for rep in reports:
            list_rep.append(
                {
                "id":rep.id,
                "aid":rep.aid,
                "reason":rep.reason,
                #"timestamp":rep.timestamp,
                'status': rep.status.name,
                "owner":{"username":rep.username}
                }
            )

        schema.remove_session()

        return list_rep
    
    @staticmethod
    def create_reportRes(schema:Schema, username: str, reason: str, aid: int) -> Dict:
        """Crea un reporte de respuesta con los parametros pasados y devuelve un diccionario con el reporte en cuestión.
        """
        session: Session = schema.new_session()
        
        rep = ReporteResFuncs.create(session, username, reason, aid)
        rep:Dict = {
            "id":rep.id,
            "aid":rep.aid,
            "reason":rep.reason,
            #"timestamp":rep.timestamp,
            'status': rep.status.name,
            "owner":{"username":rep.username}
        }

        schema.remove_session() 
        return rep

    @staticmethod
    def get_reportRes(schema:Schema, arid:int) -> Dict:
        """Devuelve los datos de un reporte de respuesta
        """
        session: Session = schema.new_session()

        rep = ReporteResFuncs.get_reporteRes(session, arid)
        rep:Dict = {
            "id":rep.id,
            "aid":rep.aid,
            "reason":rep.reason,
            #"timestamp":rep.timestamp,
            'status': rep.status.name,
            "owner":{"username":rep.username}
        }

        schema.remove_session()
        return rep   

    @staticmethod
    def change_status_reportRes(schema: Schema, arid: int, status: str):
        """Cambia el estado de un reporte de respuesta
        """
        session: Session = schema.new_session()

        rep: ReporteResFuncs = ReporteResFuncs.get_reporteRes(session, arid)

        rep.status = ReportStatus[status]
        if status == 'ACCEPTED':
            ServicioRespuestas.ocultarRes(schema, rep.aid)

        session.add(rep)
        session.commit()

        schema.remove_session()