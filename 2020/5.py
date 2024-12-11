#!/usr/bin/python3


data='''
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
'''.replace('B','1').replace('F','0').replace('R','1').replace('L','0').strip().splitlines()

data='''
'''.replace('B','1').replace('F','0').replace('R','1').replace('L','0').strip().splitlines()

maximum=0
for line in data:
	value=int(line, 2)
	maximum = max(maximum, value)
print(maximum)


ids=[]
maximum=0
minimum=2**10
for line in data:
	value=int(line, 2)
	ids+=[value]
	minimum,maximum = min(minimum, value), max(maximum, value)

for id in range(minimum+1,maximum):
	if id not in ids:
		print(id)

