
#![allow(dead_code, unused)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex;

//noinspection DuplicatedCode
fn main() {

	let data1 = "
abcdef
".trim_matches('\n').lines().collect::<Vec<&str>>();
	let data2 = "
".trim_matches('\n').lines().collect::<Vec<&str>>();


	let data = data2;

	let parsed = data;
	//let parsed: Vec<Vec<i32>> = data.map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<i32> = data.map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();

	let n : u32 = 9999999;

	for line in &parsed {
		for i in 0..n {
			let value = line.to_string() + &i.to_string();
			if format!("{:x}", md5::compute(&value)).get(0..6).unwrap() == "000000" {
				println!("{}", value);
				break;
			}
		}
	}
}

