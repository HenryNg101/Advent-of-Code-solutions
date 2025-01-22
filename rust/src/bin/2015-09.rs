use std::{cmp::{max, min}, collections::{HashMap, HashSet}, fs, u32};

// Finding all permutations
fn permute(
    stops: &mut Vec<&str>, id: usize, 
    mp: &HashMap<(&str, &str), u32>, 
    max_cost: &mut u32, min_cost: &mut u32
) {
    if id >= stops.len() - 1 {
        // Find the total cost of the whole journey, which is the sum of all pairs of 2 consecutive cities on the path
        let cost = stops.windows(2).map(|pair| mp[&(pair[0], pair[1])]).sum();
        *max_cost = max(*max_cost, cost);
        *min_cost = min(*min_cost, cost);
        return;
    }
    for i in id..stops.len() {
        stops.swap(i, id);
        permute(stops, id+1, mp, max_cost, min_cost);
        stops.swap(i, id);
    }
}

fn main(){
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    let mut mp = HashMap::new();
    let mut stops = HashSet::new();
    let mut max_cost = 0;
    let mut min_cost = u32::MAX;

    for line in content.lines() {
        let line: Vec<&str> = line.split_whitespace().collect();
        let (start, stop, cost) = (line[0], line[2], line[4].parse::<u32>().unwrap());
        mp.insert((start, stop), cost);
        mp.insert((stop, start), cost);
        stops.insert(start);
        stops.insert(stop);
    }
    let mut stops: Vec<&str> = stops.into_iter().collect();
    permute(&mut stops, 0, &mp, &mut max_cost, &mut min_cost);

    println!("Part A: {}", min_cost);
    println!("Part B: {}", max_cost);
}