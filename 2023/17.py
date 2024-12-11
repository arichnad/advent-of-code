#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
'''.strip('\n').splitlines()
data1='''
111111111111
999999999991
999999999991
999999999991
999999999991
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
# data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
W,H=len(data[0]),len(data)
MAX=1000000
MAX_DISTANCE=10+1

out = [[[[MAX for distance in range(MAX_DISTANCE)] for dir in range(4)] for i in range(W)] for j in range(H)]
for dir in range(4):
	for distance in range(MAX_DISTANCE):
		out[-1][-1][dir][distance] = data[H-1][W-1]
for times in range(50):
	for j in reversed(range(H)):
		for i in reversed(range(W)):
			dx=0
			dyRest=0
			for dir in range(4):
				dx0, dy0 = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
				dataSoFar = sum(data[j+dy0*distance][i+dx0*distance] for distance in range(4) if not (i + dx0*distance >= W or j + dy0*distance >= H or i + dx0*distance < 0 or j + dy0*distance < 0))
				for distance in range(4,10+1):
					dx,dy= dx0 * distance, dy0 * distance
					if i + dx >= W or j + dy >= H or i + dx < 0 or j + dy < 0: continue
					out[j][i][dir][distance] = min(out[j][i][dir][distance], dataSoFar + min(
						out[j + dy][i + dx][dirRest][distanceRest] for distanceRest in range(MAX_DISTANCE) for dirRest in range(4) if abs(dirRest - dir)==1 or abs(dirRest - dir)==3))
					dataSoFar += data[j + dy][i + dx]


answer=MAX
for dir in range(4):
	for distance in range(MAX_DISTANCE):
		answer=min(answer, out[0][0][dir][distance])
print(answer-data[0][0])
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

# out = [[[[MAX for distance in range(3)] for dir in range(4)] for i in range(W)] for j in range(H)]
# for dir in range(4):
# 	for distance in range(3):
# 		out[-1][-1][dir][distance] = data[H-1][W-1]
# for times in range(50):
# 	for j in reversed(range(H)):
# 		for i in reversed(range(W)):
# 			dx=0
# 			dyRest=0
# 			for dir in range(4):
# 				dx0, dy0 = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
# 				dataSoFar = data[j][i]
# 				for distance in range(3):
# 					dx,dy=dx0*(distance+1),dy0*(distance+1)
# 					if i + dx >= W or j + dy >= H or i + dx < 0 or j + dy < 0: continue
# 					out[j][i][dir][distance] = min(out[j][i][dir][distance], dataSoFar + min(
# 						out[j + dy][i + dx][dirRest][distanceRest] for distanceRest in range(3) for dirRest in range(4) if abs(dirRest - dir)==1 or abs(dirRest - dir)==3))
# 					dataSoFar += data[j + dy][i + dx]
#
#
# answer=MAX
# for dir in range(4):
# 	for distance in range(3):
# 		answer=min(answer, out[0][0][dir][distance])
# print(answer-data[0][0])
