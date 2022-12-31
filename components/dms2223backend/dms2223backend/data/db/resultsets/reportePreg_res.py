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
from dms2223backend.data.reportstatus import ReportStatus



class ReporteRes(ResultBase):

    def __init__(self, username: str, reason: str, aid: int, status: ReportStatus):

        self.username: str = username
        self.reason: str = reason
        self.aid: int = aid 
        self.id: int
        #self.timestamp: DateTime  = datetime.timestamp(datetime.now())
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
              'reportsRes',
              metadata,
              Column('username', String(32), nullable=False),
              Column('reason', String(350), nullable=False), #Nunca puede ser null
              Column('aid', Integer, ForeignKey('answers.id'), nullable=False),
              Column('id', Integer, autoincrement=True, primary_key=True), #Cada nuevo registro, +1
              #Column('timestamp', DateTime, nullable=False),
              Column('status', Enum(ReportStatus), nullable=False, default=ReportStatus.PENDING)

        )
    
    __mapper_args__ = {
        'polymorphic_identity': 'reportsRes',
    }

    

       