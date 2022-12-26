# from typing import List, Dict
# from sqlalchemy.orm.session import Session  # type: ignore
# from dms2223backend.data.db import Schema
# from .authservice import AuthService
# from sqlalchemy import select, Column, String, Text, Boolean, DateTime, ForeignKey, Integer
# from dms2223backend.data.db.results import Comentario
# from dms2223backend.data.db.Elemento.comentario import Comentario
# from dms2223backend.data.resultsets.comentario_res import ComentarioFuncs
# from dms2223backend.data.resultsets.pregunta_res import PreguntaFuncs

# #MTeresa

# class servicioComentario():
    
#     def __init__(self):
#         self.auth_service = AuthService(apikey_secret='1234',host="172.10.1.10",port=4000)

#     def get_comentario(schema:Schema, id:int) -> Comentario:
#         session: Session = schema.new_session()
#         stmt = select(Comentario).where(Comentario.id_comentario == id)
#         comentarioADevolver = session.execute(stmt).first()
#         schema.remove_session()
#         return comentarioADevolver

#     def get_comentarios(self, schema:Schema) -> List[Comentario]:
#         session: Session = schema.new_session()
#         comentariosADevolver = ComentarioFuncs.list_all(10,session)
#         schema.remove_session()
#         return comentariosADevolver

#     #filtrode comentarios??
    