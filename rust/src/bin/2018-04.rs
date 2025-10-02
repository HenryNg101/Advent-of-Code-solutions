use std::{cmp::Ordering, collections::HashMap};
use my_project::get_input;

fn main(){
    let input = get_input(2018, 4)
        .expect("Can't get the content");

    let mut time_series: Vec<Vec<&str>> = input
        .lines()
        .map(|line| line.split(' ').collect())
        .collect();

    // Sort the time series data to the right timely order
    time_series.sort_by(|a, b| {
        let res = a[0].cmp(&b[0]);
        match res {
            Ordering::Equal => a[1].cmp(&b[1]),
            _ => res
        }
    });

    let mut sleeping_times = HashMap::new();    // Tracks the occurences of a guard sleeping in that specific minute
    let mut total_sleeping = HashMap::new();    // Tracks the total sleeping time of a guard

    let mut max_guard = (0, 0);     // Part A. (guard id, minute which that guard sleep most)
    let mut max_sleeping_guard = (0, 0, 0);     // Part B's tracker (guard id, minute which that guard sleep most, minute which that got slept most across all guards)

    let mut curr_guard = 0;
    let mut start_sleep_time = 0;
    for line in time_series.iter() {
        match line[2] {
            "Guard" => {
                curr_guard = line[3][1..line[3].len()].parse().unwrap();
                sleeping_times.entry(curr_guard).or_insert([0; 60]);
                total_sleeping.entry(curr_guard).or_insert(0);
            },
            "falls" => {
                start_sleep_time = line[1][3..5].parse().unwrap();
            },
            "wakes" => {
                let end_sleep_time = line[1][3..5].parse().unwrap();
                *total_sleeping.get_mut(&curr_guard).unwrap() += end_sleep_time - start_sleep_time;

                for i in start_sleep_time..end_sleep_time {
                    if let Some(arr) = sleeping_times.get_mut(&curr_guard) {
                        arr[i] += 1;

                        // Part B update
                        if arr[i] > max_sleeping_guard.2 {
                            max_sleeping_guard = (curr_guard, i, arr[i]);
                        }
                    }
                }

                // Check for part A
                if *total_sleeping.get(&curr_guard).unwrap() > max_guard.1 {
                    max_guard = (curr_guard, *total_sleeping.get(&curr_guard).unwrap());
                }
            }
            _ => {}
        }
    }

    let mut max_minute = 0;
    if let Some(sleeping_minutes) = sleeping_times.get(&max_guard.0) {
        for (id, &sleeping_time) in sleeping_minutes.iter().enumerate() {
            if sleeping_time > sleeping_minutes[max_minute] {
                max_minute = id;
            }
        }
    }
    println!("Part A: {}", max_guard.0 * max_minute);
    println!("Part B: {}", max_sleeping_guard.0 * max_sleeping_guard.1);
}