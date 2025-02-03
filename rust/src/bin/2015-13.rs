use std::{cmp::max, collections::{HashMap, HashSet}, i32};
use itertools::Itertools;
use my_project::get_input;

fn optimal_hapiness(peoples: &HashSet<&str>, mp: &HashMap<(&str, &str), i32>) -> i32 {
    let mut max_dis = i32::MIN;
    for perm in peoples.iter().permutations(peoples.len()) {
        let mut total_dis = 0;
        for i in 0..perm.len() {
            let (start, stop) = (perm[i], perm[(i+1) % perm.len()]);
            total_dis += mp.get(&(start, stop)).unwrap() + mp.get(&(stop, start)).unwrap();
        }
        max_dis = max(max_dis, total_dis);
    }
    max_dis
}

fn main() {
    let content = get_input(2015, 13).expect("Can't read from file");

    let mut mp = HashMap::new();
    let mut peoples = HashSet::new();

    for line in content.lines() {
        let line: Vec<&str> = line.split_whitespace().collect();
        let (start, stop) = (line[0], line.last().unwrap().trim_end_matches('.'));
        let mut cost = line[3].parse::<i32>().unwrap();
        if line[2] == "lose" {
            cost = -cost;
        }

        peoples.insert(start);
        peoples.insert(stop);
        mp.insert((start, stop), cost);
    }
    println!("Part A: {}", optimal_hapiness(&peoples, &mp));

    // Part B
    peoples.iter().for_each(|&person| {
        mp.insert((person, "you"), 0);
        mp.insert(("you", person), 0);
    });
    peoples.insert("you");
    println!("Part B: {}", optimal_hapiness(&peoples, &mp));
}