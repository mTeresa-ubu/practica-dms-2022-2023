from http import HTTPStatus
from typing import Tuple, Optional


def head() -> Tuple[None, Optional[int]]:
   return (None, HTTPStatus.NO_CONTENT.value)