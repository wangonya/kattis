// https://open.kattis.com/problems/grassseed
use std::io;
use std::str::FromStr;

struct Lawn {
    width: u32,
    height: u32,
}

fn main() {
    let mut cost = String::new();
    let mut lawns = String::new();

    io::stdin().read_line(&mut cost);
    io::stdin().read_line(&mut lawns);

    let lawns_num = i32::from_str(&lawns).unwrap();
    for _ in 0..lawns_num {
        println!("ok")
    }
}

// fn calculate() -> f32 {}
