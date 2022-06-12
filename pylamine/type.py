from datetime import date, datetime, time
from typing import List

__all__ = ["CalamineRow"]

CalamineRow = List[int | float | str | bool | time | date | datetime]
