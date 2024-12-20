
#![allow(dead_code, unused)]

use std::str::Lines;
use regex::Regex;

fn main() {

	let data1 : Lines = "
(())
".trim_matches('\n').lines();
	let data2 : Lines = "
".trim_matches('\n').lines();


	let data = data2;

	let parsed = data;
	//let parsed: Vec<Vec<i32>> = data.map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<i32> = data.map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();

	for line in parsed {
		let mut n=0;
		let mut position = 1;
		for ch in line.chars() {
			if ch == '(' {
				n += 1;
			}
			else if ch == ')' {
				n-=1;
			}
			if n<0 {
				break;
			}
			position+=1;
		}
		println!("{} {}", n, position);
	}
}

