// https://open.kattis.com/problems/autori
use std::io;

fn autori(s: String) -> String {
    let mut initials = String::from("");

    // iterateover chars in string
    for c in s.chars() {
        if c.is_ascii_uppercase() {
            initials.push_str(&c.to_string())
        }
    }

    initials
}

fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("failed to read line");
    println!("{}", autori(s));
}
