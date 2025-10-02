use std::cmp::min;
use my_project::get_input;

fn polymer_collapse(input: &[u8], removed_unit: Option<u8>) -> usize{
    let mut stack = vec![];
    for &c in input.iter() {
        if let Some(check) = removed_unit {
            if c == check || c == check - 32 {
                continue;
            }
        }
        if !stack.is_empty() && (c == stack[stack.len()-1] - 32 || c == stack[stack.len()-1] + 32) {
            stack.pop();
        }
        else {
            stack.push(c);
        }
    }
    stack.len()
}

fn main(){
    let input = get_input(2018, 5)
        .expect("Can't get the content");

    let input = input.as_bytes();

    let mut res = polymer_collapse(input, None);
    println!("Part A: {}", res);
    for c in b'a'..=b'z' {
        res = min(res, polymer_collapse(input, Some(c)));
    }
    println!("Part B: {}", res);
}