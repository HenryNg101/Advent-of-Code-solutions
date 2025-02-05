use std::collections::HashMap;
use my_project::get_input;

fn main(){
    let content: Vec<i32> = get_input(2015, 17)
        .expect("Can't read from file")
        .split('\n')
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    /* A classical Knapsack 0/1 DP problem (as you can choose to use that container or not), 
    so I just need a 2D table for memoization for different amount of eggnog and different 
    container indexes */
    let sz = content.len();
    let eggnog_amount = 150;

    /* A 2d dp table for tabulation, with one direction is the indexes of the array (rows), 
    and the other one is for the eggnog amount (columns).

    Each cell contains information on the occurences of the amount of needed container to get 
    that eggnog amount, given the subarray arr[0..id], which is important for part B */
    let mut dp = vec![vec![HashMap::new(); eggnog_amount + 1]; sz];
    
    for row in 0..sz {
        dp[row][0].insert(0, 1);
    }

    for col in 1..eggnog_amount+1 {
        for row in 0..sz {
            if row > 0 {
                let (dp_before, dp_current) = dp.split_at_mut(row);
                // Immutable borrow from the first part
                let prev_map = &dp_before[row - 1][col];
                // Mutable borrow from the second part
                let current_map = &mut dp_current[0][col]; 

                // Clone previous state. This represents the one where you skip a container
                *current_map = prev_map.clone(); 

                // This is for the case when you use THIS container, and it makes the eggnog amount up to this one
                if col >= content[row] as usize {
                    let prev_col = col - content[row] as usize;
                    for (&key, &val) in &dp_before[row - 1][prev_col] {
                        current_map
                            .entry(key + 1)
                            .and_modify(|e| *e += val)
                            .or_insert(val);
                    }
                }
            }
            else {
                if col == content[row] as usize {
                    dp[row][col].insert(1, 1);
                }
            }
        }
    }

    let res = &dp[sz-1][eggnog_amount];
    println!("Part A: {}", res.values().sum::<i32>());

    let min_containers = res.keys().min().unwrap();
    println!("Part B: {}", res.get(&min_containers).unwrap());
}