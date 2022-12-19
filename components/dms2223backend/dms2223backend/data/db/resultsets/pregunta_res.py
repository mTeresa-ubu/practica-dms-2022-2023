from typing import List, Dict, Optional
from datetime import datetime

from dms2223backend.data.db.Usuario import Usuario
from dms2223backend.data.db.Elemento import Pregunta, Respuesta, Comentario
from dms2223backend.data.db.Voto import Voto

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore


class PreguntaFuncs():
    """ Calase apra acceder a los datos
    """
    @staticmethod
    def create(session:Session,pregunta:Pregunta) -> Pregunta:
        """ Inserta una pregunta en la bdd
        """
        session.add(pregunta)
        session.commit()
        # ! Importante, se recuperoa la pregunta creada, con id fecha y demas datos
        session.refresh(pregunta)

        return pregunta
        
    @staticmethod
    def get_pregunta(session:Session,qid:int) -> Pregunta:
        stmt = session.query(Pregunta).where(Pregunta.id_pregunta == qid)
        return stmt.first()

    @staticmethod
    def list_all(max:Optional[int], session: Session) -> List[Dict]:
        """ Se obtienen todos los registros de pregunta, con un limite si se especifica
        """

        listaPreguntas: List[Pregunta] = []
        stmt = select(Pregunta)

        if (max):
            stmt = stmt.limit(max)        

        for preg in session.execute(stmt):
            p = {
                "qid": preg[0].id_pregunta,
                "title": preg[0].titulo,
                "timestamp": preg[0].fecha,
                "autor" : preg[0].autor.nombre,
                "pos_votes": 0,
                "neg_votes": 0
            }
            listaPreguntas.append(p)

        # Esto tiene que devolver la lista bien formateada
        return listaPreguntas

    

    