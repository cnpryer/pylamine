mod parse;
mod utils;
use std::fs::File;
use std::io::BufReader;

use calamine::{open_workbook_auto, DataType, Error, Reader, Sheets};
use pyo3::create_exception;
use pyo3::exceptions::*;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

use utils::CellValue;

const VERSION: &str = "0.1.1";

create_exception!(python_calamine, CalamineError, PyException);

fn _get_sheet_data(path: &str, sheet: usize) -> Result<Vec<Vec<CellValue>>, Error> {
    let mut excel: Sheets = open_workbook_auto(path)?;
    let range = excel.worksheet_range_at(sheet).unwrap()?;
    let res = parse::parse_range(range);
    Ok(res)
}

#[pyfunction]
#[pyo3(text_signature = "path: str, sheet: int")]
fn get_sheet_data(path: &str, sheet: usize) -> PyResult<Vec<Vec<CellValue>>> {
    match _get_sheet_data(path, sheet) {
        Ok(r) => Ok(r),
        Err(e) => match e {
            Error::Io(err) => Err(PyIOError::new_err(err.to_string())),
            _ => Err(CalamineError::new_err(e.to_string())),
        },
    }
}

fn _get_sheet_names(path: &str) -> Result<Vec<String>, Error> {
    let excel: Sheets = open_workbook_auto(path)?;
    Ok(excel.sheet_names().to_vec())
}

#[pyfunction]
#[pyo3(text_signature = "path: str")]
fn get_sheet_names(path: &str) -> PyResult<Vec<String>> {
    match _get_sheet_names(path) {
        Ok(r) => Ok(r),
        Err(e) => match e {
            Error::Io(err) => Err(PyIOError::new_err(err.to_string())),
            _ => Err(CalamineError::new_err(e.to_string())),
        },
    }
}

fn _get_sheets(path: &str) -> Result<Vec<(String, Vec<Vec<CellValue>>)>, Error> {
    let mut res = Vec::new();
    let sheets = get_sheet_names(path).unwrap();
    for (i, name) in sheets.iter().enumerate() {
        let sheet_data = get_sheet_data(path, i as usize);
        res.push((name.to_owned(), sheet_data.unwrap()))
    }

    Ok(res)
}

#[pyfunction]
#[pyo3(text_signature = "path: str")]
fn get_sheets(path: &str) -> PyResult<Vec<(String, Vec<Vec<CellValue>>)>> {
    match _get_sheets(path) {
        Ok(r) => Ok(r),
        Err(e) => match e {
            Error::Io(err) => Err(PyIOError::new_err(err.to_string())),
            _ => Err(CalamineError::new_err(e.to_string())),
        },
    }
}

#[pymodule]
fn pylamine(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_sheet_data, m)?)?;
    m.add_function(wrap_pyfunction!(get_sheet_names, m)?)?;
    m.add_function(wrap_pyfunction!(get_sheets, m)?)?;
    m.add("CalamineError", py.get_type::<CalamineError>())?;
    m.add("__version__", VERSION)?;
    Ok(())
}
