import json
import time
from typing import Dict, Tuple, Optional, List
from http import HTTPStatus
from flask import current_app

from sqlalchemy.orm.session import Session # type: ignore

from dms2223backend.data.resultsets.pregunta_res import PreguntaRes, PreguntaFuncs
from dms2223backend.service import PreguntasServicio, UsuariosServicio
from dms2223backend.data.db import Pregunta

from flask import current_app

def get_allusers() -> Tuple[List[Dict],Optional[int]]:
    with current_app.app_context():
        usuarios = UsuariosServicio.get_all(current_app.db)
    return (usuarios, HTTPStatus.OK)