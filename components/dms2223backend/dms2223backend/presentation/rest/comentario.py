"""REST API controllers responsible of handling the server operations about comments
"""
from typing import Dict, Tuple, Union
from http import HTTPStatus
from flask import current_app
from dms2223backend.service.servicioComentario import servicioComentario

def create_comment(aid: int, body: Dict, token_info: Dict) -> Tuple[Union[Dict,str],int]:
    """ Crea un comentario
    """
    with current_app.app_context():
        usuario = token_info['user_token']['username']
        comentario:Dict = servicioComentario.crear_comentario(current_app.db, usuario, body['body'], aid, body['sentiment'])
    return (comentario, HTTPStatus.CREATED)

def get_comments(aid:int) -> Tuple[Dict,int]:
    """ Devuelve los comentarios del id de respuesta
    """
    with current_app.app_context():
        comentarios:Dict = servicioComentario.get_comentarios(current_app.db,aid)
    return (comentarios, HTTPStatus.OK)

def get_comment(id:int) -> Tuple[Dict,int]:
    """ Devuelve un comentario sabiendo el id
    """
    with current_app.app_context():
        comentario:Dict = servicioComentario.get_comentario(current_app.db,id)
    return (comentario, HTTPStatus.OK)

def vote_comment(cid: int) -> Tuple[dict, int]:
    pass

def report_comment(cid: int) -> Tuple[dict, int]:
    pass