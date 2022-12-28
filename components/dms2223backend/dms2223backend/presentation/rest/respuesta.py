from http import HTTPStatus
from flask import current_app
from typing import Dict
from dms2223backend.service.servicioRespuestas import ServicioRespuestas

def lista_Respuestas(qid : int):
    resp:Dict = ServicioRespuestas.getRespuestasAPregunta(
            schema=current_app.db,qid=qid)
    if not resp:
        idPregunta = str(qid)
        respuesta = "La pregunta con id "+ idPregunta +" no existe"
        return (respuesta, HTTPStatus.NOT_FOUND)
    return (resp, HTTPStatus.OK)

def crear_Respuesta(body: Dict, qid:int):
        return HTTPStatus.BAD_REQUEST


def vote_respuesta():
        return HTTPStatus.BAD_REQUEST     