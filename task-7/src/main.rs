extern crate regex;
use regex::Regex;

fn main() {
  let re = Regex::new(r"\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$").unwrap();
  let text = "nsaiganesh2003@gmail.com";

  match re.captures(text) {
    Some(caps) => println!("Found match: {}", &caps[0]),
    None => println!("could not find match..")
  }
}
