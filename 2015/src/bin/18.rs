
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
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"

"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let mut data = data2;

	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.chars().map(|column| column.to_digit(10).expect("need an integer") as i32).collect()).collect();
	let mut data: Vec<Vec<char>> = data.iter().map(|line| line.chars().collect()).collect();
	//json: println!("{} {}", to_string(&data).unwrap(), from_str::<Value>(&data[0]).unwrap());

	let W = data[0].len();
	let H = data.len();

	data[0][0]='#';
	data[0][W-1]='#';
	data[H-1][W-1]='#';
	data[H-1][0]='#';
	for run in 0..100 {
		let mut newData = data.clone();
		for j in 0..H {
			for i in 0..W {
				let mut total = 0;
				for dx in -1..2 {
					for dy in -1..2 {
						if dx==0 && dy==0 {continue;}
						// if dx==0 && dy==0 || dx!=0 && dy!=0 {continue;}
						let newX= i as i32 + dx;
						let newY= j as i32 + dy;
						if newX<0 || newY<0 || newX as usize>=W || newY as usize>=H {continue;}
						let newX = newX as usize; let newY = newY as usize;
						total += if data[newY][newX]=='#' {1} else {0};
					}
				}
				if data[j][i]=='#' && (total != 2 && total!=3) {
					newData[j][i] = '.';
				}
				else if data[j][i]=='.' && total == 3 {
					newData[j][i] = '#';
				}
			}
		}
		newData[0][0]='#';
		newData[0][W-1]='#';
		newData[H-1][W-1]='#';
		newData[H-1][0]='#';
		data = newData;
	}
	let mut total =0;
	for j in 0..H {
		for i in 0..W { if data[j][i]=='#' {total+=1;} }
	}
	println!("{}", total); //814
}

