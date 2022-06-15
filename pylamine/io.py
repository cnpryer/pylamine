from io import BytesIO
from pathlib import Path
from typing import BinaryIO, List, Tuple

from pylamine.error import InvalidParameterError, UnimplmentedError
from pylamine.pylamine import get_sheet_data as _get_sheet_data
from pylamine.pylamine import (
    get_sheet_data_with_name as _get_sheet_data_with_name,
)
from pylamine.pylamine import get_sheet_names as _get_sheet_names
from pylamine.pylamine import get_sheets as _get_sheets
from pylamine.type import CalamineRow, FileLike, SheetLike
from pylamine.utils import format_path


def process_file_like(file_like: FileLike) -> FileLike:
    # if given a path, format it
    if isinstance(file_like, (str, Path)):
        file_like = format_path(file_like)

    elif isinstance(file_like, (BytesIO, BinaryIO, bytes)):
        raise UnimplmentedError("File objects are not currently supported.")

    else:
        raise InvalidParameterError("FileLike value is not supported.")

    return file_like


def get_sheet_data(file_like: FileLike, sheet: SheetLike) -> List[CalamineRow]:
    file_like = process_file_like(file_like)

    # if given the name of the sheet, use _get_sheet_data_with_name
    if isinstance(sheet, (str,)):
        return _get_sheet_data_with_name(file_like, sheet)

    return _get_sheet_data(file_like, sheet)


def get_sheet_names(file_like: FileLike) -> List[str]:
    file_like = process_file_like(file_like)

    return _get_sheet_names(file_like)


def get_sheets(
    file_like: FileLike,
) -> List[Tuple[str, List[CalamineRow]]]:
    file_like = process_file_like(file_like)

    return _get_sheets(file_like)
