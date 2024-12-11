
#![allow(dead_code, unused)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex;

//noinspection DuplicatedCode
fn main() {

	let data1 = r#"
""
"abc"
"aaa\"aaa"
"\x27"
"#.trim_matches('\n').lines().collect::<Vec<&str>>();
	let data2 = r#"

"#.trim_matches('\n').lines().collect::<Vec<&str>>();


	let data = data2;

	let parsed = data;
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();

	let mut total : i32 = 0;
	for line in &parsed {
		let mut out : i32 = -2;
		let mut chars = line.chars();
		loop {
			let ch = chars.next();
			if ch.is_none() {
				break;
			}
			let ch = ch.unwrap();
			if ch == '\\' {
				let ch = chars.next().unwrap();
				if ch == 'x' {
					chars.next();
					chars.next();
				}
			}
			out+=1;
		}
		total += line.len() as i32 - out;
	}
	println!("{}", total);
	let mut total : i32 = 0;
	for line in &parsed {
		let mut out : i32 = 2;
		let mut chars = line.chars();
		loop {
			let ch = chars.next();
			if ch.is_none() {
				break;
			}
			let ch = ch.unwrap();
			if ch == '\\' || ch == '"' {
				out+=1;
			}
			out+=1;
		}
		total += out - line.len() as i32;
	}
	println!("{}", total);
}

