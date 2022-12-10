""" UserServices class module.
"""

from typing import List, Dict, ClassVar
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db import Schema

from dms2223backend.data.db.Elemento import Pregunta, Respuesta, Comentario
from dms2223backend.data.db.Voto import Voto
from dms2223backend.data.resultsets.pregunta_res import PreguntaFuncs

from sqlalchemy import select

from .authservice import AuthService

class PreguntasServicio():
    """ Clase "estatica" que permite el acceso a las operaciones de creacion o consulta
        derivados de pregunta
    """
    def __init__(self):
        self.auth_service = AuthService(apikey_secret='1234',host="172.10.1.10",port=4000)

    def get_pregunta(schema:Schema, id:int) -> Pregunta:
        """Obtiene los datos de una pregunta se debe usar para la visualizacion
            en lista de pregunta, no contiene los votos de las respuestas 
        """
        session: Session = schema.new_session()
        stmt = select(Pregunta).where(Pregunta.id_pregunta == id)
        preg = session.execute(stmt).first()
        schema.remove_session()
        return preg

    def get_preguntas(self, schema:Schema) -> List[Pregunta]:
        """ Devuleve una lista de todas las preguntas
        """
        session: Session = schema.new_session()
        preguntas = PreguntaFuncs.list_all(10,session)
        schema.remove_session()
        return preguntas
    
    def get_preguntas_filtro(schema:Schema,campo:type,valor:str|int) -> List[Pregunta]:
        session: Session = schema.new_session()
        stmt = select(Pregunta).where(campo == valor)
        preguntas = session.execute(stmt).all()
        schema.remove_session()
        return preguntas
