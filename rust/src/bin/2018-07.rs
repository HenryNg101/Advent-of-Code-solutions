use std::{cmp::{max, min, Reverse}, collections::{BinaryHeap, HashMap, VecDeque}};

use my_project::get_input;

fn main(){
    let input = get_input(2018, 7)
        .expect("Can't get the content");

    let mut res_a = String::new();
    let mut graph = HashMap::new();
    let mut indegree = HashMap::new();
    let input: Vec<(u8, u8)> = input
        .lines()
        .map(|line| line.split(' ').collect())
        .map(|line: Vec<&str>| (line[1].as_bytes()[0], line[7].as_bytes()[0]))
        .collect();

    for line in input.iter() {
        graph.entry(line.0).or_insert(vec![]);
        graph.entry(line.1).or_insert(vec![]);
        indegree.entry(line.0).or_insert(0);
        indegree.entry(line.1).or_insert(0);
        
        (*graph.get_mut(&line.0).unwrap()).push(line.1);
        *indegree.get_mut(&line.1).unwrap() += 1;
    }

    // Part A code
    let mut pq = BinaryHeap::new();
    for (&k, &v) in indegree.iter() {
        if v == 0 {
            pq.push(Reverse(k));
        }
    }

    while !pq.is_empty() {
        let curr = pq.pop().unwrap().0;
        res_a.push(curr as char);

        for new_step in graph.get(&curr).unwrap() {
            *indegree.get_mut(new_step).unwrap() -= 1;
            if *indegree.get(new_step).unwrap() == 0 {
                pq.push(Reverse(*new_step));
            }
        }
    }
    println!("Part A: {}", res_a);

    // let mut pq = BinaryHeap::new();
    // for (&k, &v) in indegree.iter() {
    //     if v == 0 {
    //         pq.push(Reverse(k));
    //     }
    // }
    // let mut timer = 0;
    // let mut workers = [(0, 0); 5];
    // while true {
    //     for i in 0..workers.len() {
    //         if workers[i].0 == 0 {
    //             if pq.is_empty() {
    //                 continue;
    //             }
    //             let curr = pq.pop().unwrap().0;
    //             workers[i] = (curr - b'A' + 61, curr);
    //         }
    //         workers[i].0 -= 1;
    //     }
    //     print!("{}: ", timer);
    //     for worker in workers {
    //         print!("{} {}, ", worker.0, worker.1 as char);
    //     }
    //     println!();

    //     let mut continue_loop = false;
    //     for mut worker in workers {
    //         if worker.0 > 0 {
    //             continue_loop = true;
    //             break;
    //         }
    //         if graph.contains_key(&worker.1){
    //             for new_step in graph.get(&worker.1).unwrap() {
    //                 *indegree.get_mut(new_step).unwrap() -= 1;
    //                 if *indegree.get(new_step).unwrap() == 0 {
    //                     pq.push(Reverse(*new_step));
    //                 }
    //             }
    //         }
    //         if worker.0 == 0 {
    //             worker.1 = 0;
    //         }
    //     }
    //     if !continue_loop && pq.is_empty() {
    //         break;
    //     }
    //     timer += 1;
    // }
    // println!("Part B: {}", timer + 1);
}