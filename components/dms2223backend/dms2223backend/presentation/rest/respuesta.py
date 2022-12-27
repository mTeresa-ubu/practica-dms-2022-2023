from http import HTTPStatus
from flask import current_app
from typing import Dict, Tuple
from dms2223backend.service.servicioRespuestas import ServicioRespuestas

def lista_Respuestas(qid : int):
    resp:Dict = ServicioRespuestas(
            current_app.db,qid)
    return (resp, HTTPStatus.OK)

def crear_Respuesta(body: Dict, qid:int):
        return HTTPStatus.BAD_REQUEST
        
def vote_respuesta(qid: int):
    pass