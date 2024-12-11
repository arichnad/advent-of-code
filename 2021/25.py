#!/usr/bin/python3


data1='''
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in line] for line in data]
data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

W,H=len(data[0]),len(data)
change=True
r=0
while change:
	change=False
	newData=[r[:] for r in data]
	for j in range(len(data)):
		for i in range(len(data[j])):
			c=data[j][i]
			if c=='>' and data[j][(i+1)%W]=='.':
				change=True
				newData[j][i]='.'
				newData[j][(i+1)%W]='>'
	data=newData
	newData=[r[:] for r in data]
	for j in range(len(data)):
		for i in range(len(data[j])):
			c=data[j][i]
			if c=='v' and data[(j+1)%H][i]=='.':
				change=True
				newData[j][i]='.'
				newData[(j+1)%H][i]='v'
	data=newData
	newData=[r[:] for r in data]
	r+=1


print('\n'.join([''.join(r) for r in data]))
print(r)

