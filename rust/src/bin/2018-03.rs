use my_project::get_input;

fn overlap_check(rect1: &[usize; 4], rect2: &[usize; 4]) -> bool {
    /* 4 cases of them not colliding: 
        - bottom side of rect1 is on the top of the top side of rect2
        - Or bottom side of rect2 is on the top of the top side of rect1
        - right side of rect1 is on the left of the left side of rect2
        - Or right side of rect2 is on the left of the left side of rect1
    */
    if rect1[0] + rect1[2] -1 < rect2[0]
    || rect1[0] > rect2[0] + rect2[2] - 1
    || rect1[1] + rect1[3] - 1 < rect2[1]
    || rect1[1] > rect2[1] + rect2[3] - 1 {
        return false;
    }
    true
}

fn process_line(line: &str) -> [usize; 4] {
    let words: Vec<&str> = line.split_whitespace().collect();
    let coordinates: Vec<usize> = words[2][..words[2].len()-1]
        .split(',')
        .map(|coordinate| coordinate.parse().unwrap())
        .collect();
    let sizes: Vec<usize> = words[3]
        .split('x')
        .map(|sz| sz.parse().unwrap())
        .collect();

    [coordinates[1], coordinates[0], sizes[1], sizes[0]]    // r, c, sz_r, sz_c
}

fn main(){
    let input = get_input(2018, 3)
        .expect("Can't get the content");

    let boxes: Vec<[usize; 4]> = input
        .lines()
        .map(|line| process_line(line))
        .collect();
    let mut fabric = [[0; 1000]; 1000];
    let mut is_overlap = vec![false; boxes.len()];
    let mut res_a = 0;

    for (id, box_id) in boxes.iter().enumerate() {
        for i in 0..id {
            if overlap_check(box_id, &boxes[i]){
                is_overlap[id] = true;
                is_overlap[i] = true;
            }
        }
        
        for i in 0..box_id[2] {
            for j in 0..box_id[3] {
                fabric[box_id[0] + i][box_id[1] + j] += 1;
            }
        }
    }
    for i in 0..1000 {
        for j in 0..1000 {
            if fabric[i][j] > 1 {
                res_a += 1;
            }
        }
    }
    println!("Part A: {}", res_a);

    // Part B
    for i in 0..is_overlap.len() {
        if !is_overlap[i] {
            println!("Part B: {}", i + 1);
            break;
        }
    }
}