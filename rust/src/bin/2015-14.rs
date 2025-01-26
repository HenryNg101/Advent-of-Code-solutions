use std::{cmp::max, fs};

struct Reindeer {
    speed: i32,         // Speed when flying
    duration: i32,      // Max flying duration before needing to rest
    rest: i32,          // Rest time needed before flying again
    travelled: i32,     // Total distance travelled
    points: i32,        // Points earned
    flying_time: i32,   // Remaining flying time in the current cycle
    resting_time: i32,  // Remaining resting time in the current cycle
}

impl Reindeer {
    fn new(speed: i32, duration: i32, rest: i32) -> Self {
        Self {
            speed,
            duration,
            rest,
            travelled: 0,
            points: 0,
            flying_time: duration,
            resting_time: rest
        }
    }
}

fn main() {
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    let mut reindeers: Vec<Reindeer> = content
        .lines()
        .map(|line| {
            let line: Vec<&str> = line.split_whitespace().collect();
            Reindeer::new(
                line[3].parse::<i32>().unwrap(),
                line[6].parse::<i32>().unwrap(),
                line[line.len() - 2].parse::<i32>().unwrap()
            )
        })
        .collect();

    let mut max_travelled = 0;
    let mut max_score = 0;
    for _ in 0..2503 {
        // Update the state of each reindeer
        for reindeer in reindeers.iter_mut() {
            if reindeer.flying_time > 0 {
                reindeer.flying_time -= 1;
                reindeer.travelled += reindeer.speed;
            }
            else {
                reindeer.resting_time -= 1;
                if reindeer.resting_time == 0 {
                    reindeer.flying_time = reindeer.duration;
                    reindeer.resting_time = reindeer.rest;
                }
            }
            max_travelled = max(max_travelled, reindeer.travelled);
        }
        // Update score and get max score
        for reindeer in reindeers.iter_mut() {
            if reindeer.travelled == max_travelled {
                reindeer.points += 1;
                max_score = max(max_score, reindeer.points);
            }
        }
    }
    println!("Part A: {}", max_travelled);
    println!("Part B: {}", max_score);
}