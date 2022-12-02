from typing import List, Dict, Optional
from datetime import datetime

from dms2223backend.data.db.Usuario import Usuario
from dms2223backend.data.db.Elemento import Pregunta, Respuesta, Comentario
from dms2223backend.data.db.Voto import Voto

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore

class PreguntaRes():
    """ Clase de alto nivel que va a contener los datos completos de una pregunta
        Incluye las operaciones de acceso a tablas
        No se si respetar la herencia, de momento no
    """
    titulo: str
    id_pregunta: int #Es el mismo que el de elemento
    fecha: datetime
    autor: Usuario
    contenido: str
    visibilidad: bool
    votos = List[Voto]
    respuestas = List[Respuesta]

    def create():
        """ Se crea con los datos del objeto
            Sin votos ni respuestas
        """
        pass

class PreguntaFuncs():
    @staticmethod
    def list_all(max:Optional[int], session: Session) -> List[PreguntaRes]:
        """ Se obtienen todos los registros de pregunta, con un limite si se especifica
        """

        listaPreguntas: List[PreguntaRes]
        stmt = select(Pregunta)

        if (max):
            stmt = stmt.limit(max)

        for preg in session.scalars(stmt):
            print(preg)

        pass
