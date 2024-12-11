
#![allow(dead_code, unused, non_snake_case)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex; //for back references:  use fancy_regex::Regex;
use serde_json::{to_string, from_str, Value};
use itertools::Itertools; //collect_tuple

//noinspection DuplicatedCode
fn main() {

	let data1 = r#"

"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"

"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let mut data = data2;

	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//json: println!("{} {}", to_string(&data).unwrap(), from_str::<Value>(&data[0]).unwrap());

	'outer: for line in &data {
		let (name, things) = line.splitn(2, ": ").collect_tuple().unwrap();
		for thing in things.split(", ") {
			let (thing, num) = thing.split(": ").collect_tuple().unwrap();
			let num = num.parse::<i32>().unwrap();
			if thing == "children" && num != 3 ||
				thing == "cats" && num <= 7 ||
				thing == "samoyeds" && num != 2 ||
				thing == "pomeranians" && num >= 3 ||
				thing == "akitas" && num != 0 ||
				thing == "vizslas" && num != 0 ||
				thing == "goldfish" && num >= 5 ||
				thing == "trees" && num <= 3 ||
				thing == "cars" && num != 2 ||
				thing == "perfumes" && num != 1 {
				continue 'outer;
			}
		}
		println!("{}", name);
	}
}

