use my_project::get_input;

fn main() {
    let content = get_input(2015, 1).expect("Can't get the content");

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