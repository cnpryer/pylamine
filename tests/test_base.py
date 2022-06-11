from datetime import date
from pathlib import Path

from pylamine import get_sheet_data, get_sheet_names, get_sheets

PATH = Path(__file__).parent / "data"


def test_ods_read() -> None:
    names = ["Sheet1", "Sheet2"]
    data = [["String", 1, 1.1, True, False]]
    sheets = [
        ("Sheet1", [["String", 1, 1.1, True, False]]),
        ("Sheet2", []),
    ]

    assert names == get_sheet_names((PATH / "base.ods").as_posix())
    assert data == get_sheet_data((PATH / "base.ods").as_posix(), 0)
    assert sheets == get_sheets((PATH / "base.ods").as_posix())


def test_xls_read() -> None:
    names = ["Sheet1", "Sheet2"]
    data = [["String", 1, 1.1, True, False]]
    sheets = [
        ("Sheet1", [["String", 1, 1.1, True, False]]),
        ("Sheet2", []),
    ]

    assert names == get_sheet_names((PATH / "base.xls").as_posix())
    assert data == get_sheet_data((PATH / "base.xls").as_posix(), 0)
    assert sheets == get_sheets((PATH / "base.xls").as_posix())


def test_xlsx_read() -> None:
    names = ["Sheet1", "Sheet2"]
    data = [["String", 1, 1.1, True, False, date(2020, 1, 1)]]
    sheets = [
        ("Sheet1", [["String", 1, 1.1, True, False, date(2020, 1, 1)]]),
        ("Sheet2", []),
    ]

    assert names == get_sheet_names((PATH / "base.xlsx").as_posix())
    assert data == get_sheet_data((PATH / "base.xlsx").as_posix(), 0)
    assert sheets == get_sheets((PATH / "base.xlsx").as_posix())
