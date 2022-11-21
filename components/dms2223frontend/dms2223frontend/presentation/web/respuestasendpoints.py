""" RespuestasEndpoints class module.
"""

from dms2223frontend.data.clases.respuesta import Respuesta
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
            "1",
            "20",
            "Hoy es dia 10",
            datetime.now(),
            34,
            35,
            "Yo",
            15
        )
        return render_template('respuesta.html', respuesta_env=resp)