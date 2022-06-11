import csv
from io import StringIO
from pathlib import Path

import polars as pl

import pylamine

PATH = Path(__file__).parent / "data"


def test_read_excel() -> None:
    # use StringIO buffer to build DataFrame
    buffer = StringIO()

    # parse rows from default sheet
    rows = pylamine.get_sheet_data((PATH / "df.xlsx").as_posix(), 0)

    writer = csv.writer(buffer, quoting=csv.QUOTE_ALL)
    for row in rows:
        writer.writerow([_ for _ in row])

    # reset buffer
    buffer.seek(0)

    df = pl.read_csv(buffer)

    assert not df.is_empty()
