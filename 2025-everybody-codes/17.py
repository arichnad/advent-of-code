#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); heapq.heappush(a, 3)
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
'''.strip('\n').splitlines()
data2='''
'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() #does not run in parallel on separate cores

# answer=0
# for j, line in enumerate(data):
# 	for i, ch in enumerate(line):
# 		if (j-H//2)**2 + (i-W//2)**2 <= 10**2:
# 			if ch=='@': continue
# 			answer+=int(ch)
# print(answer)

# best,bestN=0,0
# for n in range(1, 1000):
# 	answer=0
# 	for j, line in enumerate(data):
# 		for i, ch in enumerate(line):
# 			r = (j-H//2)**2 + (i-W//2)**2
# 			if (n-1)**2 < r <= n**2:
# 				if ch=='@': continue
# 				answer+=int(ch)
# 	if answer>best:
# 		best,bestN=answer,n
# print(best*bestN)

for j in range(H):
	for i in range(W):
		if data[j][i]=='S': startX,startY=i,j
		if data[j][i]=='@': middleX,middleY=i,j
data[startY][startX]=0
for n in range(100):
	for j, line in enumerate(data):
		for i, ch in enumerate(line):
			if (j-middleY)**2 + (i-middleX)**2 <= (n+1)**2:
				data[j][i]='@'
	positions = [(0, 0, startX, startY, None, None, None)]
	costs={}
	while len(positions) > 0:
		# print(len(positions))
		newPositions = []
		for (cost, visits, x, y, fromX, fromY, fromVisits) in sorted(positions): #remove sorted here if it's not needed
			if y<0 or y>=H or x<0 or x>=W: continue
			if data[y][x] == '@': continue
			if (visits, x, y) in costs and cost >= costs[(visits, x, y)][0]: continue #change >= here to > if you need to analyze ties
			costs[(visits, x, y)] = (cost, fromX, fromY, fromVisits)

			fromVisits=visits
			if y>=middleY and x==middleX and fromX<middleX:
				visits=-1 if visits == 0 else 0
			elif y>=middleY and fromX==middleX and x>middleX:
				visits=-1 if visits == -1 else 0

			elif y>=middleY and x==middleX and fromX>middleX:
				visits=1 if visits == 0 else 0
			elif y>=middleY and fromX==middleX and x<middleX:
				visits=1 if visits == 1 else 0
			fromX,fromY=x,y
			newCost=cost+int(data[y][x])
			for (x, y) in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
				newPositions.append((newCost, visits, x, y, fromX, fromY, fromVisits))
		positions=newPositions
	totalCost = None
	if (1, startX, startY) in costs:
		totalCost = costs[(1, startX, startY)][0]
	if (-1, startX, startY) in costs:
		totalCost = costs[(-1, startX, startY)][0]
	print(n+1, totalCost, 30*(n+2))
	if totalCost < 30*(n+2):
		print(totalCost, n+1 ,totalCost * (n+1))

		# mark=[[False for j in range(H)] for i in range(W)]
		# visits,y,x=-1,startY,startX
		# while y != None:
		# 	mark[y][x]=True
		# 	_,x,y,visits=costs[(visits, x, y)]
		# for j in range(H):
		# 	for i in range(W):
		# 		print(data[j][i] if data[j][i]=='@' or mark[j][i] else ' ', end='')
		# 	print()
		break


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

# bfs
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startX,startY=i,j
# 		if data[j][i]=='E': endX,endY=i,j
# positions = [(0, startX, startY)]
# costs={}
# while len(positions) > 0:
# 	newPositions = []
# 	for (cost, x, y) in sorted(positions): #remove sorted here if it's not needed
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x] == '#': continue
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue #change >= here to > if you need to analyze ties
# 		costs[(x, y)] = cost
#
# 		for (cost, x, y) in ((cost + 1, x + 1, y), (cost + 1, x - 1, y), (cost + 1, x, y - 1), (cost + 1, x, y + 1)):
# 			newPositions.append((cost, x, y))
# 	positions=newPositions
# print(costs[(endX, endY)])


# dijkstra's
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startX,startY=i,j
# 		if data[j][i]=='E': endX,endY=i,j
# positions = [(0, startX, startY)]
# costs={}
# while len(positions) > 0:
# 	(cost, x, y) = heapq.heappop(positions)
# 	if y<0 or y>=H or x<0 or x>=W: continue
# 	if data[y][x]=='#': continue
# 	if (x, y) in costs and cost >= costs[(x, y)]: continue
# 	costs[(x, y)] = cost
#
# 	for (cost, x, y) in ((cost + 1, x + 1, y), (cost + 1, x - 1, y), (cost + 1, x, y - 1), (cost + 1, x, y + 1)):
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue
# 		heapq.heappush(positions, (cost, x, y))
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
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startX,startY=i,j
# 		if data[j][i]=='E': endX,endY=i,j
# ff(startX, startY)
