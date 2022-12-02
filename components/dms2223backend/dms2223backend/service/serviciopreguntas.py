""" UserServices class module.
"""

from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db import Schema

from dms2223backend.data.db.Elemento import Pregunta, Respuesta, Comentario
from dms2223backend.data.db.Voto import Voto
from dms2223backend.data.resultsets.pregunta_res import PreguntaFuncs

class PreguntasServicio():
    """ Clase "estatica" que permite el acceso a las operaciones de creacion o consulta
        derivados de pregunta
    """
    @staticmethod
    def get_pregunta(schema:Schema, id:int): # -> Dict[Pregunta,List[Respuesta],List[Voto]]:
        """Obtiene los datos de una pregunta se debe usar para la visualizacion
            en lista de pregunta, no contiene los votos de las respuestas 
        """
        session: Session = schema.new_session()

    @staticmethod
    def get_preguntas(schema:Schema): # -> Dict[Pregunta,List[Respuesta],List[Voto]]:
        """Obtiene los datos de una pregunta se debe usar para la visualizacion
            en lista de pregunta, no contiene los votos de las respuestas 
        """
        session: Session = schema.new_session()
        preguntas = PreguntaFuncs.list_all(10,session)
        schema.remove_session()
        return preguntas
