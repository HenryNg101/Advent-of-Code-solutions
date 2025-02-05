use std::collections::HashSet;
use my_project::get_input;

fn main() {
    let content = get_input(2016, 1)
        .expect("Can't get the content");

    let directions = [(-1, 0), (0, 1), (1, 0), (0, -1)];
    let mut curr_pos: (i32, i32) = (0, 0);
    let mut first_revisit = None;
    let mut dir_id = 0;
    let mut visited = HashSet::new();
    visited.insert((0, 0));

    for inst in content.split(", ") {
        dir_id += match inst.as_bytes()[0] {
            b'L' => 3,
            b'R' => 1,
            _ => 0
        };

        let (dr, dc) = directions[dir_id % 4];
        for _ in 0..inst[1..].parse::<i32>().unwrap() {
            curr_pos = (curr_pos.0 + dr, curr_pos.1 + dc);

            // Only change the first time
            if !visited.insert(curr_pos) && first_revisit.is_none() {
                first_revisit = Some(curr_pos);
            }
        }
    }
    println!("Part A: {}", curr_pos.0.abs() + curr_pos.1.abs());
    if let Some((r, c)) = first_revisit {
        println!("Part B: {}", r.abs() + c.abs());
    }
}