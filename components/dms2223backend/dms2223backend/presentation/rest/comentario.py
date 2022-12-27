"""REST API controllers responsible of handling the server operations about comments
"""
import json
import time
import requests
from typing import Dict, Tuple, Optional, List, Union
from http import HTTPStatus
from flask import current_app

from sqlalchemy.orm.session import Session # type: ignore

from dms2223backend.service.servicioComentario import servicioComentario
from dms2223backend.service.servicioRespuestas import ServicioRespuestas

def create_comment(body: Dict, token_info: Dict) -> Tuple[Union[Dict,str],int]:
    pass
#    """ Crea un comentario
#    """
#    with current_app.app_context():
#
#        username = token_info['user_token']['username']
#        comentario: Dict = ComentariosServicio.crear_comentario()
#        res:Dict = PreguntasServicio.create_pregunta(current_app.db, username, body['body'], body['title'])
#    return (res, HTTPStatus.OK)
#
#
def get_comments(aid:int) -> Tuple[Dict,int]:
    pass
#    """ Devuelve una pregunta sabiendo el id
#    """
#    with current_app.app_context():
#        resp:Dict = PreguntasServicio.get_pregunta(
#            current_app.db,qid)
#    return (resp, HTTPStatus.OK)
#
def vote_comment(cid: int) -> Tuple[dict, int]:
    pass

def report_comment(cid: int) -> Tuple[dict, int]:
    pass