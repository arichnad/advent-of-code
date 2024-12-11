#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
W,H=len(data[0]),len(data)

maxX,maxY,maxZ=0,0,0

for (x0,y0,z0,x1,y1,z1) in data:
	maxX=max(x0,x1,maxX)
	maxY = max(y0, y1, maxY)
	maxZ = max(z0, z1, maxZ)

maxX+=1
maxY+=1
maxZ+=1

m=[[[-1 for x in range(maxX)] for y in range(maxY)] for z in range(maxZ)]
n=[[] for n in range(len(data))]

for pos, (x0, y0, z0, x1, y1, z1) in enumerate(data):
	for x in range(x0, x1+1):
		for y in range(y0, y1 + 1):
			for z in range(z0, z1 + 1):
				m[z][y][x]=pos
				n[pos].append((x, y, z))


change=True
while change:
	change=False
	for pos in range(len(data)):
		for (x,y,z) in n[pos]:
			if z==1 or m[z-1][y][x]!=-1 and m[z-1][y][x]!=pos: break
		else:
			change=True
			for (x, y, z) in n[pos]:
				m[z][y][x] = -1
			for (x, y, z) in n[pos]:
				m[z-1][y][x] = pos
			for p in range(len(n[pos])):
				n[pos][p] = (n[pos][p][0], n[pos][p][1], n[pos][p][2]-1)

answer=0
for remove in range(len(data)):
	removed={remove}
	changes=True
	while changes:
		changes=False
		for heldUp in range(len(data)):
			if heldUp in removed: continue
			for (x, y, z) in n[heldUp]:
				if z==1 or m[z-1][y][x]!=-1 and m[z-1][y][x]!=heldUp and m[z-1][y][x] not in removed: break
			else:
				removed.add(heldUp)
				changes=True
				answer+=1
print(answer)

#dir=(dir+4)%4
#dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = "rdlu".find(ch.lower())

#data = [[column for column in line] for line in data]
#W,H=len(data[0]), len(data)
#for j in range(H):
#	for i in range(W):
#		for dy in range(-1, 2):
#			for dx in range(-1, 2):
#				#if dx==0 and dy==0: continue
#				if dx==0 and dy==0 or dx!=0 and dy!=0: continue
#
#				newY,newX=j+dy,i+dx
#				if newY<0 or newX<0 or newY>=H or newX>=W: continue
#
#for line in data: print(''.join(line))

# answer=0
# for remove in range(len(data)):
# 	for heldUp in range(len(data)):
# 		if remove==heldUp: continue
# 		for (x, y, z) in n[heldUp]:
# 			if z==1 or m[z-1][y][x]!=-1 and m[z-1][y][x]!=heldUp and m[z-1][y][x]!=remove: break
# 		else:
# 			break
# 	else:
# 		answer+=1
# print(answer)
