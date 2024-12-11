#!/usr/bin/python3


data='''
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
'''.strip().splitlines()

data='''
'''.strip().splitlines()
all = {}

def matches(depth, rule, strings):
	if depth == 0:
		return (False, [''])
	
	if rule[0] is None:
		output = []
		for string in strings:
			if string == '':
				continue
			if string[0] == rule[1]:
				output.append(string[1:])
		return (True, output)
	
	output = []
	for currentList in rule:
		currentStrings = strings
		for currentElement in currentList:
			success, currentStrings = matches(depth-1, all[currentElement], currentStrings)
			if not success:
				break
		else:
			output.extend(currentStrings)
	if len(output) == 0:
		return (False, [''])
	else:
		return (True, output)

output=0
for line in data:
	if ':' in line:
		ruleName, definition = line.split(': ')
		if '"' in definition:
			definition = definition.replace('"', '')
			all[int(ruleName)] = [None, definition]
		else:
			definitions = definition.split(' | ')
			definitions = [[int(a) for a in definition.split(' ')] for definition in definitions]
			all[int(ruleName)] = definitions
	elif line == '':
		continue
	else:
		success, currentStrings = matches(600, all[0], [line])
		if success and '' in currentStrings:
			output+=1
	




print(output)

