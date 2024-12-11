
#![allow(dead_code, unused)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use fancy_regex::Regex;

//noinspection DuplicatedCode
fn main() {

// 	let data1 = "
// ugknbfddgicrmopn
// aaa
// jchzalrnumimnmhp
// haegwjzuvuyypxyu
// dvszwmarrgswjxmb
// ".trim_matches('\n').lines().collect::<Vec<&str>>();
	let data1 = "
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy
".trim_matches('\n').lines().collect::<Vec<&str>>();
	let data2 = "
".trim_matches('\n').lines().collect::<Vec<&str>>();


	let data = data2;

	let parsed = data;
	//let parsed: Vec<Vec<i32>> = data.map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<i32> = data.map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let parsed: Vec<Vec<i32>> = data.map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();

	let mut answer = 0;
	for line in &parsed {

		if !Regex::new(r"[aeiou].*[aeiou].*[aeiou]").unwrap().is_match(line).unwrap() {
			continue;
		}
		if !Regex::new(r"(.)\1").unwrap().is_match(line).unwrap() {
			continue;
		}
		if line.contains("ab") || line.contains("cd") || line.contains("pq") || line.contains("xy") {
			continue;
		}
		answer+=1;
	}
	println!("{}", answer);

	let mut answer = 0;
	for line in &parsed {

		if !Regex::new(r"(..).*\1").unwrap().is_match(line).unwrap() {
			continue;
		}
		if !Regex::new(r"(.).\1").unwrap().is_match(line).unwrap() {
			continue;
		}
		answer+=1;
	}
	println!("{}", answer);
}

