import csv
from io import StringIO
from typing import Dict, List

import polars as pl

from pylamine import get_sheet_data, get_sheet_names
from pylamine.type import CalamineCell

from . import DATA_DIR, DEFAULT_SHEET_INDEX


def get_df(filepath: str) -> pl.DataFrame:
    # use StringIO buffer to build DataFrame
    buffer = StringIO()

    # parse rows from default sheet
    rows = get_sheet_data(filepath, DEFAULT_SHEET_INDEX)

    writer = csv.writer(buffer, quoting=csv.QUOTE_ALL)
    for row in rows:
        writer.writerow([_ for _ in row])

    # reset buffer
    buffer.seek(0)

    df = pl.read_csv(buffer)

    return df


def test_read_excel(
    df_file_sheet_names: List[str], df_file_dict: Dict[str, List[CalamineCell]]
) -> None:
    filepath = (DATA_DIR / "df.xlsx").as_posix()
    sheet_names = get_sheet_names(filepath)
    assert sheet_names == df_file_sheet_names

    df = get_df(filepath)
    assert not df.is_empty()
    assert df.frame_equal(pl.DataFrame(df_file_dict))
