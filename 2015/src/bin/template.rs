
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


	let mut data = data1;

	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.chars().map(|column| column.to_digit(10).expect("need an integer") as i32).collect()).collect();
	//let mut data: Vec<Vec<char>> = data.iter().map(|line| line.chars().collect()).collect();
	//json: println!("{} {}", to_string(&data).unwrap(), from_str::<Value>(&data[0]).unwrap());

	/*
	let mut data: Vec<Vec<char>> = data.iter().map(|line| line.chars().collect()).collect();
	let W = data[0].len();
	let H = data.len();
	for j in 0..H {
		for i in 0..W {
			let mut total = 0;
			for dx in -1..2 {
				for dy in -1..2 {
					// if dx==0 && dy==0 {continue;}
					if dx==0 && dy==0 || dx!=0 && dy!=0 {continue;}
					let newX = i as i32 + dx;
					let newY = j as i32 + dy;
					if newX<0 || newY<0 || newX as usize>=W || newY as usize>=H {continue;}
					let newX = newX as usize; let newY = newY as usize;
				}
			}
		}
	}
	for j in 0..H {
		for i in 0..W { print!("{}", data[j][i]); }
		println!();
	}
	*/

	for line in &data {

	}
}

