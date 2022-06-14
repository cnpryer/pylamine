from datetime import date, datetime, time
from io import BytesIO
from pathlib import Path
from typing import BinaryIO, List, Union

CalamineCell = Union[int, float, str, bool, time, date, datetime]
CalamineRow = List[CalamineCell]
FileLike = Union[str, BytesIO, Path, BinaryIO, bytes]
SheetLike = Union[str, int]
PathLike = Union[str, Path]

__all__ = ["CalamineCell", "CalamineRow", "FileLike", "SheetLike"]
