from typing import List, Dict, Optional
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.db.schema import Schema 
from dms2223backend.data.db.results import Pregunta
from dms2223backend.data.db.resultsets import pregunta_res


from dms2223backend.logic.answerlogic import AnswerLogic
from dms2223backend.logic.exc.forbiddenoperationerror import ForbiddenOperationError


class preguntaLogic():
    
    def create() -> dict:
        try:
            nueva: Pregunta = pregunta_res.create
        except Exception as exception:
         raise exception

        return nueva