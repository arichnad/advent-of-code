#!/usr/bin/python3


data='''
939
7,13,x,x,59,x,31,19
'''.strip().splitlines()
data='''
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
print(minimum*minimumId)


def lcm(a, b):
	import math
	return abs(a*b) // math.gcd(a, b)

def solve(a, z, b, c):
	total = -z
	while True:
		if (total + c) % b == 0:
			return total
		total += a

def solve2(a, z, b, c):
	return solve(a, -z, b, -c)


def solveLine(dataLine):
	lastMultiple,lastSolve = None, None
	lastOffset,lastId=None,None

	for offset, line in enumerate(dataLine.split(',')):
		if line == 'x': continue
		id=int(line)
		if lastOffset is not None:
			if lastMultiple is not None:
				lastSolve = solve2(lastMultiple, lastSolve, lcm(lastId, id), solve(lastId,lastOffset, id, offset))
				lastMultiple=lcm(lastMultiple, id)
			else:
				lastSolve = solve(lastId, lastOffset, id, offset)
				lastMultiple = lcm(lastId, id)
		lastOffset=offset
		lastId=id

	return lastSolve

print(3417, solveLine('17,x,13,19'))
print(754018, solveLine('67,7,59,61'))
print(1068781, solveLine('7,13,x,x,59,x,31,19'))
print(solveLine('19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,859,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37'))

#solveLine(data[1])


