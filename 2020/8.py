#!/usr/bin/python3

data='''
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''.strip().splitlines()

data='''
'''.strip().splitlines()

data=[(line[0], int(line[1])) for line in [line.split(' ') for line in data]]

visited=set()
pc,acc=0,0

while pc not in visited:
	visited.add(pc)
	instruction, value = data[pc]
	if instruction == 'jmp':
		pc+=value
		continue
	if instruction == 'acc':
		acc+=value
	pc+=1

print(acc)


for change in range(len(data)):
	visited=set()
	pc,acc=0,0

	while pc not in visited and pc < len(data):
		visited.add(pc)
		instruction, value = data[pc]
		if pc == change:
			if instruction == 'jmp': instruction = 'nop'
			elif instruction == 'nop': instruction = 'jmp'
			else: break
		if instruction == 'jmp':
			pc+=value
			continue
		if instruction == 'acc':
			acc+=value
		pc+=1

	if pc == len(data): print(acc)

