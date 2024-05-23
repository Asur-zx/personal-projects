pub mod basics {
    pub struct Information<'a>{
        url: &'a str,
        username: &'a str,
        password: String,
        notes: String,

    }
    impl<'a> Information<'a>{
        pub fn new(url: &'a str, username: &'a str, password: String, notes: String)->Self{
            Self{
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
            println!("URL: {}", self.url);
            println!("Username: {}", self.username);
            println!("Password: {}", self.password);
            println!("Notes: {}", self.notes);
        }
        pub fn is_valid_password(&self, pword: &str)->bool{
            self.password==pword
        }
        pub fn get_uname(&self)->&str{
            return self.username;
        }
        pub fn get_url(&self)->&str{
            return self.url;
        }
        pub fn get_pword(&self)->String{
            return self.password;
        }
        pub fn get_notes(&self)->String{
            return self.notes;
        }
    }

}


