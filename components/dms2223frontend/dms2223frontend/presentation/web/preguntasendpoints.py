""" PreguntasEndpoints class module.
"""    

from dms2223frontend.data.clases.pregunta import Pregunta
from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from datetime import datetime


class PreguntasEndpoints():
    @staticmethod
    def get_pregunta(auth_service: AuthService, id_preg: int) -> Union[Response, Text]:
        preg = Pregunta(
            "Que dia es hoy",
            id_preg,
            datetime.now(),
            34,
            35,
            12,
            "Yo"
        )
        return render_template('inicio/pregunta.html', pregunta=preg)
