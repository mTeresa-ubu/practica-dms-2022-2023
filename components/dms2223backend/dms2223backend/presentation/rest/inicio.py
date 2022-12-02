""" REST API controllers responsible of handling the server operations.
"""

import json
import time
from typing import Dict, Tuple, Optional
from http import HTTPStatus
from flask import current_app

from sqlalchemy.orm.session import Session # type: ignore

from dms2223backend.data.resultsets.pregunta_res import PreguntaRes, PreguntaFuncs
from dms2223backend.service.serviciopreguntas import PreguntasServicio

from dms2223backend.data.db import Schema

def test_inicio() -> Tuple[str,Optional[int]]:
    with current_app.app_context():
        pregs = PreguntasServicio.get_preguntas(current_app.db)
        print(pregs)
    return ('Hola', HTTPStatus.OK)
