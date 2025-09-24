use my_project::get_input;
use std::collections::HashSet;

fn main(){
    let input = get_input(2018, 1)
        .expect("Can't get the content");

    let changes: Vec<i32> = input
        .lines()
        .map(|line| line.parse::<i32>().expect("Can't pase to integer"))
        .collect();

    println!("Part A: {}", changes.iter().sum::<i32>());

    let mut freq = 0;
    let mut seen_numbers = HashSet::new();

    // Keep iterating and go back to the beginning of the sequence until condition is satisfied
    for change in changes.iter().cycle() {
        if !seen_numbers.insert(freq) {
            println!("Part B: {}", freq);
            break;
        }
        freq += change;
    }
}