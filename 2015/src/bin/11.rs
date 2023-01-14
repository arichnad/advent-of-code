
#![allow(dead_code, unused, non_snake_case)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::str::Lines;

use fancy_regex::Regex;
use serde_json::to_string;

//noinspection DuplicatedCode
fn main() {

	let data1 = r#"
abcdefgh
ghijklmn
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();
	let data2 = r#"
hxbxwxba
"#.trim_matches('\n').lines().map(ToString::to_string).collect::<Vec<String>>();


	let unparsed = data2;

	let mut data = unparsed;
	//let mut data: Vec<Vec<i32>> = unparsed.iter().map(|line| Regex::new(r"-?\d+").unwrap().find_iter(line).map(|mat| mat.as_str().parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<i32> = unparsed.iter().map(|line| line.parse::<i32>().expect("need an integer")).collect();
	//let mut data: Vec<Vec<i32>> = unparsed.iter().map(|line| line.split_whitespace().map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//let mut data: Vec<Vec<i32>> = unparsed.iter().map(|line| line.split(',').map(|column| column.parse::<i32>().expect("need an integer")).collect()).collect();
	//json: println!("{}", to_string(&data).unwrap());

	let regex0 = Regex::new(r"[iol]").unwrap();
	let regex1 = Regex::new(r"(.)\1.*(.)\2").unwrap();

	let mut total = 0;
	for line in data {
		println!("{}", line);
		let mut dec = line.chars().map(|ch| ch as i8 - 'a' as i8).collect::<Vec<i8>>();
		loop {
			let mut last: Option<i8> = None;
			let mut len = 0;
			let mut good = false;
			for ch in &dec {
				if last != None {
					if last.unwrap() + 1 == *ch {
						len += 1;
						if len == 2 {
							good = true;
							break;
						}
					} else {
						len = 0;
					}
				}

				last = Some(*ch);
			}
			if good {
				let line: String = dec.iter().map(|ch| (ch + ('a' as i8)) as u8 as char).collect();
				if ! regex0.is_match(&line).unwrap() && regex1.is_match(&line).unwrap() {
					println!("{}", line);
					total += 1;
					if total == 2 {
						break;
					}
				}
			}
			for c in (0..dec.len()).rev() {
				dec[c]=(dec[c]+1)%26;
				if dec[c]!=0 {
					break;
				}
			}
		}
	}
}

