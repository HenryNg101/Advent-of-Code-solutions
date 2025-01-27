use std::{collections::HashMap, fs};

fn is_valid_number(s: &str) -> bool {
    s.parse::<f64>().is_ok()
}

fn get_value(expression: &Vec<&str>, expression_id: usize, val_mapping: &HashMap<&str, i32>) -> i32{
    if is_valid_number(expression[expression_id]) {
        expression[expression_id].parse::<i32>().unwrap()
    }
    else {
        *val_mapping.get(&expression[expression_id]).unwrap()
    }
}

// Given the mapping of existing values, and an expression, this function calculate the result of that expression
// There are 3 types of expression:
// - a -> b (exp len 1): Give a value to another value directly
// - NOT a -> b (exp len 2): Flip a value to get it
// - a op c -> b (exp len 3): Interact 2 values to get it
fn evaluate_expression(expression: &Vec<&str>, val_mapping: &HashMap<&str, i32>) -> i32{
    let mut cal_res = get_value(expression, expression.len() - 1, val_mapping);
    match expression.len() {
        2 => {
            cal_res ^= 65535;
        },
        3 => {
            let mut other_op = get_value(expression, 0, val_mapping);
            match expression[1] {
                "AND" => other_op &= cal_res,
                "OR" => other_op |= cal_res,
                "LSHIFT" => other_op <<= cal_res,
                "RSHIFT" => other_op >>= cal_res,
                _ => {}
            }
            cal_res = other_op;
        },
        _ => {}
    }
    cal_res
}

// Calculate signal to wire "a" using Kahn algorithm
fn calculate_signal<'a>(
    mp: &'a HashMap<&'a str, Vec<&'a str>>, 
    expressions: &'a HashMap<&'a str, Vec<&'a str>>, 
    mut indegrees: HashMap<&'a str, i32>,
    changed_value: Option<i32>
) -> i32 {
    let mut stack = vec![];  // Will be important for Kahn algorithm
    let mut val_mapping = HashMap::new();  // Map the value of the node to it
    
    for (&node, &indegree) in indegrees.iter() {
        if indegree == 0 {
            stack.push(node);
        }
    }

    while !stack.is_empty() {
        let curr = stack[stack.len() - 1];
        stack.pop();

        if mp.get(curr).is_some() {
            for child in mp.get(curr).unwrap() {
                if let Some(indegree) = indegrees.get_mut(child) {
                    *indegree -= 1;
                    if *indegree == 0 {
                        stack.push(child);
                    }
                }
            }
        }

        // Assign value to the current wire
        let expression = expressions.get(curr).unwrap();
        if curr == "b" && changed_value != None {
            val_mapping.insert(curr, changed_value.unwrap());
        }
        else {
            val_mapping.insert(curr, evaluate_expression(expression, &val_mapping));
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

        // Based on the pattern of all expresisons, the last one is always needed
        if !is_valid_number(exp[exp.len() - 1]) {
            level += 1;
            mp.entry(exp[exp.len() - 1]).or_default().push(var);
        }
        if exp.len() == 3 && !is_valid_number(exp[0]) {
            level += 1;
            mp.entry(exp[0]).or_default().push(var);
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