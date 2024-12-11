
#![allow(dead_code, unused)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex;

fn main() {

	let data1 = "
^>v<
".trim_matches('\n').lines().collect::<Vec<&str>>();
	let data2 = "
".trim_matches('\n').lines().collect::<Vec<&str>>();


	let data = data2;

	let parsed = data;
	//let parsed: Vec<Vec<i32>> = data.map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<i32> = data.map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();

	let mut places = HashSet::new();
	for line in &parsed {
		let mut x : i32=0;
		let mut y : i32=0;

		for ch in line.chars() {
			if ch=='<' {
				x-=1;
			}
			else if ch=='>' {
				x+=1;
			}
			else if ch=='^' {
				y-=1;
			}
			else if ch=='v' {
				y+=1;
			}
			places.insert((x,y));
		}
		println!("{}", places.len());

	}
	let mut places = HashSet::new();
	for line in &parsed {
		let mut x1 : i32=0;
		let mut y1 : i32=0;
		let mut x2 : i32=0;
		let mut y2 : i32=0;
		let mut iter = line.chars();
		loop {
			let next = iter.next();
			if next.is_none() {
				break;
			}
			let ch = next.unwrap();
			if ch=='<' {
				x1-=1;
			}
			else if ch=='>' {
				x1+=1;
			}
			else if ch=='^' {
				y1-=1;
			}
			else if ch=='v' {
				y1+=1;
			}
			places.insert((x1,y1));

			let next = iter.next();
			if next.is_none() {
				break;
			}
			let ch = next.unwrap();
			if ch=='<' {
				x2-=1;
			}
			else if ch=='>' {
				x2+=1;
			}
			else if ch=='^' {
				y2-=1;
			}
			else if ch=='v' {
				y2+=1;
			}
			places.insert((x2,y2));
		}
		println!("{}", places.len());

	}
}

