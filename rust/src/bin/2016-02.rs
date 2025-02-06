use my_project::get_input;

fn find_password(keypad: &[&[&str]], mut start_pos: (usize, usize), content: &[&str]) -> String {
    let mut final_code = String::new();
    for line in content {
        for mv in line.bytes() {
            let new_pos = match mv {
                b'U' if start_pos.0 > 0 => (start_pos.0 - 1, start_pos.1),
                b'D' if start_pos.0 < keypad.len() - 1 => (start_pos.0 + 1, start_pos.1),
                b'L' if start_pos.1 > 0 => (start_pos.0, start_pos.1 - 1),
                b'R' if start_pos.1 < keypad[0].len() - 1 => (start_pos.0, start_pos.1 + 1),
                _ => {start_pos}
            };
            if !keypad[new_pos.0][new_pos.1].is_empty() {
                start_pos = new_pos;
            }
        }
        final_code.push_str(keypad[start_pos.0][start_pos.1]);
    }
    final_code
}

fn main() {
    let content = get_input(2016, 2)
        .expect("Can't get the content");
    let content: Vec<&str> = content.split('\n').collect();

    println!("Part A: {}", find_password(&[
        &["1", "2", "3"],
        &["4", "5", "6"],
        &["7", "8", "9"]
    ], (1, 1), &content));

    println!("Part B: {}", find_password(&[
        &["", "", "1", "", ""],
        &["", "2", "3", "4", ""],
        &["5", "6", "7", "8", "9"],
        &["", "A", "B", "C", ""],
        &["", "", "D", "", ""]
    ], (2, 1), &content));
}