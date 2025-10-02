use std::{cmp::{max, min}, collections::HashMap, isize};
use my_project::get_input;

fn main(){
    let input = get_input(2018, 6)
        .expect("Can't get the content");

    let coordinates: Vec<(isize, isize)> = input
        .lines()
        .map(|line| {
            line.split(", ")
            .map(|coord| coord.parse().expect("Can't parse to integer"))
            .collect()
        })
        .map(|coord: Vec<isize>| (coord[1], coord[0]))  // Rows and columns are in reverse order
        .collect();

    let (mut min_r, mut min_c, mut max_r, mut max_c) = (isize::MAX, isize::MAX, 0, 0);

    for &(r, c) in coordinates.iter() {
        min_r = min(min_r, r);
        max_r = max(max_r, r);
        min_c = min(min_c, c);
        max_c = max(max_c, c);
    }

    let mut res_a = 0;
    let mut areas: HashMap<(isize, isize), i32> = HashMap::new();
    for r in min_r..=max_r {
        for c in min_c..=max_c {
            let mut closest_pt = (isize::MAX / 2, isize::MAX / 2);  // Assign random large number to make the distance so large
            let mut valid_coord = true; // A flag to check whether or not this coordinate has equal min distance to more than one point

            for &(r1, c1) in coordinates.iter() {
                let mht_dis = (r1 - r).abs() + (c1 - c).abs();
                let old_mht = (closest_pt.0 - r).abs() + (closest_pt.1 - c).abs();
                if mht_dis == old_mht {
                    valid_coord = false;
                }
                if mht_dis < old_mht {
                    closest_pt = (r1, c1);
                    valid_coord = true;
                }
            }
            if valid_coord {
                let (closest_r, closest_c) = closest_pt;
                if closest_r != max_r && closest_r != min_r && closest_c != max_c && closest_c != min_c {
                    areas.entry((closest_r, closest_c)).or_insert(0);

                    *areas.get_mut(&(closest_r, closest_c)).unwrap() += 1;
                    res_a = max(res_a, *areas.get(&(closest_r, closest_c)).unwrap());
                }
            }
        }
    }
    println!("Part A: {}", res_a);

    // Part B
    let safe_distance = 10000;
    let max_allowed_dis = safe_distance / (coordinates.len() as i32);
    let min_r = min_r as i32 - max_allowed_dis;
    let min_c = min_c as i32 - max_allowed_dis;
    let max_r = max_r as i32 + max_allowed_dis;
    let max_c = max_c as i32 + max_allowed_dis;
    let mut res_b = 0;

    for r in min_r..=max_r {
        for c in min_c..=max_c {
            let mut total_dis = 0;
            for &(r1, c1) in coordinates.iter() {
                total_dis += (r as i32 - r1 as i32).abs() + (c as i32 - c1 as i32).abs();
                if total_dis > safe_distance {
                    break;
                }
            }
            res_b += if total_dis < safe_distance {1} else {0};
        }
    }
    println!("Part B: {}", res_b);
}