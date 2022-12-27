"""REST API controllers responsible of handling the server operations about reports
"""

import json
import time
from typing import Dict, Tuple, Optional, List
from http import HTTPStatus
from flask import current_app

from sqlalchemy.orm.session import Session # type: ignore

from dms2223backend.data.db.resultsets.reporteCom_res import ReporteComFuncs
from dms2223backend.data.db.resultsets.reportePreg_res import ReportePregFuncs
from dms2223backend.data.db.resultsets.reporteRes_res import ReporteResFuncs
from dms2223backend.service.servicioReportes import ServicioReporte


from flask import current_app

import requests

# Rober Lastras

class reportsPresentation():
    def init(self) -> None:
        pass

def list_reportsCom() -> Tuple[List[Dict], Optional[int]]:
    pass
def get_reportsCom() -> Tuple[List[Dict], Optional[int]]:
    pass
def create_repCom(body: Dict, token_info: Dict) -> Tuple[str,Optional[int]]:
    pass

def list_reportsPreg() -> Tuple[List[Dict], Optional[int]]:
    pass
def get_reportsPreg() -> Tuple[List[Dict], Optional[int]]:
    pass

def create_repPreg(body: Dict, token_info: Dict) -> Tuple[str,Optional[int]]:
    pass

def list_reportsRes() -> Tuple[List[Dict], Optional[int]]:
    pass
def get_reportsRes() -> Tuple[List[Dict], Optional[int]]:
    pass

def create_repRes(body: Dict, token_info: Dict) -> Tuple[str,Optional[int]]:
    pass