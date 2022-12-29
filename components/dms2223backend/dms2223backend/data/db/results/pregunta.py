from typing import Dict
from sqlalchemy import Table, MetaData, Column
from sqlalchemy import String, func 
from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship 

from dms2223backend.data.db.results.resultbase import ResultBase

from sqlalchemy import Integer

from datetime import datetime

from dms2223backend.data.db.results.respuesta import Respuesta
from dms2223backend.data.db.results.reporteRes import ReporteRes

class Pregunta(ResultBase):
      

    def __init__(self, username: str, body: str, title: str, oculto: bool):

        self.username: str = username
        self.body: str = body
        self.title: str = title
        self.qid: int
        self.timestamp: DateTime
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
              'questions',
              metadata,
              Column('username', String(32)),
              Column('body', String(350), nullable=False), #Nunca puede ser null
              Column('title', String(100), nullable=False),
              Column('qid', Integer, autoincrement=True, primary_key=True), #Cada nuevo registro, +1
              Column('timestamp', DateTime, nullable=False, default=func.now()),
              Column('oculto', Boolean, default=False)
        )

    @staticmethod
    def _mapping_properties() -> dict:
        """ Gets the mapping properties dictionary.

          Returns:
              - Dict: A dictionary with the mapping properties.
        """
        return {
             'rel_respuestas': relationship(Respuesta, backref='questions'),
             #'rel_reportes2': relationship(ReporteRes, backref='questions')   
        }

       