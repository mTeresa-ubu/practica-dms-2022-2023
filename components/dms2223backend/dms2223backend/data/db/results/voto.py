from enum import Enum
from typing import Dict
from sqlalchemy import Table, MetaData, Column
from sqlalchemy import String, func 
from sqlalchemy import Boolean, DateTime, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship 

from dms2223backend.data.db.results.resultbase import ResultBase
from sqlalchemy import Integer
from dms2223backend.data.reportstatus import ReportStatus


class Voto(ResultBase):     

    def __init__(self, username: str, eid: int, tipo: str):

        self.username: str = username
        self.tipo: str = tipo
        self.eid: int = eid
        
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
            'votes',
            metadata,
            Column('username', String(32)),
            Column('tipo', String(32), nullable=False),
            Column('eid', Integer, ForeignKeyConstraint(Voto.eid,Voto.username)) 
        )

    """"
    No lo necesitamos
    @staticmethod
    def _mapping_properties() -> Dict:

    """


       