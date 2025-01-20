use std::fs;

fn main() {
    let content = fs::read_to_string("input.txt").expect("Can't read from file");

    let mut floor = 0;
    let mut res_b = None;

    for (id, inst) in content.bytes().enumerate() {
        match inst {
            b'(' => floor += 1,
            b')' => floor -= 1,
            _ => {}
        }
        if res_b.is_none() && floor < 0 {
            res_b = Some(id + 1);
        }
    }

    println!("Part A: {}", floor);
    println!("Part B: {}", res_b.unwrap_or(usize::MAX));
}