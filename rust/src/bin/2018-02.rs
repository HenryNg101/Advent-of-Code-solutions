use my_project::get_input;

fn main(){
    let input = get_input(2018, 2)
        .expect("Can't get the content");

    let mut twos_cnt = 0;
    let mut threes_cnt = 0;
    let mut boxes: Vec<&str> = input.lines().collect();
    boxes.sort();   // Sort to find close strings easier
    let boxes: Vec<&[u8]> = boxes
        .into_iter()
        .map(|box_id| box_id.as_bytes())
        .collect();

    // Logic part A
    for box_id in boxes.iter() {
        // Logic part A
        let mut counter = [0; 26];
        for c in *box_id {
            counter[(c - b'a') as usize] += 1;
        }
        if counter.iter().any(|&cnt| cnt == 2) {
            twos_cnt += 1;
        }
        if counter.iter().any(|&cnt| cnt == 3) {
            threes_cnt += 1;
        }
    }
    println!("Part A: {}", twos_cnt * threes_cnt);

    for i in 1..boxes.len() {
        let mut diff_pos = None;

        for j in 0..boxes[i].len() {
            if boxes[i][j] != boxes[i-1][j] {
                if diff_pos == None {
                    diff_pos = Some(j);
                }
                else {
                    diff_pos = None;
                    break;
                }
            }
        }

        if let Some(id) = diff_pos {
            print!("Part B: ");
            for (j, &ch) in boxes[i].iter().enumerate() {
                if j != id {
                    print!("{}", ch as char);
                }
            }
            println!();
            break;
        }
    }
}