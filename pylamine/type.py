from datetime import date, datetime, time
from typing import List

__all__ = ["CalamineCell", "CalamineRow"]

CalamineCell = int | float | str | bool | time | date | datetime
CalamineRow = List[CalamineCell]
