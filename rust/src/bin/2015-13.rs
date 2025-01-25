use std::{cmp::max, collections::{HashMap, HashSet}, fs, i32};

fn permutations<'a>(
    id: usize, peoples: &mut Vec<&'a str>, 
    result: &mut Vec<Vec<&'a str>>) {
    
    if id >= peoples.len() {
        result.push(peoples.to_vec());
        return;
    }
    for i in id..peoples.len() {
        peoples.swap(i, id);
        permutations(id+1, peoples, result);
        peoples.swap(i, id);
    }
}

fn optimal_hapiness(peoples: &HashSet<&str>, mp: &HashMap<(&str, &str), i32>) -> i32 {
    let mut max_dis = i32::MIN;
    let mut result : Vec<Vec<&str>> = Vec::new();
    permutations(0, &mut Vec::from_iter(peoples.clone()), &mut result);

    for perm in result {
        let mut total_dis = 0;
        for (i, &elem) in perm.iter().enumerate() {
            let j = if i > 0 {
                i - 1
            } else {
                perm.len() - 1
            };
            let (start, stop) = (perm[j], elem);
            total_dis += mp.get(&(start, stop)).unwrap() + mp.get(&(stop, start)).unwrap();
        }
        max_dis = max(max_dis, total_dis);
    }

    return max_dis;
}

fn main() {
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    let mut mp = HashMap::new();
    let mut peoples = HashSet::new();

    for line in content.lines() {
        let line: Vec<&str> = line.split_whitespace().collect();
        let (start, stop, cost) = (
            line[0], *line.last().unwrap(), line[3]);
        let stop = &stop[..stop.len()-1];
        let mut cost = cost.parse::<i32>().unwrap();
        if line[2] == "lose" {
            cost = 0 - cost;
        }

        peoples.insert(start);
        peoples.insert(stop);
        mp.insert((start, stop), cost);
    }
    println!("Part A: {}", optimal_hapiness(&peoples, &mp));

    // Part B
    for &people in &peoples {
        mp.insert((people, "you"), 0);
        mp.insert(("you", people), 0);
    }
    peoples.insert("you");
    println!("Part B: {}", optimal_hapiness(&peoples, &mp));
}