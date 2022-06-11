from __future__ import annotations

from datetime import date, datetime, time
from io import BufferedReader
from typing import List, Tuple

__version__ = ""

def get_sheet_data(
    path: str, sheet: int
) -> List[List[int | float | str | bool | time | date | datetime]]: ...
def get_sheet_names(path: str) -> List[str]: ...
def get_sheets(
    path: str,
) -> List[
    Tuple[str, List[List[int | float | str | bool | time | date | datetime]]]
]: ...

class CalamineError(Exception): ...
