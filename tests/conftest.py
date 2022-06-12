from datetime import date
from typing import List

from pytest import fixture

from pylamine.type import CalamineRow


@fixture
def ods_rows() -> List[List[CalamineRow]]:
    return [[["String", 1, 1.1, True, False]], []]


@fixture
def ods_sheet_names() -> List[str]:
    return ["Sheet1", "Sheet2"]


@fixture
def xls_rows() -> List[List[CalamineRow]]:
    return [[["String", 1, 1.1, True, False]], []]


@fixture
def xls_sheet_names() -> List[str]:
    return ["Sheet1", "Sheet2"]


@fixture
def xlsx_rows() -> List[List[CalamineRow]]:
    return [[["String", 1, 1.1, True, False, date(2020, 1, 1)]], []]


@fixture
def xlsx_sheet_names() -> List[str]:
    return ["Sheet1", "Sheet2"]
