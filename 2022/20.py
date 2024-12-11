#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
from collections import defaultdict, deque, Counter

data1='''
1
2
-3
3
-2
0
4
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#data=[(i,int(d)) for i,d in enumerate(data)]
#for originalPos in range(len(data)):
#	for i, (originalPos2,d) in enumerate(data):
#		if originalPos!=originalPos2:
#			continue
#		del data[i]
#		data.insert((i+d)%len(data), (originalPos2,d))
#		break
#
#for i in range(len(data)):
#	if data[i][1]==0:
#		pos=i
#print(data[(pos+1000)%len(data)][1]+ data[(pos+2000)%len(data)][1]+ data[(pos+3000)%len(data)][1])

data=[(i,int(d)*811589153) for i,d in enumerate(data)]
print(data)
for n in range(10):
	for originalPos in range(len(data)):
		for i, (originalPos2,d) in enumerate(data):
			if originalPos!=originalPos2:
				continue
			del data[i]
			data.insert((i+d)%len(data), (originalPos2,d))
			break
print(data)

for i in range(len(data)):
	if data[i][1]==0:
		pos=i
print(data[(pos+1000)%len(data)][1]+ data[(pos+2000)%len(data)][1]+ data[(pos+3000)%len(data)][1])

