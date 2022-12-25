from sqlalchemy import Enum
from typing import Dict
from sqlalchemy import Table, MetaData, Column
from sqlalchemy import String, ForeignKey

from dms2223backend.data.db.results.resultbase import ResultBase

from sqlalchemy import Integer

class VotoCom(ResultBase):

    def __init__(self, username: str, aid: int,):

        self.username: str = username
        self.aid: int = aid 
        
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
              'votesCom',
              metadata,
              Column('username', String(32), nullable=False, primary_key=True),
              Column('aid', Integer, ForeignKey('comments.id'), nullable=False, primary_key=True) #primary key compuesta que definimos anterioremente

        )
    
    __mapper_args__ = {
        'polymorphic_identity': 'votesCom',
    }

    

       