#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]



#H=len(data)
#W=len(data[0])

W=2200
H=2200

N=10 #part one
N=10000

d=[[False for i in range(W)] for j in range(H)]

for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x]=='#':
			d[y+H//2-8][x+W//2-8]=True

#for line in data:
a=[(0,-1),(0,1),(-1,0),(1,0)]
for n in range(N):
	oneMoved=False
	t={}
	u={}
	for y in range(H):
		for x in range(W):
			if not d[y][x]:
				continue
			move=False
			for dy in range(-1,2):
				for dx in range(-1,2):
					if (dy!=0 or dx!=0) and d[y+dy][x+dx]:
						move=True
						break
			if not move:
				continue
			tx,ty=None,None
			for (dx,dy) in a:
				if d[y+dy][x+dx] or d[y+dy+dx][x+dx+dy] or d[y+dy-dx][x+dx-dy]:
					continue
				tr=(x+dx,y+dy)
				t[(x,y)]=tr
				u[tr]=u[tr]+1 if tr in u else 1
				break
	for (x,y),(tx,ty) in t.items():
		if(u[(tx,ty)]>1):
			continue
		d[ty][tx]=True
		d[y][x]=False
		oneMoved=True
	val=a[0]
	del a[0]
	a.append(val)
	#for r in d: print(''.join(['#' if c else ' ' for c in r]))
	if not oneMoved:
		break

minY,minX,maxY,maxX=None,None,None,None
count=0
for y in range(H):
	for x in range(W):
		if d[y][x]:
			count+=1
			if minX is None or x<minX:
				minX=x
			if maxX is None or x>maxX:
				maxX=x
			if minY is None or y<minY:
				minY=y
			if maxY is None or y>maxY:
				maxY=y

print(n+1, (maxY-minY+1)*(maxX-minX+1)-count)

