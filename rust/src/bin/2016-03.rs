use my_project::get_input;

fn is_valid_triangle(sides: &[i32]) -> i32 {
    let &max_side = sides.iter().max().expect("No max side found");
    let total: i32 = sides.iter().sum();
    (max_side < total - max_side) as i32
}

fn main() {
    let content: Vec<Vec<i32>> = get_input(2016, 3)
        .expect("Can't get the content")
        .split('\n')
        .map(|line| {
            line.split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    let mut res_a = 0;
    let mut res_b = 0;

    for i in (0..content.len()).step_by(3) {
        for j in 0..3 {
            // Part A logic: Just calculate line by line
            res_a += is_valid_triangle(&content[i + j]);

            // Part B logic: Calculate by...columns
            let sides = [content[i][j], content[i+1][j], content[i+2][j]];
            res_b += is_valid_triangle(&sides);
        }
    }

    println!("Part A: {}", res_a);
    println!("Part B: {}", res_b);
}