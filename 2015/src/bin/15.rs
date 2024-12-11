
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
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"

"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let mut data = data2;

	let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//json: println!("{} {}", to_string(&data).unwrap(), from_str::<Value>(&data[0]).unwrap());
	println!("{}", rec(0, 100, &data, &mut vec![0; data[0].len()]));
}

fn rec(row: usize, ts: i32, data: &Vec<Vec<i32>>, totals: &mut Vec<i32>) -> i32 {
	if row == data.len() {
		if ts != 0 || totals.last().unwrap() != &500 {
			return 0;
		}
		return totals[0..data[0].len()-1].iter().map(|&v| if v > 0 { v } else { 0 }).reduce(|a,b| a*b).unwrap();
	}
	let mut max = 0;
	for used in 0..ts+1 {
		for i in 0..data[row].len() {
			totals[i] += used * data[row][i];
		}
		let value = rec(row + 1, ts-used, data, totals);
		if value > max {
			max = value;
		}
		for i in 0..data[row].len() {
			totals[i] -= used * data[row][i];
		}
	}
	return max;
}

