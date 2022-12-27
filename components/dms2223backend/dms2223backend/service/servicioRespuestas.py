from dms2223backend.data.db.resultsets.respuesta_res import RespuestaFuncs
from dms2223backend.data.db import Schema
from sqlalchemy.orm.session import Session  # type: ignore
from typing import List, Dict

class ServicioRespuestas():

    def getRespuestasAPregunta(schema: Schema, qid: int):
        """Devuelve un diccionario de las respuestas correspondientes a la pregunta
           pasada por parametro.

        Args: id_Preguta: pregunta de la que se quieren sus respuesta. 
              schema: elemento de consulta centralizado.

        Returns: Diccionario con las respuestas encontradas.
        """

        session: Session = schema.new_session()

        out: List[Dict] = RespuestaFuncs.list_all(session,qid)

        schema.remove_session()
        return out