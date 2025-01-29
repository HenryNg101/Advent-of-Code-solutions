use std::{collections::HashMap, fs};

fn execute_program(content: &Vec<&str>, register_a: i32, register_b: i32) -> i32 {
    let mut inst_cnt: i32 = 0;   // The current instruction
    let mut registers = HashMap::from([("a", register_a), ("b", register_b)]);

    while inst_cnt < content.len() as i32 {
        let arr: Vec<&str> = content[inst_cnt as usize].split_whitespace().collect();

        // Match all possible structures of instructions
        match arr[..] {
            [inst, reg, offset] => {
                let reg = &reg[0..reg.len()-1];  // Remove the command in the end
                let offset = offset.parse::<i32>().unwrap();
                let reg_val = *registers.get(reg).unwrap();
                let is_jumping = (inst == "jie" && reg_val % 2 == 0) || (inst == "jio" && reg_val == 1);

                inst_cnt += if is_jumping { offset } else { 1 };
            },
            ["jmp", reg] => {
                inst_cnt += reg.parse::<i32>().unwrap();
            },
            [inst, reg] => {
                // Only edits existing k, v pairs
                registers.entry(reg).and_modify(|val| match inst {
                    "hlf" => *val /= 2,
                    "tpl" => *val *= 3,
                    "inc" => *val += 1,
                    _ => {},
                });
                inst_cnt += 1;
            }
            _ => {}
        }
    }
    *registers.get("b").unwrap()
}

fn main(){
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    let content: Vec<&str> = content.split('\n').collect();
    println!("Part A: {}", execute_program(&content, 0, 0));
    println!("Part B: {}", execute_program(&content, 1, 0));
}