from http import HTTPStatus
from flask import current_app
from typing import Dict
from dms2223backend.service.servicioRespuestas import ServicioRespuestas
from dms2223backend.service.serviciopreguntas import PreguntasServicio

def lista_Respuestas(qid : int):       
    with current_app.app_context():
        if not PreguntasServicio.existe_pregunta(schema=current_app.db,qid=qid):
                idPregunta = str(qid)

                respuesta = "La pregunta con id "+ idPregunta +" no existe"
                return (respuesta, HTTPStatus.NOT_FOUND)
        else:
                respuestas:Dict = ServicioRespuestas.getRespuestasAPregunta(
                schema=current_app.db,qid=qid)  

    
    return (respuestas, HTTPStatus.OK)

def crear_Respuesta(body: Dict,token_info:int,qid:int):
        with current_app.app_context():
                if not PreguntasServicio.existe_pregunta(schema=current_app.db,qid=qid):
                        idPregunta = str(qid)

                        respuesta = "La pregunta con id "+ idPregunta +" no existe"

                        return (respuesta, HTTPStatus.NOT_FOUND)
                else:
                        username = token_info['user_token']['username']

                        respuesta: Dict = ServicioRespuestas.create_Respuesta(
                        schema=current_app.db,username=username,body=body,qid=qid)

                        return (respuesta, HTTPStatus.CREATED)


def vote_respuesta(aid : int):
        with current_app.app_context():
                if ServicioRespuestas.existe_respuesta(schema=current_app.db,id=aid):
                        ServicioRespuestas.votar_Respuesta(schema=current_app.db,id=aid)
                        return HTTPStatus.CREATED
                else:
                        return HTTPStatus.BAD_REQUEST     