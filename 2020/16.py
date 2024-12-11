#!/usr/bin/python3


data='''
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
'''.strip().splitlines()
data='''
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''.strip().splitlines()

data='''
'''.strip().splitlines()



all = []
mode = None
answer=0
for line in data:
	if line == 'your ticket:':	
		mode='your'
		continue
	elif line == 'nearby tickets:':
		mode='nearby'
		continue
	elif line == '': continue

	if mode is None:
		type, ranges = line.split(': ')
		ranges = ranges.split(' or ')
		for r in ranges:
			all.append([int(value) for value in r.split('-')])
	elif mode == 'nearby':
		for ticket in line.split(','):
			ticket = int(ticket)
			for r in all:
				if r[0] <= ticket <= r[1]: break
			else:
				answer += ticket

print(answer)

all = []
keyedRanges = {}
outputTickets=[]
mode = None
for line in data:
	if line == 'your ticket:':	
		mode='your'
		continue
	elif line == 'nearby tickets:':
		mode='nearby'
		continue
	elif line == '': continue

	if mode is None:
		type, ranges = line.split(': ')
		ranges = ranges.split(' or ')
		keyedRanges[type] = []
		for r in ranges:
			all.append([int(value) for value in r.split('-')])
			keyedRanges[type].append([int(value) for value in r.split('-')])
	elif mode == 'nearby' or mode == 'your':
		for ticket in line.split(','):
			ticket = int(ticket)
			valid=True
			for r in all:
				if r[0] <= ticket <= r[1]: break
			else:
				break
		else:
			outputTickets.append([int(value) for value in line.split(',')])

N=20
#N=3
possible=[None for value in range(N)]

print(outputTickets)

for ticketRow in outputTickets:
	for index, ticket in enumerate(ticketRow):
		this = []
		for type, ranges in keyedRanges.items():
			valid=False
			for r in ranges:
				if r[0] <= ticket <= r[1]:
					valid=True
					break
			if valid:
				this.append(type)

		if possible[index] is None:
			possible[index] = this
		else:
			for possibleThing in possible[index][:]:
				if possibleThing not in this:
					print('removing', index, possibleThing)
					possible[index].remove(possibleThing)
			if len(possible[index])==1:
				for index2 in range(len(possible)):
					if index2 != index and possible[index][0] in possible[index2]:
						possible[index2].remove(possible[index][0])
			for type, ranges in keyedRanges.items():
				count=0
				for index2 in range(len(possible)):
					if type in possible[index2]:
						count+=1
				if count == 1:
					for index2 in range(len(possible)):
						if type in possible[index2]:
							possible[index2] = [type]

print(possible)
answer=1
for index, ticket in enumerate(outputTickets[0]):
	if possible[index][0].startswith('departure'):
		answer*=ticket
print(answer)

