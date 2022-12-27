from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db import Schema
from .authservice import AuthService
from sqlalchemy import select, Column, String, Text, Boolean, DateTime, ForeignKey, Integer
from dms2223backend.data.db.results import Comentario
from dms2223backend.data.db.results.comentario import Comentario
from dms2223backend.data.db.resultsets.comentario_res import ComentarioFuncs
from dms2223backend.data.db.resultsets.respuesta_res import RespuestaFuncs

#MTeresa

class servicioComentario():

    def init(self):
        self.auth_service = AuthService(apikey_secret='1234',host="172.10.1.10",port=4000)

    def crear_comentario(schema:Schema) -> Comentario:
        session: Session = schema.new_session()
        pass

    def get_comentario(schema:Schema, id:int) -> Comentario:
        session: Session = schema.new_session()
        comentarioADevolver = ComentarioFuncs.get_comentario(session, id)
        schema.remove_session()
        return comentarioADevolver

    def get_comentarios(self, schema:Schema) -> List[Comentario]:
        #ESTO ESTA MAL
        session: Session = schema.new_session()
        comentariosADevolver = ComentarioFuncs.list_all(10,session)
        schema.remove_session()
        return comentariosADevolver