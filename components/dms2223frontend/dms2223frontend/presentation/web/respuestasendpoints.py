from dms2223frontend.data.claseRespuesta.respuesta import Respuesta
from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from datetime import datetime


class RespuestasEndpoints():
    @staticmethod
    def get_respuesta(auth_service: AuthService, id_respuesta: int) -> Union[Response, Text]:
        resp = Respuesta(
            "Hoy es dia 10",
            id_respuesta,
            datetime.now(),
            34,
            35,
            12,
            "Yo"
        )
        return render_template('inicio/pregunta.html', pregunta=resp)