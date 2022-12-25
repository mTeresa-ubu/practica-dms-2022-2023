from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db.schema import Schema 
from dms2223backend.data.db.results import Pregunta
from dms2223backend.data.db.resultsets import PreguntaFuncs


#from dms2223backend.logic.answerlogic import AnswerLogic
#from dms2223backend.logic.exc.forbiddenoperationerror import ForbiddenOperationError


class preguntaLogic():
    
    def get_pregunta(schema: Schema, qid: int) -> dict:
        
        session: Session = schema.new_session()
        
        try:
            nueva: Pregunta = PreguntaFuncs.get_pregunta(session, qid)
        except Exception as exception:
         raise exception
        schema.remove_session()
        return nueva