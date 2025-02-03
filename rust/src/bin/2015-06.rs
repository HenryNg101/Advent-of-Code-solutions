use std::cmp::max;
use my_project::get_input;

// Turns a coordination in string to tuple of numbers
// E.g: "10,20" => (10, 20)
fn parse_coordinate(coord: &str) -> (usize, usize) {
    let mut parts = coord.split(',').map(|x| x.parse::<usize>().expect("Invalid number"));
    (parts.next().unwrap(), parts.next().unwrap())
}

// Turns a line of instruction to useful information
fn parse_instruction(line: &str) -> (&str, (usize, usize), (usize, usize)) {
    let words: Vec<&str> = line.split_whitespace().collect();
    let (inst, start, stop) = if words[0] == "turn" {
        (words[1], words[2], words[4])
    } else {
        (words[0], words[1], words[3])
    };

    let start = parse_coordinate(start);
    let stop = parse_coordinate(stop);

    (inst, start, stop)
}

fn main(){
    let content = get_input(2015, 6).expect("Can't read from file");

    let mut grid_a = [[false; 1000]; 1000];
    let mut grid_b = [[0; 1000]; 1000];
    let mut counter_a = 0;
    let mut counter_b = 0;

    for line in content.lines() {
        let (inst, start_co, stop_co) = parse_instruction(line); 

        for r in start_co.0..=stop_co.0 {
            for c in start_co.1..=stop_co.1 {
                match inst {
                    "toggle" => {
                        grid_a[r][c] = !grid_a[r][c];
                        grid_b[r][c] += 2;
                    },
                    "on" => {
                        grid_a[r][c] = true;
                        grid_b[r][c] += 1;
                    },
                    "off" => {
                        grid_a[r][c] = false;
                        grid_b[r][c] = max(grid_b[r][c] - 1, 0);
                    },
                    _ => {}
                }
            }
        }
    }
    for r in 0..1000 {
        for c in 0..1000 {
            counter_a += grid_a[r][c] as i32;
            counter_b += grid_b[r][c];
        }
    }
    println!("Part A: {}", counter_a);
    println!("Part B: {}", counter_b);
}