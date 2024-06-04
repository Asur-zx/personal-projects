use crate::bskftrs;
use std::fs::File;
use std::io::Write;
use std::io::{BufRead, BufReader};



pub fn create_new_file(user_file_path: &str){
    let _file = File::create(user_file_path).expect("error creating new file!");
}

pub fn write_data(user_file_path: &str, content: String){
    let mut file = File::options().append(true).open(user_file_path).expect("error opening file in append mode!");
    writeln!(&mut file, "{}",content).expect("error writing to file!");

}

pub fn write_info(user_file_path: &str, content: bskftrs::Information){
    let mut current_line = content.get_name().to_string();
    println!("{}", current_line);
    current_line.push_str("\u{2605}");
    current_line.push_str(&content.get_uname());
    current_line.push_str("\u{2605}");
    current_line.push_str(&content.get_url());
    current_line.push_str("\u{2605}");
    current_line.push_str(&content.get_pword());
    current_line.push_str("\u{2605}");
    current_line.push_str(&content.get_notes());
    current_line.push_str("\n");
    write_data(user_file_path, current_line);
}

pub fn get_person(user_file_path: &str, name:String)-> bskftrs::Information{
    let file = File::open(user_file_path).expect("failed to open file!");
    let mut reader = BufReader::new(file);

    loop{
        let mut line = String::new();
    reader.read_line(&mut line).expect("failed to read line");

    if line == ""{
        break bskftrs::Information::new("".to_string(),
                                        "".to_string(),
                                        "".to_string(),
                                        "".to_string(),
                                        "".to_string());
    }

    let each_str: Vec<&str> = line.split("\u{2605}").collect();
    //println!("{} :: {}", name, each_str[0]);
    if each_str[0]==&name{
        let person = bskftrs::Information::new(each_str[0].to_string(),
                                      each_str[1].to_string(),
                                      each_str[2].to_string(),
                                      each_str[3].to_string(),
                                      each_str[4].to_string());
        return person;
    }
    else {println!("__");}
    }
}
