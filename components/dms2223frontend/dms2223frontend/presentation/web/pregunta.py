from flask import session
from dms2223common.data.rest import ResponseData
from dms2223frontend.data.rest.backendservice import BackendService
from .webutils import WebUtils
from typing import Optional, Dict

class PreguntaWeb():
    @staticmethod
    def nueva_pregunta(backend_service: BackendService, title: str, body: str) -> Optional[Dict]:
        response: ResponseData = backend_service.create_preg(body, session.get('token'), title)
        WebUtils.flash_response_messages(response)
        if response is not None:
            return response.get_content()
        else:
            return None
    
    @staticmethod
    def nuevo_reportePreg(backend_service: BackendService, qid: str, reason: str) -> Optional[Dict]:
        response: ResponseData = backend_service.create_reportePreg(qid, reason, session.get('token'))
        WebUtils.flash_response_messages(response)
        
        return response.get_content()
    