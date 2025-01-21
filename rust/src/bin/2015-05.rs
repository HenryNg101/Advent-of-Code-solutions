use std::{collections::HashMap, fs};

fn main(){
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    let mut res_a = 0;
    let mut res_b = 0;

    for line in content.lines(){
        // Check for part A
        let mut vowels_cnt = 0;
        let mut continuous = false;
        let mut valid = true;
        let byte_arr = line.as_bytes();

        for (id, chr) in byte_arr.iter().enumerate(){
            // Checking for vowels counting and making sure that the forbidden substrings aren't in the string
            match chr {
                b'a' | b'e' | b'i' | b'o' | b'u' => vowels_cnt += 1,
                b'b' | b'd' | b'q' | b'y' => if id > 0 {
                    valid &= *chr != byte_arr[id-1] + 1
                },
                _ => {}
            }
            // Check last condition
            if id > 0 && *chr == byte_arr[id-1] {
                continuous = true;
            }
        }
        if vowels_cnt >= 3 && continuous && valid {
            res_a += 1;
        }

        // Check for part B
        let mut check = false;
        let mut check2 = false;
        let mut mp = HashMap::new();

        for i in 0..byte_arr.len() - 1 {
            // Check with first condition
            let first_occurence = mp.entry(&byte_arr[i..i+2]).or_insert(i);
            check |= i - *first_occurence > 1;

            // Check with the second condition
            check2 |= i < byte_arr.len() - 2 && byte_arr[i] == byte_arr[i+2];

            if check && check2 {
                res_b += 1;
                break;
            }
        }
    }
    println!("Part A: {}", res_a);
    println!("Part B: {}", res_b);
}