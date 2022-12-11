from dms2223backend.data.db import Usuario
from typing import List, Dict, Optional
from datetime import datetime

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select # type: ignore

class UsuarioFuncs():
    
    @staticmethod
    def get_by_nombre(session:Session, nombre:str) -> Usuario:
        """  Se obtiene el id de un usuario mediante su nombre
        """
        stmt = select(Usuario).where(Usuario.nombre == nombre).first()
        usu:Usuario = session.scalars(stmt).one()
        return usu

    @staticmethod
    def create(session:Session, usu:Usuario) -> Usuario:
        """ Se solicita un usuario, si no existe se crea
        """
        session.refresh(usu)
        return usu
    
    @staticmethod
    def get_all(session:Session) -> List[Usuario]:
        stmt = select(Usuario)
        usuarios:List[Usuario] = [] 
        for usu in session.execute(stmt):
            usuarios.append(usu[0])
        return usuarios