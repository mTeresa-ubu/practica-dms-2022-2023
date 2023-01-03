from dms2223frontend.data.clases.respuesta import Respuesta
from dms2223frontend.data.rest.authservice import AuthService
from dms2223frontend.data.rest.backendservice import BackendService

from typing import Text, Union
from flask import redirect, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2223common.data import Role
from .webauth import WebAuth
from .webutils import WebUtils
from datetime import datetime

#-------------------------------------------
#ESTA SIN FINALIZAR, DE MOMENTO NO FUNCIONAN
#-------------------------------------------

@staticmethod
def post_crear_comentario(backend_service: BackendService, auth_service: AuthService) -> Union[Response, Text]:
    if not WebAuth.test_token(auth_service):
        return redirect(url_for('get_login'))
    if Role.DISCUSSION.name not in session['roles']:
        return redirect(url_for('get_home'))

    autor = session.get('user')
    texto = request.form.get('body')
    aid = request.form.get('aid')
    sentiment = request.form.get('sentiment')

    comentario: Response = backend_service.crear_comentario(backend_service, autor, texto, aid, sentiment)
    


    return redirect(redirect_to)

@staticmethod
def post_new_comment_vote(backend_service: BackendService, auth_service: AuthService):
    if not WebAuth.test_token(auth_service):
        return redirect(url_for('get_login'))
    if Role.DISCUSSION.name not in session['roles']:
        return redirect(url_for('get_home'))

    cid = request.form.get('cid')
    qid = request.form.get('qid')

    WebAnswer.new_comment_vote(backend_service, cid)
    return redirect("/questions/answers?qid=" + str(qid))