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
        stmt = select(Usuario).where(Usuario.nombre == nombre)
        usu:Usuario = session.execute(stmt).first()

        return usu[0]
    
    @staticmethod
    def get_or_create(session:Session, nombre:str) -> Usuario:
        """  Se obtiene el id de un usuario mediante su nombre
        """
        stmt = select(Usuario).where(Usuario.nombre == nombre)
        usu:Usuario = session.execute(stmt).first()

        if usu is None:
            usu = UsuarioFuncs.create(session=session,usu=Usuario(nombre=nombre))
        else:
            usu = usu[0]
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