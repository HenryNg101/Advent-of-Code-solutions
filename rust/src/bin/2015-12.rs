use serde_json::Value;
use my_project::get_input;

fn traverse(json_doc: &Value, ignore_value: Option<&str>) -> i64 {
    match json_doc {
        // If it's array, just traverse and get the sum
        Value::Array(arr) => arr.iter().map(|x| traverse(x, ignore_value)).sum(),

        // If it's object, check if it has the forbidden value or not, if not, treat it same as array
        Value::Object(obj) => {
            if ignore_value.is_some() && obj.values().any(|val| val == ignore_value.unwrap()) {
                return 0;
            }
            obj.values().map(|val| traverse(val, ignore_value)).sum()
        },
        
        // Simple number -> just add
        Value::Number(num) => num.as_i64().unwrap_or(0),
        _ => 0
    }
}

fn main(){
    let content = get_input(2015, 12).expect("Can't read from file");

    // Parse JSON data into an unstructured json data form
    let parsed_json: Value = serde_json::from_str(&content)
        .expect("Failed to parse JSON");

    println!("Part A: {}", traverse(&parsed_json, None));
    println!("Part B: {}", traverse(&parsed_json, Some("red")));
}