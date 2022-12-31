"""REST API controllers responsible of handling the server operations about questions
"""

import json
import time
from typing import Dict, Tuple, Optional, List, Union
from http import HTTPStatus


from sqlalchemy.orm.session import Session # type: ignore

from dms2223backend.service.serviciopreguntas import PreguntasServicio
from flask import current_app
import requests

def __init__(self) -> None:
    pass

def create_preg(body: Dict, token_info: Dict) -> Tuple[Union[Dict,str],int]:
    """ Recoge los datos de la peticion y los manda al servicio de preguntas
    """
    with current_app.app_context():
        username = token_info['user_token']['username']
        res:Dict = PreguntasServicio.create_pregunta(current_app.db, body['body'], body['title'], username)
    return (res, HTTPStatus.CREATED)

def get_preg_id(qid:int) -> Tuple[Dict,int]:
    """ Devuelve una pregunta sabiendo el id
    """
    with current_app.app_context():
        resp:Dict = PreguntasServicio.get_pregunta(
            current_app.db,qid)
    return (resp, HTTPStatus.OK)

def get_pregs() -> Tuple[Dict,int]:
    """ Devuelve una pregunta sabiendo el id
    """
    with current_app.app_context():
        resp:Dict = PreguntasServicio.get_preguntas(
            current_app.db)
    return (resp, HTTPStatus.OK)

# def get_preg_answers(qid:int) -> Tuple[List[Dict],Optional[int]]:
#     """ Devuelve una lista de respuestas a una pregunta
#     """
#     with current_app.app_context():
#         resp:Dict = RespuestasServicio.get_answers(current_app.db,qid)
#     return (resp, HTTPStatus.OK)

# def set_preg_answer(qid:int) -> Tuple[Dict,Optional[int]]:
#     """ Crea una respuesta a unn comentario !TODO delegar a respuesta
#     """
#     with current_app.app_context():
#         resp:Dict = PreguntasServicio.get_answers(qid)
#     return (resp, HTTPStatus.OK)

# def set_preg_report(qid:int,body: Dict, token_info: Dict) -> Tuple[Dict,Optional[int]]:
#     with current_app.app_context():
#         rep:Dict = {
#             "razon_reporte":body["reason"],
#             "qid":qid,
#             "autor":token_info["user_token"]["username"]
#         }

#         report = PreguntasServicio.set_report(
#             schema=current_app.db,
#             reporte=rep
#         )
#     return (report, HTTPStatus.OK)

# def get_all_reports() -> Tuple[List[Dict],Optional[int]]:
#     """ Devuelve todos los reportes que se han hecho a las preguntas
#     """
#     with current_app.app_context():
#         resp:Dict = PreguntasServicio.get_all_reports(
#             schema=current_app.db
#         )
#     return (resp, HTTPStatus.OK)

# def put_preg_report(qrid:int) -> Tuple[Dict,Optional[int]]:
#     with current_app.app_context():
#         resp:Dict = PreguntasServicio.get_pregunta(qrid)
#     return (resp, HTTPStatus.OK)