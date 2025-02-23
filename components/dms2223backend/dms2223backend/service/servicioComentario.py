from typing import List, Dict
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db import Schema
from .authservice import AuthService
from dms2223backend.data.sentiment import  Sentiment
from dms2223backend.data.db.results.comentario import Comentario
from dms2223backend.data.db.resultsets.comentario_res import ComentarioFuncs

class servicioComentario():

    def init(self):
        self.auth_service = AuthService(apikey_secret='1234',host="172.10.1.10",port=4000)

    def crear_comentario(schema:Schema, autor: str, body: str, aid: int, sentiment: Sentiment) -> Dict:
        session: Session = schema.new_session()
        comentario = ComentarioFuncs.create(session, autor, body, aid, sentiment)
        comentario:Dict = {
           "aid":comentario.aid,
            "body":comentario.body,
            "id": comentario.id,
            "owner":{"username":comentario.username},
            "sentiment": comentario.sentiment.name,
            "timestamp":comentario.timestamp
        }
        schema.remove_session()
        return comentario

    def get_comentario(schema:Schema, id:int) -> Comentario:
        session: Session = schema.new_session()
        comentario: Comentario = ComentarioFuncs.get_comentario(session, id)
        comentario:Dict = {
            "aid":comentario.aid,
            "body":comentario.body,
            "id": comentario.id,
            "owner":{"username":comentario.username},
            "sentiment": comentario.sentiment.name,
            "timestamp":comentario.timestamp
        }
        schema.remove_session()
        return comentario

    def get_comentarios(schema:Schema, aid:int) -> List[Comentario]:
        session: Session = schema.new_session()
        comentariosADevolver = ComentarioFuncs.list_all(session, aid)
        lista_comentarios: List = []
        for comentario in comentariosADevolver:
            lista_comentarios.append({
                "aid":comentario.aid,
                "body":comentario.body,
                "id": comentario.id,
                "owner":{"username":comentario.username},
                "sentiment": comentario.sentiment.name,
                "timestamp":comentario.timestamp
            })
        schema.remove_session()
        return lista_comentarios
    
    @staticmethod
    def ocultarCom(schema: Schema, id: int):
        """Oculta el comentario
        """
        session: Session = schema.new_session()

        com = ComentarioFuncs.get_comentario(session,id)
        com.oculto = True

        session.add(com)
        session.commit()

        schema.remove_session()

    @staticmethod
    def existe_comentario(schema: Schema,qid:int):
        session: Session = schema.new_session()
        comentario: Dict = ComentarioFuncs.get_comentario(session,qid)
        schema.remove_session()
        if not comentario:
            return False
        else:
            return True
    
