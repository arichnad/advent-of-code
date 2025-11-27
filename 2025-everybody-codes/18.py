#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); heapq.heappush(a, 3)
# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
# from astar import AStar #python3 -mpip install astar #see astarExample.py
# from collections import defaultdict, deque, Counter
from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
# import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
# from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
'''.strip('\n').splitlines()
data1TestCases='''
'''.strip('\n').splitlines()
data2='''
'''.strip('\n').splitlines()
data2TestCases='''
'''.strip('\n').splitlines()
# data=data1;dataTestCases=data1TestCases
data=data2;dataTestCases=data2TestCases

# data = [int(line) for line in data]; H=len(data)
data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
dataTestCases = [[int(column) for column in re.findall('-?\d+', line)] for line in dataTestCases]
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() #does not run in parallel on separate cores

# currentPlant=0
# plants=[]
# first=True
# for line in data:
# 	if len(line)==0:
# 		if currentPlant<thickness: currentPlant=0
#		plants.append(currentPlant)
# 		first=True
# 		currentPlant=0
# 		continue
# 	if first:
# 		first=False
# 		thickness=line[1]
# 	else:
# 		if len(line)==1:
# 			currentPlant += line[0]
# 		else:
# 			currentPlant+=line[1]*plants[line[0]-1]
# if currentPlant<thickness: currentPlant=0
# plants.append(currentPlant)
# print(plants)

# answer=0
# for testCase in dataTestCases:
# 	currentPlant=0
# 	freeBranchCount=0
# 	plants=[]
# 	first=True
# 	for line in data:
# 		if len(line)==0:
# 			if currentPlant<thickness: currentPlant=0
# 			plants.append(currentPlant)
# 			first=True
# 			currentPlant=0
# 			continue
# 		if first:
# 			first=False
# 			thickness=line[1]
# 		else:
# 			if len(line)==1:
# 				currentPlant += line[0]*testCase[freeBranchCount]
# 				freeBranchCount += 1
# 			else:
# 				currentPlant+=line[1]*plants[line[0]-1]
# 	if currentPlant<thickness: currentPlant=0
# 	plants.append(currentPlant)
# 	answer+=plants[-1]
# print(answer)


def _(plants, testCase):
	plantAnswer=[]
	for (plant, plantFree, thickness) in plants:
		answer=0
		for (freeBranch, freeThickness) in plantFree:
			answer+=freeThickness*testCase[freeBranch]
		for (plantIndex, plantThickness) in plant:
			answer+=plantThickness*plantAnswer[plantIndex]
		plantAnswer.append(0 if answer<thickness else answer)
	return plantAnswer[-1]

currentPlant,currentPlantFree=[],[]
freeBranchCount=0
plants=[]
first=True
thickness=None
for line in data:
	if len(line)==0:
		plants.append((currentPlant, currentPlantFree, thickness))
		first=True
		currentPlant,currentPlantFree=[],[]
		continue
	if first:
		first=False
		thickness=line[1]
	else:
		if len(line)==1:
			currentPlantFree.append((freeBranchCount, line[0]))
			freeBranchCount += 1
		else:
			index=line[0]-1
			currentPlant.append((index, line[1]))

plants.append((currentPlant, currentPlantFree, thickness))
print(plants)

pool=[]
for j in range(10000):
	entry=[random.getrandbits(1) for i in range(freeBranchCount)]
	pool.append((_(plants, entry), entry))

for iterations in range(200):
	pool=sorted(pool, key=lambda x: x[0], reverse=True)[0:1000]
	lastPool=pool
	for i in range(len(pool)):
		for copy in range(1):
			entry=pool[i][1]
			newEntry=entry[:]
			for change in range(3):
				index=random.randrange(0, len(newEntry))
				newEntry[index]=1-newEntry[index]
			pool.append((_(plants, newEntry), newEntry))
print(lastPool[0][0])
bestResult=lastPool[0][0]
answer=0
for testCase in dataTestCases:
	if _(plants, testCase) > 0:
		answer+=bestResult-_(plants, testCase)
print(answer)
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
