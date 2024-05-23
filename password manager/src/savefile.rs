use serde::{Serialize, Deserialize};  // to converst json to struct and vice versa
use std::fs;
use std::io;
use serde::json;
mod bskftrs;
use bskftrs::basics::Information;

fn process_data(data: Data) {
    println!("Processing data: {:?}", Information);
}

fn write_to_file(data: Information){

}

