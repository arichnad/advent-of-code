
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
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"

"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let mut data = data2;

	let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//json: println!("{} {}", to_string(&data).unwrap(), from_str::<Value>(&data[0]).unwrap());

	let total = 2503;
	let mut max = 0;
	for line in &data {
		let (speed, flying, rest) = line.iter().collect_tuple().unwrap();
		let value = total %(flying+rest);
		let mut distance = total /(flying+rest) * flying * speed;
		if &value < flying {
			distance += value * speed;
		}
		else {
			distance += flying * speed;
		}
		if distance > max {
			max = distance;
		}
	}
	println!("{}", max);

	let mut points = vec![0; data.len()];
	for time in 1..total+1 {
		let mut max = 0;
		let mut maxI = 0;
		for i in 0..data.len() {
			let line = &data[i];
			let (speed, flying, rest) = line.iter().collect_tuple().unwrap();
			let value = time %(flying+rest);
			let mut distance = time /(flying+rest) * flying * speed;
			if &value < flying {
				distance += value * speed;
			}
			else {
				distance += flying * speed;
			}
			if distance > max {
				max = distance;
			}
		}
		for i in 0..data.len() {
			let line = &data[i];
			let (speed, flying, rest) = line.iter().collect_tuple().unwrap();
			let value = time %(flying+rest);
			let mut distance = time /(flying+rest) * flying * speed;
			if &value < flying {
				distance += value * speed;
			}
			else {
				distance += flying * speed;
			}
			if distance == max {
				points[i]+=1;
			}
		}
	}
	println!("{}", points.iter().reduce(core::cmp::max).unwrap());
}

