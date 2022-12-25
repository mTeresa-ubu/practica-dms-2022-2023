from enum import Enum
from typing import Dict
from sqlalchemy import Table, MetaData, Column
from sqlalchemy import String, func 
from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship 

from dms2223backend.data.db.results.resultbase import ResultBase

from sqlalchemy import Integer

from dms2223backend.data.reportstatus import ReportStatus


class Reporte(ResultBase):     

    def __init__(self, username: str, reason: str, tipo: str, eid: int, status: ReportStatus):

        self.username: str = username
        self.reason: str = reason
        self.tipo: str = tipo
        self.id: int
        self.eid: int = eid
        self.status: ReportStatus = status

        
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
              'reports',
              metadata,
              Column('username', String(32)),
              Column('reason', String(350), nullable=False), #Nunca puede ser null
              Column('tipo', String(32), nullable=False),
              Column('id', Integer, autoincrement=True, primary_key=True), #Cada nuevo registro, +1
              Column('eid', Integer, nullable=False),
              Column('status', Enum(ReportStatus))
        )

    """"
    No lo necesitamos
    @staticmethod
    def _mapping_properties() -> Dict:

    """


       