mod bskftrs;
mod savefile;
use std::io;
    fn main(){
        println!("Please Type the data as requested :");
        println!("Type the name of entry :");
        let mut name = String::new();
        let mut url= String::new();
        let mut uname= String::new();
        let mut pword= String::new();
        let mut notes= String::new();
        io::stdin().read_line(&mut name).expect("error readling input");

        println!("Type the url of entry :");
        io::stdin().read_line(&mut url).expect("error readling input");

        println!("Type the username of entry :");
        io::stdin().read_line(&mut uname).expect("error readling input");

        println!("Type the pword of entry :");
        io::stdin().read_line(&mut pword).expect("error readling input");

        println!("Type the notes of entry :");
        io::stdin().read_line(&mut notes).expect("error readling input");

        let person = bskftrs::Information::new(name.trim().to_string(),
                                               url.trim().to_string(),
                                               uname.trim().to_string(),
                                               pword.trim().to_string(),
                                               notes.trim().to_string());
            //savefile::create_new_file("database1.txt");
            savefile::write_info("database1.txt",person);
            let person = savefile::get_person("database1.txt","yahoo".to_string());
            println!("{}::{}::{}::{}::{}", person.get_name(), person.get_uname(), person.get_url(), person.get_pword(), person.get_notes());
    }
