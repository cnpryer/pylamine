use crate::utils::CellValue;
use calamine::{DataType, Range};

pub fn parse_range(range: &Range<DataType>) -> Vec<Vec<CellValue>> {
    let mut res = Vec::new();
    for row in range.rows() {
        let mut result_row = Vec::new();
        for value in row.iter() {
            match value {
                DataType::Int(v) => result_row.push(CellValue::Int(*v)),
                DataType::Float(v) => result_row.push(CellValue::Float(*v)),
                DataType::String(v) => result_row.push(CellValue::String(String::from(v))),
                DataType::DateTime(v) => {
                    if *v < 1.0 {
                        result_row.push(CellValue::Time(value.as_time().unwrap()))
                    } else if *v == (*v as u64) as f64 {
                        result_row.push(CellValue::Date(value.as_date().unwrap()))
                    } else {
                        result_row.push(CellValue::DateTime(value.as_datetime().unwrap()))
                    }
                }
                DataType::Bool(v) => result_row.push(CellValue::Bool(*v)),
                DataType::Error(_) => result_row.push(CellValue::Empty),
                DataType::Empty => result_row.push(CellValue::Empty),
            };
        }
        res.push(result_row);
    }
    res
}
