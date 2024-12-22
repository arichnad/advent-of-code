#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, numpy # list(itertools.permutations(range(4), 4))
# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
# from astar import AStar #python3 -mpip install astar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
# import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
# from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
1
2
3
2024
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()

# answer=0
# for line in data:
# 	for i in range(2000):
# 		line=(line*64) ^ line
# 		line=line % 16777216
# 		line=(line//32) ^ line
# 		line = line % 16777216
# 		line= (line*2048) ^ line
# 		line = line % 16777216
# 	answer+=line
# print(answer)

N=10
N=2000


answer={}
for line in data:
	d=[]
	skip=set()
	for i in range(N):
		previous = line
		line=(line*64) ^ line
		line=line % 16777216
		line=(line//32) ^ line
		line = line % 16777216
		line= (line*2048) ^ line
		line = line % 16777216

		difference = line%10 - previous%10
		d.append(difference)
		recent = d[-4:]
		# print(i, recent, line%10)
		if len(recent)==4:
			recent=tuple(recent)
			if recent not in skip:
				skip.add(recent)
				if recent not in answer: answer[recent]=0
				answer[recent]+=line%10

	# print(answer[(-2, 1, -1, 3)])
	# print(answer[(-2, 2, -1, -1)])
m,n=None,None
for k, v in answer.items():
	if m is None or v>m:
		m,n=v,k
print(m, n)

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

# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startX,startY=i,j
# 		if data[j][i]=='E': endX,endY=i,j
# positions = [(0, startX, startY)]
# costs={}
# while len(positions) > 0:
# 	newPositions = []
# 	for (cost, x, y) in sorted(positions): #remove sorted here if it's not needed
#		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x] == '#': continue
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue #change >= here to > if you need to analyze ties
# 		costs[(x, y)] = cost
#
# 		newPositions.append((cost + 1, x + 1, y))
# 		newPositions.append((cost + 1, x - 1, y))
# 		newPositions.append((cost + 1, x, y - 1))
# 		newPositions.append((cost + 1, x, y + 1))
# 	positions=newPositions
# print(costs[(endX, endY)])

# # flood fill does NOT work when want a breadth first (minimum cost, that sort of thing)
# visited=set()
# def ff(x, y):
# 	if y<0 or x<0 or y>=H or x>=W: return
# 	if data[y][x] == '#' or (x, y) in visited: return
# 	visited.add((x, y))
# 	ff(x + 1, y)
# 	ff(x - 1, y)
# 	ff(x, y + 1)
# 	ff(x, y - 1)
#
# ff(startX, startY)
