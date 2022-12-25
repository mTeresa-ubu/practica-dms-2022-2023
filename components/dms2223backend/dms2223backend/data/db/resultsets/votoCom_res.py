# from typing import List, Dict, Optional

# from dms2223backend.data.db.results import Respuesta

# from sqlalchemy.orm.session import Session  # type: ignore
# from sqlalchemy import select # type: ignore


# class VotoFuncs():

#     @staticmethod
#     def create(session:Session,username: str, body: str, qid: int) -> Respuesta: 
#         if not body:
#             raise ValueError('Campo contenido vacío.')
#         nueva = Respuesta(username,body,qid, oculto=False) 

#         session.add(nueva)
#         session.commit()
#         return nueva
        
#     @staticmethod
#     def get_respuesta(session:Session,qid:int) -> Respuesta:
#         stmt = session.query(Respuesta).where(Respuesta.qid == qid).first()
#         return stmt

#     @staticmethod
#     def list_all(session: Session,qid:int) -> List[Dict]:
#         stmt = session.query(Respuesta).where(Respuesta.qid == qid).all()
#         return stmt

    

    