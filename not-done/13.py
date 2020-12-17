#!/usr/bin/python3


data='''
1001798
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,859,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37
'''.strip().splitlines()
data='''
939
7,13,x,x,59,x,31,19
'''.strip().splitlines()


minimum=100000000
start=int(data[0])
for line in data[1].split(','):
	if line == 'x': continue
	id=int(line)
	time=id-(start%id)
	if time < minimum:
		minimum=time
		minimumId=id
#print(minimum*minimumId)

import math

def lcm(a, b):
	return a*b
	#return abs(a*b) // math.gcd(a, b)

def solve(a, z, b, c):
	total = 0
	while True:
		if (total - z + c) % b == 0:
			return total
		total += a

#def solve2(a, b, c, d, e):
#	total = 0
#	while True:
#		if (total + c) % b == 0 and (total + e) % d == 0:
#			return total
#		total += a


def solveLine(dataLine):
	lastMultiple = None
	#change lastOffset to firstOffset?
	lastOffset,lastId=None,None
	output = 0

	for offset, line in enumerate(dataLine.split(',')):
		if line == 'x': continue
		id=int(line)
		if lastOffset is not None:
			if lastMultiple is not None:
				output += solve(lastMultiple, 0, id, offset)
				lastMultiple=lcm(lastMultiple, id)
			else:
				output += solve(lastId, lastOffset, id, offset)
				lastMultiple = lcm(lastId, id)
		lastOffset=offset
		lastId=id

	return output

#3417 = 17 * 201 = 13 * 263 - 2 = 180 * 19 - 3
print(solve(17, 0, 13, 2) + solve(lcm(13, 17), 0, 19, 3) + lcm(13, 17))
print(3417, solveLine('17,x,13,19'))
print()

print(solve(67, 0, 7, 1) + solve(lcm(67, 7), 0, 59, 2) + lcm(67, 7) + solve(lcm(lcm(67, 7), 59), 0, 61, 3) + lcm(lcm(67, 7), 59))
print(754018, solveLine('67,7,59,61'))
print()

print(1068781, solveLine('7,13,x,x,59,x,31,19'))
print()

#print(solveLine('19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,859,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37'))

#print(solveLine('67,x,7,59,61'))
#print(solveLine('67,7,x,59,61'))

#solveLine(data[1])


