
#![allow(dead_code, unused, non_snake_case)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex; //for back references:  use fancy_regex::Regex;
use serde_json::{to_string, from_str, Value};

//noinspection DuplicatedCode
fn main() {

	let data1 = r#"
[1,2,3] and {"a":2,"b":4} [[[3]]] and {"a":{"b":4},"c":-1} {"a":[-1,1]} and [-1,{"a":1}] [] and {}
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"

"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let mut data = data2;

	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//json: println!("{} {}", to_string(&data).unwrap(), from_str::<Value>(&data[0]).unwrap());

	{
		let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
		println!("{}", data[0].iter().sum::<i32>());
	}
	{
		let data : Value = from_str(&data[0]).unwrap();
		println!("{}", recurse(&data));
	}
}

fn recurse(element: &Value) -> i64 {
	//adding a nightly feature is super annoying!
	fn is_some_and<T>(option: &Option<T>, f: impl FnOnce(&T) -> bool) -> bool {
		matches!(option, Some(x) if f(x))
	}
	match element {
		Value::Object(map) => if map.values().any(|value| is_some_and(&value.as_str(), |&s|s == "red")) {0} else { map.values().map(|val| recurse(val)).sum() },
		Value::Number(number) => number.as_i64().unwrap(),
		Value::Array(array) => array.iter().map(|val| recurse(val)).sum(),
		_ => 0
	}
}


