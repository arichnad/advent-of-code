#!/usr/bin/python3


data='''
0,3,6
'''.strip().splitlines()
data='''
6,19,0,5,7,13,1
'''.strip().splitlines()


last=int(data[0].split(',')[-1])
data={int(line):id for id,line in enumerate(data[0].split(','))}
del data[last]


id=len(data)

number=0

while id < 30000000-1:
	if last in data:
		number=id-data[last]
	else:
		number=0
	data[last]=id
	id+=1
	last=number
print(number)


