""" CommonEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth

from dms2223frontend.data.clases.pregunta import Pregunta
from datetime import datetime

class CommonEndpoints():
    """ Monostate class responsible of handling the common web endpoint requests.
    """
    @staticmethod
    def get_home(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the home endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        # Editado por alvar el 4/11/2022 apra evitar la redireccion, linea 26, 27
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))

        name = session['user']

        #Lista de preguntas hardcodeada
        #Cambiar por una peticion que solicite la lista
        pregs=[
            Pregunta("Contenido 1","1",datetime.now(),34,35,"Yo","Titulo 1"),
            Pregunta("Contenido 2","2",datetime.now(),34,35,"Yo","Titulo 2"),
            Pregunta("Contenido 3","3",datetime.now(),34,35,"Yo","Titulo 3"),
            Pregunta("Contenido 4","4",datetime.now(),34,35,"Yo","Titulo 4")
        ]

        return render_template('home.html', 
            name=name, 
            roles=session['roles'],
            preguntas=pregs)

    @staticmethod
    def get_inicio():
        """ Genstiona el acceso a inicio sin ningun tipo de login necesario
        
        """

        pregs=[
            Pregunta("Contenido 1","1",datetime.now(),34,35,"Yo","Titulo 1"),
            Pregunta("Contenido 2","2",datetime.now(),34,35,"Yo","Titulo 2"),
            Pregunta("Contenido 3","3",datetime.now(),34,35,"Yo","Titulo 3"),
            Pregunta("Contenido 4","4",datetime.now(),34,35,"Yo","Titulo 4")
        ]

        return render_template('inicio/inicio.html',
            preguntas=pregs)