use std::fs;

fn count_and_say(content: &str, iteration: usize) -> usize {
    let mut cpy: Vec<u8> = content.bytes().collect(); // Work with bytes directly for performance
    for _ in 0..iteration {
        let mut counter = 0;
        let mut rep = cpy[0];
        let mut new_sz = 0;

        // Calculate size of new string
        for &e in &cpy {
            if e != rep {
                while counter > 0 {
                    new_sz += 1;
                    counter /= 10;
                }
                new_sz += 1;
            }
            counter += 1;
        }
        while counter > 0 {
            new_sz += 1;
            counter /= 10;
        }
        new_sz += 1;


        // Fill in the data
        rep = cpy[0];
        counter = 0;
        let mut new_content = Vec::with_capacity(new_sz); // Pre-allocate to reduce reallocations
        for &e in &cpy {
            if e != rep {
                // Push the count and the character directly to `new_content`
                new_content.extend_from_slice(counter.to_string().as_bytes());
                new_content.push(rep);
                rep = e;
                counter = 0;
            }
            counter += 1;
        }        
        // Handle the last sequence
        new_content.extend_from_slice(counter.to_string().as_bytes());
        new_content.push(rep);
        
        cpy = new_content; // Update `cpy` with the new content
    }
    cpy.len()
}

fn main() {
    let content = fs::read_to_string("input.txt")
        .expect("Can't read from file");

    println!("{}", count_and_say(&content, 40));
    println!("{}", count_and_say(&content, 50));
}