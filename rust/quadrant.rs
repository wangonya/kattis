use std::io;

fn main() {
    let mut x = String::new();
    io::stdin().read_line(&mut x).expect("failed to read line");
    let x: i32 = x.trim().parse().expect("not a number");

    let mut y = String::new();
    io::stdin().read_line(&mut y).expect("failed to read line");
    let y: i32 = y.trim().parse().expect("not a number");

    if x > 0 && y > 0 {
        print!("1")
    } else if x < 0 && y > 0 {
        print!("2")
    } else if x < 0 && y < 0 {
        print!("3")
    } else {
        print!("4")
    }
}
