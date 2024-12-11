
#![allow(dead_code, unused, non_snake_case)]

use std::collections::HashMap;
use std::collections::HashSet;
use itertools::Itertools; //collect_tuple

use std::str::Lines;
use regex::Regex; //for back references:  use fancy_regex::Regex;
use serde_json::{to_string, from_str, Value};

//noinspection DuplicatedCode
fn main() {

	let data1 = r#"
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"

"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let mut data = data2;

	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<i32> = data.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = data.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//json: println!("{} {}", to_string(&data).unwrap(), from_str::<Value>(&data[0]).unwrap());

	let mut m : HashMap<(String,String), i32> = HashMap::new();
	let mut people : HashSet<String> = HashSet::new();
	for line in &data {
		let line = line.replace(".", "");
		let (person1, would, gain, number, happiness, units, by, sitting, next, to, person2) = line.split_whitespace().collect_tuple().unwrap();
		let number = number.parse::<i32>().unwrap();
		people.insert(person1.to_string());
		m.insert((person1.to_string(),person2.to_string()), if gain=="gain" { number } else { -number });
	}

	//part 2
	let you : String = "you".to_string();
	for person in &people {
		m.insert((person.to_string(), you.to_string()), 0);
		m.insert((you.to_string(), person.to_string()), 0);
	}
	people.insert("you".to_string());


	println!("{}", rec(0, &people, &m, &mut vec!["".to_string(); people.len()]));
}

fn rec(index: usize, people: &HashSet<String>, m: &HashMap<(String, String), i32>, order: &mut Vec<String>) -> i32 {
	if index == order.len() {
		return m.get(&(order[index-1].to_string(), order[0].to_string())).unwrap() +
			m.get(&(order[0].to_string(), order[index-1].to_string())).unwrap();
	}
	let mut max : Option<i32> = None;
	for person in people {
		if (&order).get(0..index).unwrap().contains(person) {
			continue;
		}

		order[index]=person.to_string();
		let mut value = 0;
		if index>0 {
			value += m.get(&(order[index].to_string(), order[index-1].to_string())).unwrap() +
				m.get(&(order[index-1].to_string(), order[index].to_string())).unwrap();
		}
		let result = value + rec(index+1, people, m, order);
		if max == None || result > max.unwrap() {
			max = Some(result);
		}
	}
	return max.unwrap();
}

