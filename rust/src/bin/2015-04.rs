use md5;
use std::fs;

fn lowest_md5(content: &str, n: usize) -> i32{
    let cmp = &"0".repeat(n);
    for i in 1.. {
        let s = format!("{}{}", content, i.to_string());
        let hash_val = format!("{:x}", md5::compute(s));
        if hash_val.starts_with(cmp){
            return i;
        }
    }
    unreachable!();
}

fn main(){
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    println!("Part A: {}", lowest_md5(&content, 5));
    println!("Part B: {}", lowest_md5(&content, 6));
}