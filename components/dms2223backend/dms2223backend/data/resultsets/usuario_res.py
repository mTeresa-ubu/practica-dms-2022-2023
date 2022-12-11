from dms2223backend.data.db import Usuario
from typing import List, Dict, Optional
from datetime import datetime

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore

class usuario_funcs():
    
    @staticmethod
    def get_by_nombre(session:Session, nombre:str) -> Usuario:
        """  Se obtiene el id de un usuario mediante su nombre
        """
        stmt = select(Usuario).where(Usuario.nombre == nombre).first()
        usu:Usuario = session.scalars(stmt).one()
        return usu