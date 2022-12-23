from sqlalchemy import Integer, select
from sqlalchemy.orm.session import Session  
from typing import List, Dicr, Optional
from datetime import datetime
from dms2223backend.data.db.Elemento.comentario import Comentario
from dms2223backend.data.db.Elemento.pregunta import Pregunta
from dms2223backend.data.db.Elemento.respuesta import Respuesta
#MTeresa
class ComentarioRset():
    id_comentario: int # = id_elemento
    feedback: str
    id_respuesta: int
    fecha: datetime
    autor: Usuario
    contenido: str
    visibilidad: bool

class ComentarioFuncs():
    @staticmethod
    def list_all(session: Session) -> List[Dict]:
        listaComentarios: List[ComentarioRset] = []
        ComentarioSeleccionado = select(Comentario)

        for com in session.execute(ComentarioSeleccionado):
            coment = {
                "cid": com[0].id_comentario,
                "feedback": com[0].feedback,
                "id_respuesta": com[0].id_respuesta,
                "fecha": com[0].fecha,
                "contenido": com[0].contenido,
                "autor": com[0].autor
            }
            listaComentarios.append(coment)

        
        return listaComentarios


        # get numero de votos y hacer .count