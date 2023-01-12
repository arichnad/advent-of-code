
#![allow(dead_code, unused, non_snake_case)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex;
use serde_json::to_string;

//noinspection DuplicatedCode
fn main() {

	let data1 = r#"
1
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"
1113122113
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let unparsed = data2[0].to_owned();

	let mut data = unparsed;
	//let data: Vec<Vec<i32>> = unparsed.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let data: Vec<i32> = unparsed.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let data: Vec<Vec<i32>> = unparsed.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let data: Vec<Vec<i32>> = unparsed.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//json: println!("{}", to_string(&data).unwrap());

	for i in 0..50 {
		let mut j = data.chars().peekable();
		let mut newData = String::new();
		loop {
			let ch = j.next();
			if ch.is_none() {
				break;
			}
			let ch = ch.unwrap();
			let mut k=1;
			while !j.peek().is_none() && j.peek().unwrap() == &ch {
				j.next();
				k += 1;
			}
			newData += &*format!("{}{}", k, ch);
		}
		data = newData;
	}
	println!("{}", data.len());
}

