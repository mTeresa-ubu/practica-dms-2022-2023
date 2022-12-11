"""REST API controllers responsible of handling the server operations about questions
"""

import json
import time
from typing import Dict, Tuple, Optional, List
from http import HTTPStatus
from flask import current_app

from sqlalchemy.orm.session import Session # type: ignore

from dms2223backend.data.resultsets.pregunta_res import PreguntaRes, PreguntaFuncs
from dms2223backend.service.serviciopreguntas import PreguntasServicio
from dms2223backend.data.db import Pregunta

from flask import current_app

from dms2223backend.service import AuthService

import requests

def create_preg(body: Dict, token_info: Dict) -> Tuple[str,Optional[int]]:
    """ Recoge los datos de la peticion y los manda al servicio de preguntas
    """
    with current_app.app_context():
        preg:Dict = {
            "titulo":body["title"],
            "contenido":body["body"],
            "autor":token_info["user_token"]["username"]
        }

        res:Pregunta = PreguntasServicio.create_pregunta(
            schema=current_app.db,datos=preg)
    return (res.titulo, HTTPStatus.OK)