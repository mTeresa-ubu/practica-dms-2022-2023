""" UserServices class module.
"""
from typing import List
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db import Schema
from dms2223backend.data.db.resultsets.pregunta_res import PreguntaFuncs
from dms2223backend.data.db.results.pregunta import Pregunta
from datetime import datetime

class PreguntasServicio():
    """ Clase "estatica" que permite el acceso a las operaciones de creacion o consulta
        derivados de pregunta
    """
##de esta forma sí respetamos el SINGLE RESPONSABILITY PRINCIPLE   
    @staticmethod
    def get_pregunta(schema:Schema, qid:int) -> dict:
        """Obtiene los datos de una pregunta se debe usar para la visualizacion
            en lista de pregunta, no contiene los votos de las respuestas 
        """
        session: Session = schema.new_session()
        preg: Pregunta = PreguntaFuncs.get_pregunta(session, qid)
        
        preg:dict = {
            "qid":preg.qid,
            "title":preg.title,
            "timestamp":preg.timestamp,
            "body":preg.body,
            "owner":{"username":preg.username}
        }
        

        schema.remove_session()
        return preg
        pass

    @staticmethod
    def get_preguntas(schema:Schema) -> List:
        """ Devuleve una lista de todas las preguntas
        """
        session: Session = schema.new_session()
        preguntas = PreguntaFuncs.list_all(session)
        list_preg: List = []
        for p in preguntas:
            list_preg.append(
                {
                "qid":p.qid,
                "title":p.title,
                "timestamp":p.timestamp
                }
            )

        schema.remove_session()
        return list_preg
        pass
    
    @staticmethod
    def create_pregunta(schema:Schema, username:str, body: str, title:str) -> dict:
        """ Construye el objeto Pregunta que se insertara en la BDD
        """
        session: Session = schema.new_session() 

        res = PreguntaFuncs.create(session, body, title, username)
        res:dict = {
            "qid":res.qid,
            "title":res.title,
            "timestamp":res.timestamp,
            "body":res.body,
            "owner":{"username":res.username}
        }
        
        schema.remove_session()
        return res



    @staticmethod
    def existe_pregunta(schema: Schema,qid:int) -> bool:
        session: Session = schema.new_session()
        preg: Pregunta = PreguntaFuncs.get_pregunta(session, qid)
        schema.remove_session()
        if not preg:
            return False
        else:
            return True

    @staticmethod
    def ocultarPreg(schema: Schema, id: int):
        """Oculta la pregunta
        """
        session: Session = schema.new_session()

        preg = PreguntaFuncs.get_pregunta(session,id)
        preg.hidden = True

        session.add(preg)
        session.commit()

        schema.remove_session()

