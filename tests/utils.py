from pathlib import Path

from pylamine.type import PathLike
from pylamine.utils import format_path

from . import DATA_DIR


def create_filepath(filename: str, directory: PathLike = DATA_DIR) -> PathLike:
    if isinstance(directory, (str,)):
        directory = Path(directory)

    return format_path((directory / filename).as_posix())
