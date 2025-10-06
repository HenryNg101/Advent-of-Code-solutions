use my_project::get_input;

#[derive(Clone)]
struct Node {
    metadatas: Vec<i32>,
    childrens: Vec<Node>,
    value: i32
}

impl Node {
    fn new(metadatas: Vec<i32>, childrens: Vec<Node>) -> Self {
        Node {metadatas, childrens, value: 0}
    }
}

// So basically, the data was given in such a way that resembles postorder traversal of N-array tree
// The format is like: [child nodes count, metadata count, [content of child nodes from leftmost to rightmost], metadata]
fn create_tree(input: &Vec<i32>, id: &mut usize, res_a: &mut i32) -> Node {
    let child_count = input[*id] as usize;
    let metadata_count = input[*id+1] as usize;
    *id += 2;
    let mut childrens = vec![Node::new(vec![], vec![]); child_count];
    let mut metadatas = vec![0; metadata_count];

    for i in 0..child_count {
        childrens[i] = create_tree(input, id, res_a);
    }
    for i in 0..metadata_count {
        metadatas[i] = input[*id];
        *res_a += input[*id];
        *id += 1;
    }
    Node::new(metadatas, childrens)
}

fn traverse_tree(root: &mut Node) -> i32 {
    if root.value > 0 {
        return root.value;
    }
    if root.childrens.is_empty() {
        for val in &root.metadatas {
            root.value += val;
        }
    }
    else {
        for &id in &root.metadatas {
            if id as usize <= root.childrens.len() {
                root.value += traverse_tree(&mut root.childrens[id as usize -1]);
            }
        }
    }
    root.value
}

fn main(){
    let input = get_input(2018, 8)
        .expect("Can't get the content");

    let input: Vec<i32> = input
        .split(' ')
        .map(|num| num.parse().unwrap())
        .collect();
    let mut id = 0;
    let mut res_a = 0;
    let mut root_node = create_tree(&input, &mut id, &mut res_a);
    println!("Part A: {}", res_a);
    println!("Part B: {}", traverse_tree(&mut root_node));
}