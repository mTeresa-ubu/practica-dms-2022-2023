""" PreguntasEndpoints class module.
"""    

from dms2223frontend.data.clases.pregunta import Pregunta
from dms2223frontend.data.clases.respuesta import Respuesta
from dms2223frontend.data.rest.authservice import AuthService
from dms2223frontend.data.rest.backendservice import BackendService

from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2223common.data import Role
from .webauth import WebAuth
from .pregunta import PreguntaWeb
from datetime import datetime
from flask import request

class PreguntasEndpoints():
     
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
        if Role.ADMINISTRATION.name not in session['roles']: #cambiar a discussion cuando funcione
            return redirect(url_for('get_home'))
        return render_template('preguntas/crear_preguntas.html', name=session['user'], roles=session['roles'])
        
    @staticmethod
    def post_preguntas(auth_service: AuthService, back_service: BackendService) -> Union[Response, Text]:
         if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
         if Role.ADMINISTRATION.name not in session['roles']: #cambiar a discussion cuando funcione
            return redirect(url_for('get_home'))
         preg = PreguntaWeb.nueva_pregunta(back_service, title=request.form.get('title'), body=request.form.get('body'))
         redirect_to = request.form['redirect_to']
         if not redirect_to:
            redirect_to = url_for('get_questions')
         
         return redirect(redirect_to)

    
    @staticmethod
    def get_crear_reportePreg(auth_service: AuthService) -> Union[Response, Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        return render_template('/preguntas/crear_reporte_pregunta.html', name=session['user'], roles=session['roles'], qid=request.args.get('qid'))

    @staticmethod
    def post_reportePreg(auth_service: AuthService, backend_service: BackendService) -> Union[Response, Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        qid = request.form.get('qid')
        reason = request.form.get('bodyText')

        new_question = PreguntaWeb.new_report_question(backend_service, qid=qid, reason=reason)
        if not new_question:
            return redirect(url_for('get_new_question'))
        redirect_to = request.form['redirect_to']
        if not redirect_to:
            redirect_to = url_for('get_questions')
        return redirect(redirect_to)