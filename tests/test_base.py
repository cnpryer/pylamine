from typing import List

from pylamine import get_sheet_data, get_sheet_names, get_sheets
from pylamine.type import CalamineRow

from .utils import create_filepath


def test_get_sheet_data_ods(ods_file_rows: List[List[CalamineRow]]) -> None:
    path, sheet = create_filepath("base.ods"), 0
    rows = ods_file_rows[sheet]
    assert rows == get_sheet_data(path, sheet=sheet)
    assert rows == get_sheet_data(path, sheet="Sheet1")


def test_get_sheet_data_xls(xls_file_rows: List[List[CalamineRow]]) -> None:
    path, sheet = create_filepath("base.xls"), 0
    rows = xls_file_rows[sheet]
    assert rows == get_sheet_data(path, sheet=sheet)
    assert rows == get_sheet_data(path, sheet="Sheet1")


def test_get_sheet_data_xlsx(xlsx_file_rows: List[List[CalamineRow]]) -> None:
    path, sheet = create_filepath("base.xlsx"), 0
    rows = xlsx_file_rows[sheet]
    assert rows == get_sheet_data(path, sheet=sheet)
    assert rows == get_sheet_data(path, sheet="Sheet1")


def test_get_sheet_names_ods(ods_file_sheet_names: List[str]) -> None:
    path = create_filepath("base.ods")
    assert ods_file_sheet_names == get_sheet_names(path)


def test_get_sheet_names_xls(xls_file_sheet_names: List[str]) -> None:
    path = create_filepath("base.xls")
    assert xls_file_sheet_names == get_sheet_names(path)


def test_get_sheet_names_xlsx(xlsx_file_sheet_names: List[str]) -> None:
    path = create_filepath("base.xlsx")
    assert xlsx_file_sheet_names == get_sheet_names(path)


# NOTE: order is currently not preserved using get_sheets


def test_get_sheets_ods(
    ods_file_sheet_names: List[str], ods_file_rows: List[List[CalamineRow]]
) -> None:
    path = create_filepath("base.ods")
    expected = list(zip(ods_file_sheet_names, ods_file_rows))
    res = get_sheets(path)
    assert res == expected


def test_get_sheets_xls(
    xls_file_sheet_names: List[str], xls_file_rows: List[List[CalamineRow]]
) -> None:
    path = create_filepath("base.xls")
    expected = list(zip(xls_file_sheet_names, xls_file_rows))
    res = get_sheets(path)
    assert res == expected


def test_get_sheets_xlsx(
    xlsx_file_sheet_names: List[str], xlsx_file_rows: List[List[CalamineRow]]
) -> None:
    path = create_filepath("base.xlsx")
    expected = list(zip(xlsx_file_sheet_names, xlsx_file_rows))
    res = get_sheets(path)
    assert res == expected
