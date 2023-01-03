from typing import List,Dict
from sqlalchemy import Table, MetaData, Column
from sqlalchemy import String, func 
from sqlalchemy import Boolean, DateTime, ForeignKey,PickleType
from sqlalchemy.orm import relationship 

from dms2223backend.data.db.results.resultbase import ResultBase

from sqlalchemy import Integer

from datetime import datetime

from dms2223backend.data.db.results.reporteRes import ReporteRes
from dms2223backend.data.db.results.votoRes import VotoRes
from dms2223backend.data.db.results.comentario import Comentario


class Respuesta(ResultBase):

    def __init__(self, body: Dict,username: str,qid:int):

        self.username: str = username
        self.qid: int = qid
        self.body: str = body['body']
        self.timestamp: DateTime
        self.id: int 
        self.oculto: bool
        
    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ Gets the table definition.

          Args:
              - metadata (MetaData): The database schema metadata
                          (used to gather the entities' definitions and mapping)

          Returns:
              - Table: A `Table` object with the table definition.
        """
        return Table(
              'answers',
              metadata,
              Column('username', String(32)),
              Column('body', String(350), nullable=False), #Nunca puede ser null
              Column('qid', Integer, ForeignKey('questions.qid'), nullable=False),
              Column('id', Integer, autoincrement=True, primary_key=True), #Cada nuevo registro, +1
              Column('timestamp', DateTime, nullable=False, default=func.now()),
              Column('oculto', Boolean, default=False),

        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.

          Returns:
              - Dict: A dictionary with the mapping properties.
        """
        return {
             'rel_comentarios': relationship(Comentario, backref='answers'),
             'rel_reportes': relationship(ReporteRes, backref='answers'),
             #'rel_votos': relationship(VotoRes, backref='answers')
             
        }

       