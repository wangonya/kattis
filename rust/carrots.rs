use std::any::type_name;
use std::io;
use std::str::FromStr;

fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

fn main() {
    let mut inp = String::new();
    io::stdin()
        .read_line(&mut inp)
        .expect("failed to read line");
    println!("You entered {}", inp);

    let first_char = &inp[..1];
    let last_char = &inp[2..];
    println!("first char = {} and last = {}", first_char, last_char);
    println!("type of first = {}", type_of(first_char));
    println!("type of last = {}", type_of(last_char));

    let first_num = i32::from_str(first_char).unwrap();

    let mut inp2 = String::new();
    for _ in 0..first_num {
        io::stdin().read_line(&mut inp2);
    }

    print!("{}", last_char);
}
