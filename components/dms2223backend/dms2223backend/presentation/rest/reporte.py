"""REST API controllers responsible of handling the server operations about reports
"""
from typing import Dict, Tuple, Optional, List, Union
from http import HTTPStatus
from flask import current_app
from sqlalchemy.orm.session import Session # type: ignore
from dms2223backend.service.servicioReportes import ServicioReporte

# Rober Lastras

# Reportes para comentarios

def list_repCom() -> Tuple[Dict,int]:
    """ Devuelve reportes de comentarios
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.list_reportsCom(current_app.db)
    return (rep, HTTPStatus.OK)

def get_repCom(id:int) -> Tuple[Dict,int]:
    """ Devuelve un reporte sabiendo el id
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.get_reportCom(current_app.db, id)
        if not rep:
            return("No existe ese reporte", HTTPStatus.BAD_REQUEST)
    return (rep, HTTPStatus.OK)

def create_repCom(cid: int, body: Dict, token_info: Dict) -> Tuple[Union[Dict,str],int]:
    """ Recoge los datos de la peticion y los manda al servicio de reportes (comentarios)
    """
    with current_app.app_context():
        username = token_info['user_token']['username']
        rep: Dict = ServicioReporte.create_reportCom(current_app.db, username, body['reason'], cid)
    return (rep, HTTPStatus.CREATED)

def change_status_repCom(crid: int, body: Dict) -> Tuple[Union[Dict,str],int]:
    """Cambia el estado de un reporte de comentario
    """
    with current_app.app_context():
        ServicioReporte.change_status_reportCom(current_app.db, crid, body['status'])
        rep: Dict = ServicioReporte.get_reportCom(current_app.db, crid)
        return rep, HTTPStatus.OK


# Reportes para preguntas

def list_repPreg() -> Tuple[Dict,int]:
    """ Devuelve reportes de preguntas
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.list_reportsPreg(current_app.db)
    return (rep, HTTPStatus.OK)

def get_repPreg() -> Tuple[Dict,int]:
    """ Devuelve un reporte sabiendo el id
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.get_reportPreg(current_app.db, id)
        if not rep:
            return("No existe ese reporte", HTTPStatus.BAD_REQUEST)
    return (rep, HTTPStatus.OK)

def create_repPreg(qid: int, body: Dict, token_info: Dict) -> Tuple[Union[Dict,str],int]:
    """ Recoge los datos de la peticion y los manda al servicio de reportes (preguntas)
    """
    with current_app.app_context():
        username = token_info['user_token']['username']
        rep: Dict = ServicioReporte.create_reportPreg(current_app.db, username, body['reason'], qid)
    return (rep, HTTPStatus.CREATED)

def change_status_repPreg(qrid: int, body: Dict) -> Tuple[Union[Dict,str],int]:
    """Cambia el estado de un reporte de pregunta
    """
    with current_app.app_context():
        ServicioReporte.change_status_reportPreg(current_app.db, qrid, body['status'])
        rep: Dict = ServicioReporte.get_reportPreg(current_app.db, qrid)
        return rep, HTTPStatus.OK


# Reportes para respuestas

def list_repRes() -> Tuple[Dict,int]:
    """ Devuelve reportes de respuestas
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.list_reportsRes(current_app.db)
    return (rep, HTTPStatus.OK)

def get_repRes() -> Tuple[Dict,int]:
    """ Devuelve un reporte sabiendo el id
    """
    with current_app.app_context():
        rep: Dict = ServicioReporte.get_reportRes(current_app.db, id)
        if not rep:
            return("No existe ese reporte", HTTPStatus.BAD_REQUEST)
    return (rep, HTTPStatus.OK)

def create_repRes(aid: int, body: Dict, token_info: Dict) -> Tuple[Union[Dict,str],int]:
    """ Recoge los datos de la peticion y los manda al servicio de reportes (respuestas)
    """
    with current_app.app_context():
        username = token_info['user_token']['username']
        rep: Dict = ServicioReporte.create_reportRes(current_app.db, username, body['reason'], aid)
    return (rep, HTTPStatus.CREATED)

def change_status_repRes(arid: int, body: Dict) -> Tuple[Union[Dict,str],int]:
    """Cambia el estado de un reporte de respuesta
    """
    with current_app.app_context():
        ServicioReporte.change_status_reportRes(current_app.db, arid, body['status'])
        rep: Dict = ServicioReporte.get_reportRes(current_app.db, arid)
        return rep, HTTPStatus.OK