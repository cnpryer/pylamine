from typing import List

from pylamine import get_sheet_data, get_sheet_names, get_sheets
from pylamine.type import CalamineRow

from . import DATA_DIR, DEFAULT_SHEET_INDEX


def test_base_files(
    base_file_sheet_names: List[str],
    ods_rows: List[List[CalamineRow]],
    xls_rows: List[List[CalamineRow]],
    xlsx_rows: List[List[CalamineRow]],
) -> None:
    test_data = (
        ("base.ods", ods_rows),
        ("base.xls", xls_rows),
        ("base.xlsx", xlsx_rows),
    )

    for (name, rows) in test_data:
        filepath = (DATA_DIR / name).as_posix()

        assert rows[DEFAULT_SHEET_INDEX] == get_sheet_data(
            filepath, DEFAULT_SHEET_INDEX
        )
        assert base_file_sheet_names == get_sheet_names(filepath)
        assert list(zip(base_file_sheet_names, rows)) == get_sheets(filepath)
