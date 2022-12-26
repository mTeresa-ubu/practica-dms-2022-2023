from typing import List, Dict, ClassVar
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db import Schema


from dms2223backend.data.db.resultsets.pregunta_res import PreguntaFuncs

from sqlalchemy import select

class RespuestasServicio():
    @staticmethod
    def get_answers(schema:Schema,qid:int) -> List[Dict]:
        """ Construye la lista de respuestas (y comentarios) a una pregunta
        """
        session: Session = schema.new_session()
        res = PreguntaFuncs.get_pregunta(session=session,qid=qid)
        
        answers:List[Dict] = []

        # for answer in res.respuestas:
        #     session.refresh(answer)

        #     comentarios:List = []
        #     for comm in answer.comentarios:
        #         comentarios.append({
        #             "id":comm.id_comentario,
        #             "aid":answer.id_respuesta,
        #             "timestamp":comm.fecha,
        #             "body":comm.contenido,
        #             "owner":{"username":comm.autor.nombre},
        #             "votes":3,
        #             "sentiment":"POSITIVE"
        #         })

        #     answers.append({
        #         "id":answer.id_respuesta,
        #         "qid":qid,
        #         "timestamp":answer.fecha,
        #         "body":answer.contenido,
        #         "owner":{"username":answer.autor.nombre},
        #         "comments":comentarios
        #     })

        schema.remove_session()    
        return answers

    # def get_all_reports(schema:Schema) -> list:
    #     """ Transforma los reportes en una lista
    #     """
    #     session: Session = schema.new_session()
    #     reports:List = []
    #     res = ReporteFuncs.get_question_reps(session)
    #     for rep in res:
    #         reports.append({
    #             "id":rep.id_reporte,
    #             "qid":rep.id_pregunta,
    #             "reason":rep.razon_reporte,
    #             "status":rep.estado.name,
    #             "owner":{"username":rep.autor.nombre},
    #             "timestamp":rep.fecha
    #         })
    #     schema.remove_session()  
    #     return reports

    # def set_report(schema:Schema,reporte:Dict) -> Dict:
    #     session: Session = schema.new_session()

    #     p = PreguntaFuncs.get(session,reporte["qid"])
    #     usu = UsuarioFuncs.get_or_create(
    #         session=session,
    #         nombre=reporte["autor"])
    #     session.refresh(usu)

    #     rep:ReportePregunta = ReportePregunta(
    #         pregunta=p,
    #         razon_reporte=reporte["razon_reporte"],
    #         autor=usu
    #     )

    #     rep = ReporteFuncs.create_question_reps(session,rep)
    #     resp:Dict = {
    #         "id":rep.id_reporte,
    #         "qid":rep.id_pregunta,
    #         "reason":rep.razon_reporte,
    #         "status":rep.estado.name,
    #         "owner":{"username":rep.autor.nombre},
    #         "timestamp":rep.fecha
    #     }
    #     schema.remove_session()
    #     return resp