from typing import Dict
from sqlalchemy import Table, MetaData, Column
from sqlalchemy import String, func 
from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship 

from dms2223backend.data.db.results.resultbase import ResultBase

from sqlalchemy import Integer

#from dms2223backend.data.db.results.report. import FALTAN MAS

#class Respuesta(ResultBase):
##TODOCAMBIAR DE AQUÍ PARA ABAJO
    #def __init__(self, username: str, password: str):

    #      self.username: str = username
    #      self.password: str = password
        
    # @staticmethod
    # def _table_definition(metadata: MetaData) -> Table:
    #      """ Gets the table definition.

    #      Args:
    #          - metadata (MetaData): The database schema metadata
    #                      (used to gather the entities' definitions and mapping)

    #      Returns:
    #          - Table: A `Table` object with the table definition.
    #      """
    #      return Table(
    #          'users',
    #          metadata,
    #          Column('username', String(32), primary_key=True),
    #          Column('password', String(64), nullable=False)
    #      )

    # @staticmethod
    # def _mapping_properties() -> Dict:
    #      """ Gets the mapping properties dictionary.

    #      Returns:
    #          - Dict: A dictionary with the mapping properties.
    #      """
    #      return {
    #          'rights': relationship(UserRole, backref='user')
    #      }