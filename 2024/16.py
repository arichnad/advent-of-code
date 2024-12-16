#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, numpy # list(itertools.permutations(range(4), 4))
# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
# from astar import AStar #python3 -mpip install astar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
# import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
# from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
W,H=len(data[0]),len(data)
for j in range(H):
	for i in range(W):
		if data[j][i]=='S':
			start=(i, j)
		if data[j][i]=='E':
			end=(i, j)
v= {}
f={}

locs = [(0, start[0], start[1], 0, None, None, None)]
while len(locs)>0:
	newLocs= []
	for (cost, x, y, dir, fromX, fromY, fromDir) in sorted(locs):
		dir = (dir + 4) % 4
		if data[y][x] == '#': continue
		if (x, y, dir) in v and cost > v[(x, y, dir)]: continue
		if (x, y, dir) not in f or cost < v[(x, y, dir)]: f[(x, y, dir)] = []
		v[(x, y, dir)] = cost

		f[(x, y, dir)].append((fromX, fromY, fromDir))
		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]  # clockwise, starting right
		newLocs.append((cost + 1, x + dx, y + dy, dir, x, y, dir))
		newLocs.append((cost + 1000, x, y, dir + 1, x, y, dir))
		newLocs.append((cost + 1000, x, y, dir - 1, x, y, dir))
	locs=newLocs


minAnswer = min(v[(end[0], end[1], 0)], v[(end[0], end[1], 1)], v[(end[0], end[1], 2)], v[(end[0], end[1], 3)])
print(minAnswer)

v2=set()
answer=set()
def ff2(x, y, dir):
	global answer
	if (x, y, dir) in v2:
		return
	v2.add((x, y, dir))
	answer.add((x, y))
	for (fromX, fromY, fromDir) in f[(x, y, dir)]:
		if fromX is None: continue
		ff2(fromX, fromY, fromDir)
for d in range(4):
	if v[(end[0], end[1], d)] == minAnswer:
		ff2(end[0], end[1], d)
print(len(answer))
#dir = (dir+4)%4
#dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir = 1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = 'rdlu'.find(d.lower()) #clockwise, starting right
#dir = ['right', 'down', 'left', 'up'].index(d.lower()) #clockwise, starting right
#dir = '>v<^'.find(d.lower()) #clockwise, starting right

#data = [[column for column in line] for line in data]
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

