""" PreguntasEndpoints class module.
"""    

from dms2223frontend.data.clases.pregunta import Pregunta

from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2223common.data import Role
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
     
    """ Monostate class responsible of handling the session web endpoint requests.
    """
    @staticmethod
    def get_crear_preguntas(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the home endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.ADMINISTRATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        return render_template('preguntas/crear_preguntas.html', name=name, roles=session['roles'])

