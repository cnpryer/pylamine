mod parse;
mod utils;

use std::collections::HashMap;

use calamine::{open_workbook_auto, Error, Reader};
use pyo3::create_exception;
use pyo3::exceptions::*;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

use utils::CellValue;

create_exception!(python_calamine, CalamineError, PyException);

fn _get_sheet_data(path: &str, sheet: usize) -> Result<Vec<Vec<CellValue>>, Error> {
    let mut book = open_workbook_auto(path)?;
    let range = book.worksheet_range_at(sheet).unwrap()?;
    let res = parse::parse_range(&range);
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

fn _get_sheet_data_with_name(path: &str, sheet: &str) -> Result<Vec<Vec<CellValue>>, Error> {
    let mut book = open_workbook_auto(path)?;
    let range = book.worksheet_range(sheet).unwrap()?;
    let res = parse::parse_range(&range);
    Ok(res)
}

#[pyfunction]
#[pyo3(text_signature = "path: str, sheet: str")]
fn get_sheet_data_with_name(path: &str, sheet: &str) -> PyResult<Vec<Vec<CellValue>>> {
    match _get_sheet_data_with_name(path, sheet) {
        Ok(r) => Ok(r),
        Err(e) => match e {
            Error::Io(err) => Err(PyIOError::new_err(err.to_string())),
            _ => Err(CalamineError::new_err(e.to_string())),
        },
    }
}

fn _get_sheet_names(path: &str) -> Result<Vec<String>, Error> {
    let book = open_workbook_auto(path)?;
    Ok(book.sheet_names().to_vec())
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
    let mut book = open_workbook_auto(path)?;

    // use native worksheets method
    let worksheets = book.worksheets();
    let sheet_map: HashMap<_, _> = worksheets.into_iter().collect();

    // sheet names are in order
    let sheet_names = book.sheet_names().to_vec();

    // create vec with capacity to insert into original order positions
    let mut res = Vec::new();
    for name in sheet_names.iter() {
        res.push((
            name.clone(),
            parse::parse_range(sheet_map.get(name).unwrap()),
        ));
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
    m.add_function(wrap_pyfunction!(get_sheet_data_with_name, m)?)?;
    m.add_function(wrap_pyfunction!(get_sheet_names, m)?)?;
    m.add_function(wrap_pyfunction!(get_sheets, m)?)?;
    m.add("CalamineError", py.get_type::<CalamineError>())?;
    Ok(())
}
