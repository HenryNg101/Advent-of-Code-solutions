use std::fs;
use std::cmp::{min, max};

fn main() {
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    let mut total_a = 0;
    let mut total_b = 0;

    for line in content.split('\n'){
        let mut arr = line.split('x').map(|x| x.parse::<i32>().unwrap());
        let (a, b, c) = (arr.next().unwrap(), arr.next().unwrap(), arr.next().unwrap());

        let s1 = a * b;
        let s2 = b * c;
        let s3 = c * a;

        total_a += 2 * (s1 + s2 + s3) + min(s1, min(s2, s3));
        total_b += 2 * (a + b + c - max(a, max(b, c))) + a * b * c;
    }
    println!("Part A: {}", total_a);
    println!("Part B: {}", total_b);
}