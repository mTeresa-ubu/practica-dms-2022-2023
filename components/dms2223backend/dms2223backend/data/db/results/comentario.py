from sqlalchemy import Enum
from typing import Dict
from sqlalchemy import Table, MetaData, Column
from sqlalchemy import String, func 
from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship 

from dms2223backend.data.db.results.resultbase import ResultBase

from sqlalchemy import Integer

from datetime import datetime
from dms2223backend.data.sentiment import Sentiment

from dms2223backend.data.db.results.votoCom import VotoCom
from dms2223backend.data.db.results.reporteCom import ReporteCom


class Comentario(ResultBase):

    def __init__(self, username: str, body: str, aid: int, sentiment: Sentiment):

        self.username: str = username
        self.body: str = body
        self.aid: int = aid
        self.id: int 
        self.timestamp: DateTime  = datetime.timestamp(datetime.now())
        self.oculto: bool
        self.sentiment: Sentiment = sentiment
        
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
              'comments',
              metadata,
              Column('username', String(32)),
              Column('body', String(350), nullable=False), #Nunca puede ser null
              Column('aid', Integer, ForeignKey('answers.id'), nullable=False),
              Column('id', Integer, autoincrement=True, primary_key=True), #Cada nuevo registro, +1
              Column('timestamp', DateTime, nullable=False),
              Column('oculto', Boolean, default=False),
              Column('sentiment', Enum(Sentiment)) 

        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.

          Returns:
              - Dict: A dictionary with the mapping properties.
        """
        return {
             'rel_reportes_2': relationship(ReporteCom, backref='comments'),
             'rel_votos2': relationship(VotoCom, backref='comments')
             
        }

       