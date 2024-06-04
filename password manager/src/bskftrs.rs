    pub struct Information<>{
        name: String,
        url: String,
        username: String,
        password: String,
        notes: String,

    }

    impl<> Information<>{
        pub fn new(name: String, url: String, username: String, password: String, notes: String)->Self{
            Self{
                name,
                url,
                username,
                password,
                notes,
            }
        }
        pub fn updatepassword(&mut self, new_password: String){
            self.password=new_password;
        }

        pub fn updatenotes(&mut self, new_notes: String){
            self.notes=new_notes;
        }
        pub fn display_info(&self) {
            println!("Name: {}", self.name);
            println!("URL: {}", self.url);
            println!("Username: {}", self.username);
            println!("Password: {}", self.password);
            println!("Notes: {}", self.notes);
        }
        pub fn is_valid_password(&self, pword: String)->bool{
            self.password==pword
        }
        pub fn get_name(&self)->String{
            return self.name.clone();
        }
        pub fn get_uname(&self)->String{
            return self.username.clone();
        }
        pub fn get_url(&self)->String{
            return self.url.clone();
        }
        pub fn get_pword(&self)->String{
            return self.password.clone();
    }
        pub fn get_notes(&self)->String{
            return self.notes.clone();
        }
    }
