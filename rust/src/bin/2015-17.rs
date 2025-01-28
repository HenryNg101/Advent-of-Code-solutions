use std::{collections::HashMap, fs};

fn knapsack(amount: usize, content: Vec<i32>) -> HashMap<i32, i32> {
    let mut dp = vec![vec![HashMap::new(); amount+1]; content.len()];
    for i in 0..dp.len() {
        dp[i][0].insert(0, 1);
    }

    for col in 1..amount+1 {
        for row in 0..content.len() {
            if row > 0 {
                dp[row][col] = dp[row-1][col].clone();
                if col >= content[row].try_into().unwrap() {
                    for (key, val) in dp[row-1][col - content[row]] {
                        
                    }
                }
            }
            else {
                if col == content[row].try_into().unwrap() {
                    dp[row][col].insert(1, 1);
                }
            }
        }
    }
    
    dp[content.len() - 1][amount].clone();
}

fn main() {
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    let content: Vec<i32> = content.lines()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
}