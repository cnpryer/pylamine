from __future__ import annotations

from datetime import date, datetime, time
from typing import List

__version__: str = ""

def get_sheet_data(
    path: str, sheet: int
) -> List[List[int | float | str | bool | time | date | datetime]]: ...
def get_sheet_names(path: str) -> List[str]: ...

class CalamineError(Exception): ...
