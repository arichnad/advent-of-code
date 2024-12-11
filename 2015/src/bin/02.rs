
#![allow(dead_code, unused)]

use std::str::Lines;
use regex::Regex;

fn main() {

	let data1 : Lines = "
2x3x4
".trim_matches('\n').lines();
	let data2 : Lines = "
".trim_matches('\n').lines();


	let data = data2;

	//let parsed = data;
	let parsed: Vec<Vec<i32>> = data.map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<i32> = data.map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();

	// let mut total=0;
	// for line in parsed {
	// 	let mut min=-1;
	// 	let mut answer = 0;
	// 	for col in 0..line.len() {
	// 		let side = line[col] * line[(col+1)%line.len()];
	// 		answer += 2 * side;
	// 		if min == -1 || side < min {
	// 			min = side;
	// 		}
	// 	}
	// 	total += answer + min;
	// }
	// println!("{}", total);
	let mut total=0;
	for line in parsed {
		let mut min=-1;
		let mut answer = 0;
		for col in 0..line.len() {
			let side = line[col] * 2 + line[(col+1)%line.len()] * 2;
			if min == -1 || side < min {
				min = side;
			}
		}
		total += min + line[0]*line[1]*line[2];
	}
	println!("{}", total);
}

