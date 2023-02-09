
#![allow(dead_code, unused, non_snake_case)]

use std::cmp::min;
use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use regex::Regex; //for back references:  use fancy_regex::Regex;
use serde_json::{to_string, from_str, Value};
use itertools::{enumerate, Itertools}; //collect_tuple

//noinspection DuplicatedCode
fn main() {

	let data1 = r#"
H => HO
H => OH
O => HH

HOHOHO
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"
Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();

	let data3 = r#"
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let mut data = data2;

	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.chars().map(|column| column.to_digit(10).expect("need an integer") as i32).collect()).collect();
	//let mut data: Vec<Vec<char>> = data.iter().map(|line| line.chars().collect()).collect();
	//json: println!("{} {}", to_string(&data).unwrap(), from_str::<Value>(&data[0]).unwrap());

	let mut tokens : Vec<String> = vec![];
	// let mut lookup : HashMap<String, u16> = HashMap::new();
	let mut d : HashMap<usize, Vec<Vec<usize>>> = HashMap::new();
	for (line) in &data {
		if line == "" {
			break;
		}

		let (from, to) = line.split(" => ").collect_tuple().unwrap();
		let from = from.to_string();
		if !tokens.contains(&from) {
			tokens.push(from);
		}
	}
	let endTokenPosition = tokens.len();
	let mut last : Vec<usize> = vec![];
	let lastEndTokens : Vec<&usize> = get_end_tokens(&last, endTokenPosition);

	for (i, line) in enumerate(&data) {
		if line == "" {
			last=parse(&data[i+1], &mut tokens);
			break;
		}

		let (from, to) = line.split(" => ").collect_tuple().unwrap();
		let from = find(from, &tokens);
		let to = parse(to, &mut tokens);
		println!("{:?} => {:?}", tokens[from], to.iter().map(|ch| tokens[*ch].as_str()).collect::<Vec<&str>>());
		d.entry(from).or_insert_with(|| vec![]).push(to);
	}
	println!("{:?} {:?}", tokens, endTokenPosition);
	let mut results : HashSet<Vec<usize>> = HashSet::new();
	for (key, values) in d {
		for position in last.iter().positions(|last| last==&key) {
			for value in &values {
				let mut cur = last.clone();
				cur.splice(position..position + 1, value.iter().cloned());
				results.insert(cur);
			}
		}
	}
	println!("{}", results.len());

	let mut last : Vec<usize> = vec![];
	let mut d : HashMap<usize, Vec<Vec<usize>>> = HashMap::new();
	for (i, line) in enumerate(&data) {
		if line == "" {
			last=parse(&data[i+1], &mut tokens);
			break;
		}

		let (from, to) = line.split(" => ").collect_tuple().unwrap();
		let from = find(from, &tokens);
		let to = parse(to, &mut tokens);
		d.entry(from).or_insert_with(|| vec![]).push(to);
	}

	let mut forwardState: HashSet<(Vec<usize>, usize)> = HashSet::new();
	let start = parse("e", &mut tokens);
	forwardState.insert((start, 0));
	// visited.insert(end.clone());
	println!("{}", is_subset(&vec![&0], &vec![&0]));
	println!("{}", is_subset(&vec![&1, &2, &3], &vec![&1, &2, &3]));
	println!("{}", is_subset(&vec![&1, &2, &3], &vec![&1, &2, &3, &3, &3]));
	println!("{}", is_subset(&vec![&1, &2, &3], &vec![&1, &2, &3, &0, &0]));
	return;
	let mut count = 0;
	'outer: loop {
		let mut newForwardState: HashSet<(Vec<usize>, usize)> = HashSet::new();
		count += 1;
		for (from, minimumPosition) in forwardState.iter() {
			for (key, values) in &d {
				for position in from[*minimumPosition..].iter().positions(|last| last==key).map(|position| position+minimumPosition) {
					for value in values {
						let mut cur = from.clone();
						cur.splice(position..position + 1, value.iter().cloned());

						let curEndTokens : Vec<&usize> = get_end_tokens(&cur, endTokenPosition);
						// if !is_subset(curEndTokens, &lastEndTokens) {
						// 	//7: 305987 to
						// 	continue;
						// }

						// if visited.contains(&cur) {
						// 	continue;
						// }
						// visited.insert(cur.clone());
						if cur == last {
							println!("answer {}", count);
							break 'outer;
						}
						newForwardState.insert((cur, position));
					}
				}
			}
		}
		// let mut newBackwardState: HashSet<String> = HashSet::new();
		// for from in backwardState.iter() {
		// 	for (key, values) in &e {
		// 		for (position, entry) in from.match_indices(key) {
		// 			for value in values {
		// 				let mut cur = (*from).clone();
		// 				cur.replace_range(position..position + entry.len(), value);
		// 				// if visited.contains(&cur) {
		// 				// 	continue;
		// 				// }
		// 				// visited.insert(cur.clone());
		// 				if forwardState.contains(&cur) {
		// 					println!("answer {}", count * 2 - 1);
		// 					break 'outer;
		// 				}
		// 				if newForwardState.contains(&cur) {
		// 					println!("answer {}", count * 2);
		// 					break 'outer;
		// 				}
		// 				newBackwardState.insert(cur);
		// 			}
		// 		}
		// 	}
		// }
		forwardState = newForwardState;
		// backwardState = newBackwardState;
		println!("{} {}", count, forwardState.len());
	}
}

fn is_subset(inner: &Vec<&usize>, outer: &Vec<&usize>) -> usize {
	let mut value : Vec<Vec<usize>> = vec![vec![0; outer.len()] ; inner.len()];
	//levenshtein distance, additions are free, changes are 1, and deletions are 1
	for (j, innerToken) in enumerate(inner) {
		for (i, outerToken) in enumerate(outer) {
			value[j][i] = if j>0 {value[j-1][i]} else {usize::MAX}
				.min(if i>0 {value[j][i-1]} else {usize::MAX})
				.min(if i>0 && j>0 {value[j-1][i-1]} else {0}) +
				if innerToken!=outerToken {1} else {0};
		}
	}
	return *value.last().unwrap().last().unwrap();
}

fn get_end_tokens(tokens: & Vec<usize>, endTokenPosition: usize) -> Vec<&usize> {
	return tokens.iter().filter(|token| token >= &&endTokenPosition).collect()
}

fn parse(string: &str, tokens: &mut Vec<String>) -> Vec<usize> {
	let mut string = string.to_string();
	let mut output : Vec<usize> = vec![];
	let mut current = "".to_string();
	while string.len() > 0 {
		let character = string.remove(0);
		if character.is_uppercase() && current != "" {
			if !tokens.contains(&current) {
				println!("found {}", current);
				tokens.push(current.to_string());
			}
			output.push(find(current.as_str(), tokens));
			current.clear();
		}
		current.push(character);
	}
	if !tokens.contains(&current) {
		println!("found {} at end", current);
		tokens.push(current.to_string());
	}
	output.push(find(current.as_str(), tokens));
	return output
}

fn find(current: &str, tokens: &Vec<String>) -> usize {
	return tokens.iter().position(|token| current == token).unwrap();
}

