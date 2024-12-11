#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
from collections import defaultdict, deque, Counter

data1='''
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data1; W=6+3
data=data2; W=21+3

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
data = [[int(column) for column in line.split(',')] for line in data]

tot=0
for a in data:
	vis=6
	for b in data:
		if a!=b and abs(b[0]-a[0]) + abs(b[1]-a[1]) + abs(b[2]-a[2]) == 1:
			vis-=1
	tot+=vis
print(tot)

d=[[[False for x in range(W)] for y in range(W)] for z in range(W)]
visited=set()
sys.setrecursionlimit(11000) #ewww.  also had to run this yikes:  ulimit -s 81920

for line in data:
	d[line[2]+1][line[1]+1][line[0]+1]=True

def rec(x, y, z):
	if x<0 or x==W or y<0 or y==W or z<0 or z==W: return 0
	if d[z][y][x]:
		return 1
	if (x, y, z) in visited: return 0
	visited.add((x, y, z))
	#print(x, y, z, len(visited))
	ans=0
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			for dz in [-1,0,1]:
				if (dx==0)+(dy==0)+(dz==0)!=2: continue
				ans+=rec(x+dx, y+dy, z+dz)
	return ans

print(rec(0,0,0)) #2482 2476 2486

