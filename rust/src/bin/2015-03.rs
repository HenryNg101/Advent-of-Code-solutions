use std::collections::HashSet;
use my_project::get_input;

fn received_presents_count(content: &str, deliverers_count: usize) -> usize{
    let mut start_locs = vec![(0, 0); deliverers_count]; // Deliverers positions
    let mut visited_houses = HashSet::new(); // Houses that got at least one present
    visited_houses.insert(start_locs[0]);

    for (id, char) in content.bytes().enumerate() {
        let deliverer_id = id % start_locs.len();
        match char {
            b'^' => start_locs[deliverer_id].0 -= 1,
            b'v' => start_locs[deliverer_id].0 += 1,
            b'<' => start_locs[deliverer_id].1 -= 1,
            b'>' => start_locs[deliverer_id].1 += 1,
            _ => {}
        }
        visited_houses.insert(start_locs[deliverer_id]);
    }
    visited_houses.len()
}

fn main() {
    let content = get_input(2015, 3).expect("Can't read from file");

    println!("Part A: {}", received_presents_count(&content, 1));
    println!("Part B: {}", received_presents_count(&content, 2));
}