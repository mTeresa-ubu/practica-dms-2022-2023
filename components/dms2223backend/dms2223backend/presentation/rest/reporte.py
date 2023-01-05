"""REST API controllers responsible of handling the server operations about reports
"""
from typing import Dict, Tuple, Optional, List, Union
from http import HTTPStatus
from flask import current_app
from sqlalchemy.orm.session import Session # type: ignore
from dms2223backend.service.servicioReportes import ServicioReporte
from dms2223backend.service.servicioRespuestas import ServicioRespuestas
from dms2223backend.service.servicioComentario import servicioComentario
from dms2223backend.service.serviciopreguntas import PreguntasServicio

# Rober Lastras

# Reportes para comentarios

def list_repCom() -> Tuple[Dict,int]:
    """ Devuelve reportes de comentarios
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.list_reportsCom(current_app.db)
    return (rep, HTTPStatus.OK)

def get_repCom(crid:int) -> Tuple[Dict,int]:
    """ Devuelve un reporte sabiendo el id
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.get_reportCom(current_app.db, crid)
    return (rep, HTTPStatus.OK)

def create_repCom(cid: int, body: Dict, token_info: Dict) -> Tuple[Dict,int]:
    """ Recoge los datos de la peticion y los manda al servicio de reportes (comentarios)
    """
    with current_app.app_context():
        if not servicioComentario.existe_comentario(current_app.db, cid):
            idComentario = str(cid)
            rep = "El comentario con id "+ idComentario +" no existe"
            return (rep, HTTPStatus.NOT_FOUND)
        else:
            username = token_info['user_token']['username']
            rep: Dict = ServicioReporte.create_reportCom(current_app.db, username, body['reason'], cid)
            return (rep, HTTPStatus.CREATED)

def change_status_repCom(crid: int, body: Dict) -> Tuple[Dict,int]:
    """Cambia el estado de un reporte de comentario
    """
    with current_app.app_context():
        if not ServicioReporte.existe_reporteCom(current_app.db, crid):
            idReporteCom = str(crid)
            rep = "El reporte de comentario con id "+ idReporteCom +" no existe"
            return (rep, HTTPStatus.NOT_FOUND)
        else:
            ServicioReporte.change_status_reportCom(current_app.db, crid, body['status'])
            rep: Dict = ServicioReporte.get_reportCom(current_app.db, crid)
            #rep: Dict = ServicioReporte.change_status_reportCom(current_app.db, crid, body['status'])
            return (rep, HTTPStatus.NO_CONTENT)


# Reportes para preguntas

def list_repPreg() -> Tuple[Dict,int]:
    """ Devuelve reportes de preguntas
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.list_reportsPreg(current_app.db)
    return (rep, HTTPStatus.OK)

def get_repPreg(qrid:int) -> Tuple[Dict,int]:
    """ Devuelve un reporte sabiendo el id
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.get_reportPreg(current_app.db, qrid)
    return (rep, HTTPStatus.OK)

def create_repPreg(qid: int, body: Dict, token_info: Dict) -> Tuple[Dict,int]:
    """ Recoge los datos de la peticion y los manda al servicio de reportes (preguntas)
    """
    with current_app.app_context():
        if not PreguntasServicio.existe_pregunta(current_app.db, qid):
            idPregunta = str(qid)
            rep = "La pregunta con id "+ idPregunta +" no existe"
            return (rep, HTTPStatus.NOT_FOUND)
        else:
            username = token_info['user_token']['username']
            rep: Dict = ServicioReporte.create_reportPreg(current_app.db, username, body['reason'], qid)
            return (rep, HTTPStatus.CREATED)

def change_status_repPreg(qrid: int, body: Dict) -> Tuple[Dict,int]:
    """Cambia el estado de un reporte de pregunta
    """
    with current_app.app_context():
        if not ServicioReporte.existe_reportePreg(current_app.db, qrid):
            idReportePreg = str(qrid)
            rep = "El reporte de pregunta con id "+ idReportePreg +" no existe"
            return (rep, HTTPStatus.NOT_FOUND)
        else:
            ServicioReporte.change_status_reportPreg(current_app.db, qrid, body['status'])
            rep: Dict = ServicioReporte.get_reportPreg(current_app.db, qrid)
            #rep: Dict = ServicioReporte.change_status_reportPreg(current_app.db, qrid, body['status'])
            return (rep, HTTPStatus.NO_CONTENT)


# Reportes para respuestas

def list_repRes() -> Tuple[Dict,int]:
    """ Devuelve reportes de respuestas
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.list_reportsRes(current_app.db)
    return (rep, HTTPStatus.OK)

def get_repRes(arid:int) -> Tuple[Dict,int]:
    """ Devuelve un reporte sabiendo el id
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.get_reportRes(current_app.db, arid)
    return (rep, HTTPStatus.OK)

def create_repRes(aid: int, body: Dict, token_info: Dict) -> Tuple[Dict,int]:
    """ Recoge los datos de la peticion y los manda al servicio de reportes (respuestas)
    """
    with current_app.app_context():
        if not ServicioRespuestas.existe_respuesta(current_app.db, aid):
            idRespuesta = str(aid)
            rep = "La respuesta con id "+ idRespuesta +" no existe"
            return (rep, HTTPStatus.NOT_FOUND)
        else:
            username = token_info['user_token']['username']
            rep: Dict = ServicioReporte.create_reportRes(current_app.db, username, body['reason'], aid)
            return (rep, HTTPStatus.CREATED)

def change_status_repRes(arid: int, body: Dict) -> Tuple[Dict,int]:
    """Cambia el estado de un reporte de respuesta
    """
    with current_app.app_context():
        if not ServicioReporte.existe_reporteRes(current_app.db, arid):
            idReporteRes = str(arid)
            rep = "El reporte de respuesta con id "+ idReporteRes +" no existe"
            return (rep, HTTPStatus.NOT_FOUND)
        else:
            ServicioReporte.change_status_reportRes(current_app.db, arid, body['status'])
            rep: Dict = ServicioReporte.get_reportRes(current_app.db, arid)
            #rep: Dict = ServicioReporte.change_status_reportRes(current_app.db, arid, body['status'])
            return (rep, HTTPStatus.NO_CONTENT)
