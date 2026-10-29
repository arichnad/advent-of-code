#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); itertools: product (like permutations with replacement.  repeat=N lets you use the same range multiple times), permutations, combinations, combinations_with_replacement. heapq.heappush(a, 3)
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

data0='''
'''.strip('\n').splitlines()
data1='''
'''.strip('\n').splitlines()
data2='''
'''.strip('\n').splitlines()

data=data2
# import fileinput # data=[a.strip('\n') for a in fileinput.input()]

# data = [int(line) for line in data]; H=len(data)
data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores
a={}
total={}
for line in data:
	id=line[0]
	q=int(line[1])
	p=int(line[2])
	t=int(line[3])
	if q not in a:
		a[q]={}
	if p not in a[q]:
		a[q][p]={}
	if id not in a[q][p]:
		a[q][p][id]=0
	a[q][p][id] += t
	if id not in total: total[id] = 0

timeChecker = lambda id: sum(a[q][thisPart][id] for thisPart in range(1, p+1))
print(a)

for q in range(1, 1000):
	if q not in a:
		break
	for p in range(1, 4):
		if p not in a[q]: continue
		ids = a[q][p].keys()
		ids = sorted(ids, key=timeChecker)
		current=50 * p
		shared=False
		idsIterator = enumerate(ids)
		for i, id in idsIterator:
			if current <= 0: break
			skip=0
			while i+1<len(ids) and timeChecker(ids[i+1]) == timeChecker(ids[i]):
				skip+=1
				print('SHARED', id, ids[i+1], timeChecker(ids[i]), timeChecker(ids[i+1]), current)
				total[ids[i]]+=current
				next(idsIterator, None)
				i+=1
			if skip>0:
				total[ids[i]] += current
				current-=skip+1
				continue
			print(id, timeChecker(id), current)
			total[id]+=current
			current-=1
output=0
current=1
ids = sorted(total.keys(), key=lambda x: -total[x])
idsIterator = enumerate(ids)
for i, x in idsIterator:
	print(x)
	skip=0
	while i+1<len(ids) and total[ids[i+1]] == total[ids[i]]:
		skip+=1
		output += current*total[ids[i]]
		next(idsIterator, None)
		i+=1
	if skip>0:
		output += current*total[ids[i]]
		current+=skip+1
		continue
	output += current* total[x]
	current+=1


print(output)
# a={}
# b={}
# for line in data:
# 	id=line[0]
# 	t=int(line[3])
# 	a[id] = a[id]+t if id in a else t
# 	b[id] = b[id]+1 if id in b else 1
# print(a, b)
# output=0
# for i, x in enumerate(sorted(a.keys(), key=lambda x: b[x]*-1000000 + a[x])):
# 	print(x)
# 	output += (i+1)* a[x]
# print(output)
# a={}
# for line in data:
# 	id=line[0]
# 	t=int(line[3])
# 	a[id] = a[id]+t if id in a else t
# print(a)
# output=0
# for i, b in enumerate(sorted(a, key=a.get)):
# 	output += (i+1)* a[b]
# print(output)

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


# bfs (priority queue)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, startY, startX)]
# costs={}
# while len(positions) > 0:
# 	(cost, y, x) = heapq.heappop(positions)
# 	if y<0 or y>=H or x<0 or x>=W: continue
# 	if data[y][x]=='#': continue
# 	if (y, x) in costs and cost >= costs[(y, x)]: continue
# 	costs[(y, x)] = cost
# 	
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			if (y+dy, x+dx) in costs and cost+1 >= costs[(y+dy, x+dx)]: continue
# 			heapq.heappush(positions, (cost+1, y+dy, x+dx))
# print(costs[(endY, endX)])

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

