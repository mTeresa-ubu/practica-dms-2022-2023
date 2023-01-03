from sqlalchemy import Enum, Table, MetaData, Column
from sqlalchemy import String, Integer, func 
from sqlalchemy import DateTime, ForeignKey

from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223backend.data.reportstatus import ReportStatus

from datetime import datetime


class ReportePreg(ResultBase):

    def __init__(self, username: str, reason: str, qid: int, status: ReportStatus):

        self.username: str = username
        self.reason: str = reason
        self.qid: int = qid 
        self.id: int
        self.timestamp: DateTime
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
              'reportsPreg',
              metadata,
              Column('username', String(32), nullable=False),
              Column('reason', String(350), nullable=False), #Nunca puede ser null
              Column('qid', Integer, ForeignKey('questions.qid'), nullable=False),
              Column('id', Integer, autoincrement=True, primary_key=True), #Cada nuevo registro, +1
              Column('timestamp', DateTime, nullable=False, default=func.now()),
              Column('status', Enum(ReportStatus), nullable=False, default=ReportStatus.PENDING)

        )
    
    __mapper_args__ = {
        'polymorphic_identity': 'reportsPreg',
    }
