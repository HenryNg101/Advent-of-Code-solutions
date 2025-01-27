use std::{collections::HashMap, fs};

fn is_valid_number(s: &str) -> bool {
    s.parse::<f64>().is_ok()
}

// Calculate signal to wire a using Kahn algorithm
fn calculate_signal<'a>(
    mp: &'a HashMap<&'a str, Vec<&'a str>>, 
    expressions: &'a HashMap<&'a str, Vec<&'a str>>, 
    mut indegrees: HashMap<&'a str, i32>,
    changed_value: Option<i32>
) -> i32 {
    let mut stack = vec![];  // Will be important for Kahn algorithm
    let mut val_mapping = HashMap::new();  // Map the value of the node to it
    
    // Init the Kahn algorithm
    for (&node, &indegree) in indegrees.iter() {
        if indegree == 0 {
            stack.push(node);
        }
    }

    // Main algorithm
    while !stack.is_empty() {
        let curr = stack[stack.len() - 1];
        stack.pop();

        if mp.get(curr).is_some() {
            for child in mp.get(curr).unwrap() {
                indegrees.insert(child, indegrees.get(child).unwrap() - 1);
                if *indegrees.get(child).unwrap() == 0 {
                    stack.push(child);
                }
            }
        }

        let expression = expressions.get(curr).unwrap();
        let mut cal_res = -1;

        match expression.len() {
            1 => {
                cal_res = if is_valid_number(expression[0]) {
                    expression[0].parse::<i32>().unwrap()
                }
                else {
                    *val_mapping.get(&expression[0]).unwrap()
                };
            },
            2 => {
                cal_res = if is_valid_number(expression[1]) {
                    expression[1].parse::<i32>().unwrap()
                }
                else {
                    *val_mapping.get(&expression[1]).unwrap()
                };
                cal_res ^= 65535;
            },
            3 => {
                cal_res = if is_valid_number(expression[0]) {
                    expression[0].parse::<i32>().unwrap()
                }
                else {
                    *val_mapping.get(&expression[0]).unwrap()
                };

                let other_op = if is_valid_number(expression[2]) {
                    expression[2].parse::<i32>().unwrap()
                }
                else {
                    *val_mapping.get(&expression[2]).unwrap()
                };

                match expression[1] {
                    "AND" => cal_res &= other_op,
                    "OR" => cal_res |= other_op,
                    "LSHIFT" => cal_res <<= other_op,
                    "RSHIFT" => cal_res >>= other_op,
                    _ => {}
                }
            },
            _ => {}
        }
        val_mapping.insert(curr, cal_res);
        if curr == "b" && changed_value != None {
            val_mapping.insert(curr, changed_value.unwrap());
        }
    }
    return *val_mapping.get(&"a").unwrap();
}

fn main(){
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    let mut mp: HashMap<&str, Vec<&str>> = HashMap::new();    // Dependency graph
    let mut indegrees = HashMap::new();    // Indegree of each node
    let mut expressions = HashMap::new();   // The expression that leads to the result of a node

    // Building the map
    for line in content.lines() {
        let line: Vec<&str> = line.split_whitespace().collect();
        let exp = line[..line.len() - 2].to_vec();
        let var = line[line.len() - 1];
        let mut level = 0;

        match exp.len() {
            1 => {
                if !is_valid_number(exp[0]) {
                    level += 1;
                    mp.entry(exp[0]).or_default().push(var);
                }
            },
            2 => {
                if !is_valid_number(exp[1]) {
                    level += 1;
                    mp.entry(exp[1]).or_default().push(var);
                }
            },
            3 => {
                if !is_valid_number(exp[0]) {
                    level += 1;
                    mp.entry(exp[0]).or_default().push(var);
                }
                if !is_valid_number(exp[2]) {
                    level += 1;
                    mp.entry(exp[2]).or_default().push(var);
                }
            },
            _ => {}
        }
        indegrees.insert(var, level);
        expressions.insert(var, exp);
    }

    // Run the algorithm for part A
    let res_a = calculate_signal(&mp, &expressions, indegrees.clone(), None);
    println!("Part A: {}", res_a);

    // Part B: applying the result we got to wire b, then redo the calculation
    let res_b = calculate_signal(&mp, &expressions, indegrees, Some(res_a));
    println!("Part B: {}", res_b);
}