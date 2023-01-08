from typing import List, Dict, Optional
from dms2223backend.data.db.results import Respuesta
from dms2223backend.data.db.results import Comentario

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select, update# type: ignore


class Votos():

    @staticmethod
    def votar_Respuesta(session:Session, id: int):
        stmt = update(Respuesta).where(Respuesta.id == id).values(votos= Respuesta.votos + 1)
    



    