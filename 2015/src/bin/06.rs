
#![allow(dead_code, unused)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex;

//noinspection DuplicatedCode
fn main() {

	let data1 = "
turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
".trim_matches('\n').lines().collect::<Vec<&str>>();
	let data2 = "
".trim_matches('\n').lines().collect::<Vec<&str>>();


	let data = data2;

	let parsed = data;
	//let parsed: Vec<Vec<usize>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<usize>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();

	let mut total : i32 = 0;
	let mut d : Vec<Vec<bool>> = vec![vec![false; 1000]; 1000];
	for line in &parsed {
		let values = Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<usize>().expect("need an integer")).collect::<Vec<usize>>();
		let (x1,y1,x2,y2) = (values[0], values[1], values[2], values[3]);
		for x in x1..x2+1 {
			for y in y1..y2+1 {
				if line.starts_with("toggle") {
					total += if d[y][x] { -1 } else { 1 };
					d[y][x] = !d[y][x];
				}
				else if line.starts_with("turn on") {
					total += if d[y][x] { 0 } else { 1 };
					d[y][x] = true;
				}
				else if line.starts_with("turn off") {
					total += if d[y][x] { -1 } else { 0 };
					d[y][x] = false;
				}
			}
		}
	}
	println!("{}", total);

	let mut total : i32 = 0;
	let mut d : Vec<Vec<i32>> = vec![vec![0; 1000]; 1000];
	for line in &parsed {
		let values = Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<usize>().expect("need an integer")).collect::<Vec<usize>>();
		let (x1,y1,x2,y2) = (values[0], values[1], values[2], values[3]);
		for x in x1..x2+1 {
			for y in y1..y2+1 {
				if line.starts_with("toggle") {
					d[y][x] += 2;
					total += 2;
				}
				else if line.starts_with("turn on") {
					d[y][x]+=1;
					total += 1;
				}
				else if line.starts_with("turn off") {
					total += if d[y][x]>0 { -1 } else { 0 };
					d[y][x] += if d[y][x]>0 { -1 } else { 0 };
				}
			}
		}
	}
	println!("{}", total);
}

