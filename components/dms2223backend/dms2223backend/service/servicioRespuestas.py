from dms2223backend.data.db.resultsets.respuesta_res import RespuestaFuncs
from dms2223backend.data.db.resultsets.votos import Votos
from dms2223backend.service.servicioComentario import servicioComentario
from dms2223backend.data.db import Schema
from sqlalchemy.orm.session import Session  # type: ignore
from typing import List, Dict

class ServicioRespuestas():
    @staticmethod
    def getRespuestasAPregunta(schema: Schema, qid: int):
        """Devuelve un diccionario de las respuestas correspondientes a la pregunta
           pasada por parametro.

        Args: qid: pregunta de la que se quieren sus respuesta. 
              schema: elemento de consulta centralizado.

        Returns: Diccionario con las respuestas encontradas.
        """

        session: Session = schema.new_session()

        out: List[Dict] = RespuestaFuncs.list_all(session,qid)
        lista_respuestas: List = []
        for respuesta in out:
            lista_respuestas.append({
            "id":respuesta.id,
            "qid":respuesta.qid,
            "body":respuesta.body,
            "comentarios": servicioComentario.get_comentarios(schema=schema,aid=respuesta.id),
            "owner":{"username":respuesta.username},
            "timestamp":respuesta.timestamp,
            "oculto":respuesta.oculto,
            "votos":respuesta.votos
            })
        schema.remove_session()
        return lista_respuestas
    @staticmethod
    def create_Respuesta(schema:Schema,username:str,body:Dict,qid:int):
        """Crea una respuesta y devuelve el diccionario de la respuesta creada.

        Args: qid: Identificador de la pregunta que se va a responder.
                 username: Usuario que responde a la pregunta.
                 body: Cuerpo de la respuesta.
                 schema: elemento de consulta centralizado.
        Returns: Diccionario de la respuesta creada. 
        """
        session: Session = schema.new_session()

        res: Dict = RespuestaFuncs.create(session,username=username, body=body,qid=qid)

        respuesta: Dict = {
            "id":res.id,
            "qid":res.qid,
            "body":res.body,
            "comentarios": servicioComentario.get_comentarios(schema=schema,aid=res.id),
            "owner":{"username":res.username},
            "timestamp":res.timestamp,
            "oculto":res.oculto,
            "votos":res.votos
        }

        schema.remove_session()

        return respuesta


    @staticmethod
    def existe_respuesta(schema: Schema,id:int):
        session: Session = schema.new_session()
        respuesta: Dict = RespuestaFuncs.get_respuesta(session,id)
        schema.remove_session()
        if not respuesta:
            return False
        else:
            return True

    @staticmethod
    def ocultarRes(schema: Schema, id: int):
        """Oculta la respuesta
        """
        session: Session = schema.new_session()

        res = RespuestaFuncs.get_respuesta(session,id)
        res.oculto = True

        session.add(res)
        session.commit()

        schema.remove_session()
    
    @staticmethod
    def votar_Respuesta(schema: Schema, id: int):
        session: Session = schema.new_session()

        Votos.votar_Respuesta(session,id)

        schema.remove_session()


