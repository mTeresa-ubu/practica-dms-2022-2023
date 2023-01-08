from dms2223frontend.data.rest.backendservice import BackendService
from flask import session
from dms2223common.data.rest import ResponseData

class WebAnswer():  
    def get_answers(backend_service: BackendService,username:str,qid:int):
        response: ResponseData = backend_service.list_answers_for_a_question(session.get('token'),qid)
        WebUtils.flash_response_messages(response)
        return response.get_content()