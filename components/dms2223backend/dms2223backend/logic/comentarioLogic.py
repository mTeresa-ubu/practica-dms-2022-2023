from sqlalchemy import Integer
from dms2223backend.data.db.results import Comentario
from dms2223backend.data.db.resultsets import ComentarioFuncs

class comentarioLogic():
    def get_comentario() -> Comentario:
        try:
            nueva: Comentario = Comentario
        except Exception as exception:
         raise exception

        return nueva