from pathlib import Path

from pylamine import get_sheet_data, get_sheet_names, get_sheets

PATH = Path(__file__).parent / "data"
SHEET_INDEX = 0


def test_ods_read(ods_sheet_names, ods_rows) -> None:
    assert ods_sheet_names == get_sheet_names((PATH / "base.ods").as_posix())
    assert ods_rows[SHEET_INDEX] == get_sheet_data(
        (PATH / "base.ods").as_posix(), SHEET_INDEX
    )
    assert list(zip(ods_sheet_names, ods_rows)) == get_sheets(
        (PATH / "base.ods").as_posix()
    )


def test_xls_read(xls_sheet_names, xls_rows) -> None:
    assert xls_sheet_names == get_sheet_names((PATH / "base.xls").as_posix())
    assert xls_rows[SHEET_INDEX] == get_sheet_data(
        (PATH / "base.xls").as_posix(), SHEET_INDEX
    )
    assert list(zip(xls_sheet_names, xls_rows)) == get_sheets(
        (PATH / "base.xls").as_posix()
    )


def test_xlsx_read(xlsx_sheet_names, xlsx_rows) -> None:
    assert xlsx_sheet_names == get_sheet_names((PATH / "base.xlsx").as_posix())
    assert xlsx_rows[SHEET_INDEX] == get_sheet_data(
        (PATH / "base.xlsx").as_posix(), SHEET_INDEX
    )
    assert list(zip(xlsx_sheet_names, xlsx_rows)) == get_sheets(
        (PATH / "base.xlsx").as_posix()
    )
