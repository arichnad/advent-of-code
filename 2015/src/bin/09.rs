
#![allow(dead_code, unused, non_snake_case)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex;
use serde_json::to_string;

//noinspection DuplicatedCode
fn main() {

	let data1 = r#"
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"#.trim_matches('\n').lines().collect::<Vec<&str>>();
	let data2 = r#"

"#.trim_matches('\n').lines().collect::<Vec<&str>>();


	let data = data2;

	let parsed = data;
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//json: println!("{}", to_string(&data).unwrap());

	let mut d : HashMap<&str, Vec<(&str, i32)>> = HashMap::new();
	let mut e : HashSet<(Vec<&str>, i32)> = HashSet::new();
	for line in &parsed {
		let line = line.split(" = ").collect::<Vec<&str>>();
		let distance = line[1].parse::<i32>().unwrap();
		let mut line = line[0].split(" to ");
		let a=line.next().unwrap();
		let b=line.next().unwrap();
		if d.get(a).is_none() {
			d.insert(a, vec!());
		}
		let v: &mut Vec<(&str, i32)> = &mut d.get_mut(a).unwrap();
		v.push((b, distance));

		if d.get(b).is_none() {
			d.insert(b, vec!());
		}
		let v: &mut Vec<(&str, i32)> = &mut d.get_mut(b).unwrap();
		v.push((a, distance));

		e.insert((vec![a], 0));
	}

	loop {
		let mut minimum = -1i32;
		let mut maximum = -1i32;
		let mut newE : HashSet<(Vec<&str>, i32)> = HashSet::new();
		for (places, totalDistance) in &e {
			if minimum == -1 || *totalDistance < minimum {
				minimum = *totalDistance;
			}
			if maximum == -1 || *totalDistance > maximum {
				maximum = *totalDistance;
			}
			for (connection, distance) in d.get(places.last().unwrap()).unwrap() {
				if places.contains(connection) {
					continue;
				}
				let mut newPlaces = places.clone();
				newPlaces.push(connection);
				newE.insert((newPlaces, totalDistance + distance));
			}
		}

		if newE.len() == 0 {
			println!("{} {}", minimum, maximum);
			break;
		}
		e = newE;
	}
}

