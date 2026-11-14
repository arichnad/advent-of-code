#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); itertools: product (like permutations with replacement.  repeat=N lets you use the same range multiple times), permutations, combinations, combinations_with_replacement. heapq.heappush(a, 3); d=copy.deepcopy(d)
# sort list in python3 with a comparator:  v.sort(key=functools.cmp_to_key(lambda a, b: -1 if (a, b) in g else 1 if (b, a) in g else 0))

# you CANNOT copy venv directories.  use this instead:  sudo apt install pypy3-venv && pypy3 -m venv .venv
# OR:  settings -> python -> interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# sudo apt install python3-dev pypy3-dev pypy3-venv libopenblas-dev gfortran libgeos-dev && .venv/bin/pip install sortedcontainers astar z3-solver lmfit sympy shapely
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #SortedList('bat') + 'cat'
# from astar import AStar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3.z3 import * # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); MAYBE s.minimize(sum(params)); print(s.check()); if s.check()==z3.sat: print(int(str(s.model()[x]))) #Int is sometimes slow, but also sometimes Real doesn't give you what you want
# from sympy import * # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# import lmfit # try z3 or sympy first please
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area)
# from testtemplate import *
  	
data1='''

'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()
data3='''

'''.strip('\n').splitlines()

data=data2
# import fileinput # data=[a.strip('\n') for a in fileinput.input()]

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores

s=set()
# bfs (priority queue)
corners=set()
for j in range(H):
	for i in range(W):
		if data[j][i]=='S': startY,startX=j,i
		if data[j][i]=='E': endY,endX=j,i
		if data[j][i] == '@': s.add((j, i))
		if 1<=j<H-1 and 1<=i<W-1:
			if data[j][i]=='#': continue
			walls = (data[j - 1][i] == '#') + (data[j + 1][i] == '#') + (data[j][i - 1] == '#') + (data[j][i + 1] == '#')
			if walls <= 1: corners.add((j, i))
corners.add((startY, startX))
corners.add((endY, endX))
cornerCosts={}
def _(j, i, visited, cornerStart, lowestPoint, cost, sulfur):
	if not (0 <= j < H and 0 <= i < W) or data[j][i]=='#': return

	if (j, i) in corners and (j, i) != cornerStart:
		if cornerStart not in cornerCosts: cornerCosts[cornerStart] = []
		# lowestPoint.append((j, i))
		cornerCosts[cornerStart].append(((j, i), cost, sulfur, lowestPoint))
		return

	if (j, i) in visited: return
	visited.add((j, i))

	if (j, i) != cornerStart:
		if lowestPoint is None:
			lowestPoint = (j, i)
		else:
			lowestPoint = min(lowestPoint, (j, i))
	# lowestPoint.append((j, i))

	cost+=1
	if data[j][i]=='@':
		sulfur=set(sulfur)
		sulfur.add((j, i))
	_(j+1, i, visited, cornerStart, lowestPoint, cost, sulfur)
	_(j-1, i, visited, cornerStart, lowestPoint, cost, sulfur)
	_(j, i-1, visited, cornerStart, lowestPoint, cost, sulfur)
	_(j, i+1, visited, cornerStart, lowestPoint, cost, sulfur)

corners=list(corners)
for k in range(len(corners)):
	(j, i)=corners[k]
	_(j, i, set(), corners[k], None, 0, set())

from fractions import Fraction
pool=[]
for corner in corners:
	pool.append((0, corner, 0, None, corner, None))
best=0
for length in range(8):
	newPool=[]
	for (cost, corner, sulfur, lastEdge, firstCorner, firstEdge) in pool:
		for (newCorner, costAdd, sulfurAdd, lowestPoint) in cornerCosts[corner]:
			newEdge = lowestPoint
			if newEdge == lastEdge: continue
			newSulfur = sulfur + len(sulfurAdd)
			newCost = cost + costAdd
			newFirstEdge = firstEdge if firstEdge is not None else newEdge
			if newCorner == firstCorner:
				ratio = Fraction(newSulfur, newCost)
				if ratio >= best:
					if ratio > best:
						bestDetails=[]
					best=ratio
					bestDetails.append((newSulfur, newCost, firstCorner, firstEdge, newEdge))
				continue
			newPool.append((newCost, newCorner, newSulfur, newEdge, firstCorner, newFirstEdge))
	pool=newPool

bestStarts=set()
for b in bestDetails:
	bestStarts.add(b[2])

positions = [(0, (startY, startX), 0, None, (0, 0))]
costs={}
previousCost=0
endCorner = (endY, endX)
answer=math.inf
while len(positions) > 0:
	(cost, corner, sulfur, lastEdge, madeBest) = heapq.heappop(positions)
	if cost>previousCost:
		previousCost=cost
	costsKey = (corner, sulfur, madeBest)
	if costsKey in costs and cost >= costs[costsKey]: continue
	costs[costsKey] = cost
	for (newCorner, costAdd, sulfurAdd, lowestPoint) in cornerCosts[corner]:
		newEdge = lowestPoint
		if lastEdge is not None and newEdge == lastEdge: continue
		newSulfur=sulfur + len(sulfurAdd)
		newCost=cost+costAdd

		if madeBest == (0, 0) and newCorner in bestStarts:
			for (_newSulfur, _newCost, _firstCorner, _firstEdge, _newEdge) in bestDetails:
				if _firstCorner == newCorner and newEdge != _firstEdge:

					heapq.heappush(positions, (newCost, newCorner, newSulfur, newEdge, (_newSulfur, _newCost)))

		if newCorner == endCorner and madeBest!=(0, 0):
			(_newSulfur, _newCost) = madeBest
			rounds = (202620262026 - newSulfur + _newSulfur - 1) // _newSulfur
			newCost += rounds * _newCost
			newSulfur += rounds * _newSulfur

			if newCost < answer and newSulfur == 202620262026:
				print(newCost, newCorner, (_newSulfur, _newCost), newSulfur)
				answer = newCost
			continue
		# if newCorner == endCorner and newSulfur >= 2026 and madeBest==(0, 0):
		# 	print(newCost, newCorner, newSulfur)
		# 	sys.exit(0)
		heapq.heappush(positions, (newCost, newCorner, newSulfur, newEdge, madeBest))

# s=set()
# # bfs (priority queue)
# corners=set()
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# 		if data[j][i] == '@': s.add((j, i))
# 		if 1<=j<H-1 and 1<=i<W-1:
# 			if data[j][i]=='#': continue
# 			walls = (data[j - 1][i] == '#') + (data[j + 1][i] == '#') + (data[j][i - 1] == '#') + (data[j][i + 1] == '#')
# 			if walls <= 1: corners.add((j, i))
# corners.add((startY, startX))
# corners.add((endY, endX))
#
# cornerCosts={}
# def _(j, i, visited, cornerStart, cost, sulfur):
# 	if not (0 <= j < H and 0 <= i < W) or data[j][i]=='#': return
#
# 	if (j, i) in corners and (j, i) != cornerStart:
# 		if cornerStart not in cornerCosts: cornerCosts[cornerStart] = []
# 		cornerCosts[cornerStart].append(((j, i), cost, sulfur))
# 		return
#
# 	if (j, i) in visited: return
# 	visited.add((j, i))
#
# 	cost+=1
# 	if data[j][i]=='@':
# 		sulfur=set(sulfur)
# 		sulfur.add((j, i))
# 	_(j+1, i, visited, cornerStart, cost, sulfur)
# 	_(j-1, i, visited, cornerStart, cost, sulfur)
# 	_(j, i-1, visited, cornerStart, cost, sulfur)
# 	_(j, i+1, visited, cornerStart, cost, sulfur)
#
# corners=list(corners)
# for k in range(len(corners)):
# 	(j, i)=corners[k]
# 	_(j, i, set(), corners[k], 0, set())
#
# positions = [(0, (startY, startX), 0, None)]
# costs={}
# previousCost=0
# endCorner = (endY, endX)
# while len(positions) > 0:
# 	(cost, corner, sulfur, lastEdge) = heapq.heappop(positions)
# 	if cost>previousCost:
# 		previousCost=cost
# 		print(cost, sulfur, len(positions))
# 	if (corner, sulfur) in costs and cost >= costs[(corner, sulfur)]: continue
# 	costs[(corner, sulfur)] = cost
# 	for (newCorner, costAdd, sulfurAdd) in cornerCosts[corner]:
# 		newEdge = (sorted([corner, newCorner]), sulfurAdd, costAdd)
# 		if newEdge == lastEdge: continue
# 		newSulfur=sulfur + len(sulfurAdd)
# 		newCost=cost+costAdd
# 		costsKey = (newCorner, newSulfur)
# 		if costsKey in costs and newCost >= costs[costsKey]: continue
# 		if newCorner == endCorner and newSulfur>=2026:
# 			print(newCost, newCorner, newSulfur)
# 			sys.exit(0)
# 		heapq.heappush(positions, (newCost, newCorner, newSulfur, newEdge))


# s=set()
# # bfs (priority queue)
# corners=set()
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# 		if data[j][i] == '@': s.add((j, i))
# 		if 1<=j<H-1 and 1<=i<W-1:
# 			if data[j][i]=='#': continue
# 			walls = (data[j - 1][i] == '#') + (data[j + 1][i] == '#') + (data[j][i - 1] == '#') + (data[j][i + 1] == '#')
# 			if walls <= 1: corners.add((j, i))
# corners.add((startY, startX))
# corners.add((endY, endX))
#
# cornerCosts={}
# def _(j, i, visited, cornerStart, lowestPoint, cost, sulfur):
# 	if not (0 <= j < H and 0 <= i < W) or data[j][i]=='#': return
#
# 	if (j, i) in corners and (j, i) != cornerStart:
# 		if cornerStart not in cornerCosts: cornerCosts[cornerStart] = []
# 		cornerCosts[cornerStart].append(((j, i), cost, sulfur, lowestPoint))
# 		return
#
# 	if (j, i) in visited: return
# 	visited.add((j, i))
#
# 	if (j, i) != cornerStart:
# 		if lowestPoint is None:
# 			lowestPoint = (j, i)
# 		else:
# 			lowestPoint = min(lowestPoint, (j, i))
#
# 	cost+=1
# 	if data[j][i]=='@':
# 		sulfur=set(sulfur)
# 		sulfur.add((j, i))
# 	_(j+1, i, visited, cornerStart, lowestPoint, cost, sulfur)
# 	_(j-1, i, visited, cornerStart, lowestPoint, cost, sulfur)
# 	_(j, i-1, visited, cornerStart, lowestPoint, cost, sulfur)
# 	_(j, i+1, visited, cornerStart, lowestPoint, cost, sulfur)
#
# corners=list(corners)
# for k in range(len(corners)):
# 	(j, i)=corners[k]
# 	_(j, i, set(), corners[k], None, 0, set())
#
# positions = [(0, (startY, startX), (), None)]
# costs={}
# previousCost=0
# endState = ((endY, endX), tuple(sorted(s)))
# while len(positions) > 0:
# 	(cost, corner, sulfur, lastEdge) = heapq.heappop(positions)
# 	if cost>previousCost:
# 		previousCost=cost
# 		print(cost, len(sulfur), len(positions))
# 	if (corner, sulfur) in costs and cost >= costs[(corner, sulfur)]: continue
# 	costs[(corner, sulfur)] = cost
# 	for (newCorner, costAdd, sulfurAdd, lowestPoint) in cornerCosts[corner]:
# 		newLastEdge = lowestPoint
# 		if lastEdge is not None and newLastEdge == lastEdge: continue
# 		newSulfur=set(sulfur)
# 		newSulfur |= sulfurAdd
# 		newSulfur=tuple(sorted(newSulfur))
# 		newCost=cost+costAdd
# 		costsKey = (newCorner, newSulfur)
# 		if costsKey in costs and newCost >= costs[costsKey]: continue
# 		if costsKey == endState:
# 			print(newCost, newCorner, len(newSulfur))
# 			sys.exit(0)
# 		heapq.heappush(positions, (newCost, newCorner, newSulfur, newLastEdge))
# print(costs[endState])


# dir = (dir+4)%4
# dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] # clockwise, starting right
# dir = 1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 # clockwise, starting right
# dir = 'rdlu'.find(d.lower()) # clockwise, starting right
# dir = ['right', 'down', 'left', 'up'].index(d.lower()) # clockwise, starting right
# dir = '>v<^'.find(d.lower()) # clockwise, starting right

# data = [[column for column in line] for line in data]
# for j in range(H):
# 	for i in range(W):
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				# if dx==0 and dy==0: continue
# 				if abs(dx)+abs(dy)!=1: continue
#
# 				newY,newX=j+dy,i+dx
# 				if newY<0 or newX<0 or newY>=H or newX>=W: continue
#
# for line in data: print(''.join(line))

# bfs simple queue
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, startY, startX)]
# costs={}
# while len(positions) > 0:
# 	# print(len(positions))
# 	newPositions = []
# 	for (cost, y, x) in sorted(positions): # remove sorted here if it's not needed
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x] == '#': continue
# 		if y==endY and x==endX:
# 			print(cost)
# 			newPositions=[]
# 			break
# 		if (y, x) in costs and cost >= costs[(y, x)]: continue # change >= here to > if you need to analyze ties
# 		costs[(y, x)] = cost
#
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				# if dx==0 and dy==0: continue
# 				if abs(dx)+abs(dy)!=1: continue
# 				newPositions.append((cost + 1, y+dy, x+dx))
# 	positions=newPositions




#
# import math
# s=set()
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# 		if data[j][i]=='@': s.add((j, i))
# s=tuple(s)
# print(s)
#
#
# from astar import AStar # see installation in template.py
#
# from testtemplate import *
#
# class AStarSolver(AStar):
# 	def heuristic_cost_estimate(self, current, goal):
# 		(x1, y1, sulfur) = current
# 		(x2, y2, sulfurGoal) = goal
#
# 		res=math.hypot(x2 - x1, y2 - y1) + \
# 				(len(sulfurGoal)-len(sulfur))*100000
# 		return res
#
# 	# only gets called on connecting neighbors
# 	def distance_between(self, n1, n2): return .1
#
# 	def neighbors(self, node):
# 		(x, y, sulfur) = node
# 		output=[]
# 		for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
# 			if 0 <= nx < W and 0 <= ny < H and data[ny][nx] != '#':
# 				if data[ny][nx] != '.': print(data[ny][nx])
# 				newSulfur = sulfur
# 				if data[ny][nx]=='@':
# 					newSulfur=set(sulfur)
# 					newSulfur.add((ny, nx))
# 					newSulfur=tuple(newSulfur)
# 					# newSulfur.add((ny, nx))
# 				output.append((nx, ny, newSulfur))
# 		return output
#
# result=AStarSolver().astar((startX,startY, (), ), (endX, endY, ((1, 2),)))
# result=list(result)
# print(len(result))
# # error about NoneType is not iterable, means astar couldn't find a path



# flood fill does NOT work when want a breadth first (minimum cost, that sort of thing)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# visited=set()
# def ff(y, x):
# 	if y<0 or x<0 or y>=H or x>=W: return 0
# 	if data[y][x] == '#' or (y, x) in visited: return 0
# 	visited.add((y, x))
# 
# 	answer=1
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			answer+=ff(y+dy, x+dx)
# 	return answer
# 
# print(ff(startY, startX))

