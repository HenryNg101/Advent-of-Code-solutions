use std::fs;
use reqwest::header::{HeaderMap, HeaderValue, COOKIE};
use std::path::Path;
use serde::Deserialize;
use reqwest;
use reqwest::blocking::Client;
use std::error::Error;

#[derive(Deserialize, Debug)]
struct CookieData {
    session: String
}

// Parse JSON data into a structured json data form, and get the session value
fn load_cookie_session(file_path: &str) -> Result<String, Box<dyn Error>> {
    let content = fs::read_to_string(file_path).expect("Can't find the json input file");
    let cookie_value: CookieData = serde_json::from_str(&content).expect("Can't get the session value");
    Ok(cookie_value.session)
}

// A synchronus version of getting input. I might use async later on, if needed
pub fn get_input(year: i32, day: i32) -> Result<String, Box<dyn Error>> {
    // If the file exists and got cached, no need to making extra http requests
    let input_dirname = "inputs";
    let input_filename = format!("{}/{}-{}.txt", input_dirname, year, day);
    fs::create_dir_all(input_dirname)?;  // Create the input folder if doesn't exist

    if Path::new(&input_filename).exists() {
        return Ok(fs::read_to_string(input_filename)?);
    }

    // Otherwise, making that API call to fetch input
    // Insert the cookie's session value to the request's header
    let cookie_header = format!("session={}", load_cookie_session("cookies.json")?);
    let mut header = HeaderMap::new();
    header.insert(COOKIE, HeaderValue::from_str(&cookie_header)?);
    
    // Make a get request to the url, with the customized header, then cache the data to a file
    let client = Client::new();
    let mut input_data = client
        .get(format!("https://adventofcode.com/{}/day/{}/input", year, day))
        .headers(header)
        .send()?
        .text()?;
    if input_data.ends_with('\n'){
        input_data.pop();   // Remove the last character, which is a terminating '\n', not needed
    }
    fs::write(&input_filename, &input_data)?;

    Ok(input_data)
}