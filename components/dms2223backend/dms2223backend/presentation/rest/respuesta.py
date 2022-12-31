from http import HTTPStatus
from flask import current_app
from typing import Dict
from dms2223backend.service.servicioRespuestas import ServicioRespuestas

def lista_Respuestas(qid : int):       
    with current_app.app_context():
        respuestas:Dict = ServicioRespuestas.getRespuestasAPregunta(
                schema=current_app.db,qid=qid)  
        if not respuestas:
                idPregunta = str(qid)
                respuesta = "La pregunta con id "+ idPregunta +" no existe"
                return (respuesta, HTTPStatus.NOT_FOUND)
    
    return (respuestas, HTTPStatus.OK)

def crear_Respuesta(body: Dict,token_info:int,qid:int):
        with current_app.app_context():
                username = token_info['user_token']['username']
                respuesta: Dict = ServicioRespuestas.create_Respuesta(
                        schema=current_app.db,username=username,body=body)
        return (respuesta, HTTPStatus.CREATED)


def vote_respuesta(aid : int):
        return HTTPStatus.BAD_REQUEST     