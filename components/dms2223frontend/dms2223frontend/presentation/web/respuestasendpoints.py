""" RespuestasEndpoints class module.
"""


from dms2223frontend.data.clases.comentario import Comentario
from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.authservice import AuthService
from dms2223frontend.data.rest.backendservice import BackendService
from .webauth import WebAuth
from .webAnswer import WebAnswer
from datetime import datetime


class RespuestasEndpoints():
    @staticmethod
    def get_respuestas(auth_service: AuthService,backend_service:BackendService,qid: int) -> Union[Response, Text]:
        redirect_to = request.args.get('redirect_to', default='/respuestas/respuesta.html')
        return render_template('respuesta.html',name=session['user'],redirect_to=redirect_to,
        respuesta= WebAnswer.get_answers(backend_service,qid))