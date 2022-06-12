from datetime import date
from typing import Dict, List

from pytest import fixture

from pylamine.type import CalamineRow

# base files for ods and xls have the same row data, but
# xlsx is read with dates. all files have the same sheet
# names ("Sheet1", "Sheet2").
# a df.xlsx was added for special use cases.


@fixture
def df_file_sheet_names() -> List[str]:
    return ["Sheet1"]


@fixture
def df_file_rows() -> List[CalamineRow]:
    return [["a", "b", "c"], [0, "foo", 1], [1, "bar", 2], [2, "ham", 3]]


@fixture
def df_file_dict() -> Dict[str, CalamineRow]:
    return {"a": [0, 1, 2], "b": ["foo", "bar", "ham"], "c": [1, 2, 3]}


@fixture
def base_file_sheet_names() -> List[str]:
    return ["Sheet1", "Sheet2"]


@fixture
def ods_rows() -> List[List[CalamineRow]]:
    return [[["String", 1, 1.1, True, False]], []]


@fixture
def xls_rows() -> List[List[CalamineRow]]:
    return [[["String", 1, 1.1, True, False]], []]


@fixture
def xlsx_rows() -> List[List[CalamineRow]]:
    return [[["String", 1, 1.1, True, False, date(2020, 1, 1)]], []]
