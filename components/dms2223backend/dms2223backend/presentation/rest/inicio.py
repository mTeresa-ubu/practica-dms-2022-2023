""" REST API controllers responsible of handling the server operations.
"""

import json
import time
from typing import Dict, Tuple, Optional
from http import HTTPStatus
from flask import current_app

def test_inicio() -> Tuple[str,Optional[int]]:
    return ('Hola', HTTPStatus.OK)
