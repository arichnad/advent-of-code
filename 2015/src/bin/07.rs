
#![allow(dead_code, unused)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex;

//noinspection DuplicatedCode
fn main() {

	let data1 = "
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
".trim_matches('\n').lines().collect::<Vec<&str>>();
	let data2 = "
".trim_matches('\n').lines().collect::<Vec<&str>>();


	let data = data2;

	let parsed = data;
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();

	let mut d : HashMap<&str, u16> = HashMap::new();
	d.insert("1", 1);
	let mut changes : bool = true;
	while changes {
		changes = false;
		for line in &parsed {
			let line = line.split(" -> ").collect::<Vec<&str>>();
			let b = line[1];
			let line = line[0].split(" ").collect::<Vec<&str>>();
			if line.len() == 1 {
				if !d.contains_key(b) && line[0].parse::<u16>().is_ok() {
					d.insert(b, line[0].parse::<u16>().unwrap());
					changes = true;
				}
				else if !d.contains_key(b) && !line[0].parse::<u16>().is_ok() && d.contains_key(line[0]) {
					d.insert(b, *d.get(line[0]).unwrap());
					changes = true;
				}
			}
			else if line.len() == 2 && d.contains_key(line[1]) && !d.contains_key(b) {
				d.insert(b, !*d.get(line[1]).unwrap());
				changes = true;
			}
			else if line.len() == 3 && d.contains_key(line[0]) && !d.contains_key(b) {
				if line[1]=="AND" && d.contains_key(line[2]) {
					changes = true;
					d.insert(b, d.get(line[0]).unwrap() & d.get(line[2]).unwrap());
				}
				else if line[1]=="OR" && d.contains_key(line[2]) {
					changes = true;
					d.insert(b, d.get(line[0]).unwrap() | d.get(line[2]).unwrap());
				}
				else if line[1]=="LSHIFT" {
					changes = true;
					d.insert(b, d.get(line[0]).unwrap() << line[2].parse::<u16>().unwrap());
				}
				else if line[1]=="RSHIFT" {
					changes = true;
					d.insert(b, d.get(line[0]).unwrap() >> line[2].parse::<u16>().unwrap());
				}
			}
		}
		// for (key, value) in &d {
		// 	println!("{}: {}", key, value);
		// }
	}
	let a = d.get("a").unwrap();
	println!("{}", a);
	let mut d : HashMap<&str, u16> = HashMap::new();
	d.insert("1", 1);
	d.insert("b", *a);
	let mut changes : bool = true;
	while changes {
		changes = false;
		for line in &parsed {
			let line = line.split(" -> ").collect::<Vec<&str>>();
			let b = line[1];
			let line = line[0].split(" ").collect::<Vec<&str>>();
			if line.len() == 1 {
				if !d.contains_key(b) && line[0].parse::<u16>().is_ok() {
					d.insert(b, line[0].parse::<u16>().unwrap());
					changes = true;
				}
				else if !d.contains_key(b) && !line[0].parse::<u16>().is_ok() && d.contains_key(line[0]) {
					d.insert(b, *d.get(line[0]).unwrap());
					changes = true;
				}
			}
			else if line.len() == 2 && d.contains_key(line[1]) && !d.contains_key(b) {
				d.insert(b, !*d.get(line[1]).unwrap());
				changes = true;
			}
			else if line.len() == 3 && d.contains_key(line[0]) && !d.contains_key(b) {
				if line[1]=="AND" && d.contains_key(line[2]) {
					changes = true;
					d.insert(b, d.get(line[0]).unwrap() & d.get(line[2]).unwrap());
				}
				else if line[1]=="OR" && d.contains_key(line[2]) {
					changes = true;
					d.insert(b, d.get(line[0]).unwrap() | d.get(line[2]).unwrap());
				}
				else if line[1]=="LSHIFT" {
					changes = true;
					d.insert(b, d.get(line[0]).unwrap() << line[2].parse::<u16>().unwrap());
				}
				else if line[1]=="RSHIFT" {
					changes = true;
					d.insert(b, d.get(line[0]).unwrap() >> line[2].parse::<u16>().unwrap());
				}
			}
		}
		// for (key, value) in &d {
		// 	println!("{}: {}", key, value);
		// }
	}
	println!("{}", d.get("a").unwrap());
}

