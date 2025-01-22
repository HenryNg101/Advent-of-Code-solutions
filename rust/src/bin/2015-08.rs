use std::fs;

fn main(){
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    let mut res_a = 0;
    let mut res_b = 0;

    for line in content.lines() {
        let line = line.as_bytes();
        // Logic part A
        let mut id = 1;
        let mut mem_count = 0;
        while id < line.len() - 1  {
            if line[id] == b'\\' {
                id += 1;
                if line[id] == b'x' {
                    id += 2;
                }
            }
            id += 1;
            mem_count += 1;
        }
        res_a += line.len() - mem_count;

        // Logic part B. Added 2 to include the pair of double quotes that u always needed
        res_b += line.iter().filter(|&&chr| chr == b'\"' && chr == b'\\').count() + 2;
    }
    println!("Part A: {}", res_a);
    println!("Part B: {}", res_b);
}