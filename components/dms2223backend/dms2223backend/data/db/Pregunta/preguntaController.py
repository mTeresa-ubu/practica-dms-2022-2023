from dms2223backend.data.config import BackendConfiguration
from dms2223backend.data.db import Base, Schema
from dms2223backend.data.db import Usuario, Pregunta, Reporte, Respuesta, Comentario, Voto, Feedback

from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy import select, Table, Column, Integer, String, MetaData # type: ignore

session:Session = db.new_session()
cfg: BackendConfiguration = BackendConfiguration()
cfg.load_from_file(cfg.default_config_file())
db: Schema = Schema(base=Base,config=cfg)

class PreguntaController():
    
    def retornar_pregunta(id_pr):
        stmt = select(Pregunta).where(Pregunta.id_pregunta == id_pr)
        result = session.execute(stmt).first()
        return result[0]

