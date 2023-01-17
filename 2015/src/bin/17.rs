
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
20
15
10
5
5
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"
33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let mut data = data2; let TOTAL = 150;

	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	let mut data: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//json: println!("{} {}", to_string(&data).unwrap(), from_str::<Value>(&data[0]).unwrap());

	for containers in 1..data.len() {
		let mut answer = 0;
		for i in 0i32..1<<data.len() {
			if i.count_ones() != containers as u32 {
				continue;
			}
			let mut cur = i;
			let mut total = 0;
			for j in 0..data.len() {
				if cur&1==1 {
					total+=data[j];
				}
				cur>>=1;
			}
			if total==TOTAL {
				answer+=1;
			}
		}
		if answer > 0 {
			println!("{} {}", containers, answer);
			break;
		}
	}
}

