from typing import List, Tuple

from pylamine.pylamine import get_sheet_data as _get_sheet_data
from pylamine.pylamine import get_sheet_names as _get_sheet_names
from pylamine.pylamine import get_sheets as _get_sheets
from pylamine.type import CalamineRow


def get_sheet_data(path: str, sheet: int) -> List[CalamineRow]:
    return _get_sheet_data(path, sheet)


def get_sheet_names(path: str) -> List[str]:
    return _get_sheet_names(path)


def get_sheets(
    path: str,
) -> List[Tuple[str, List[CalamineRow]]]:
    return _get_sheets(path)
