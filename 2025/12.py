#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); heapq.heappush(a, 3)

# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# .venv/bin/pip3 install sortedcontainers astar z3-solver lmfit sympy shapely
# for lmfit:  sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran
# for shapely:  sudo apt install python3-dev pypy3-dev libgeos-dev
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #SortedList('bat') + 'cat'
# from astar import AStar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3.z3 import * # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()); if s.check()==z3.sat: print(int(str(s.model()[x]))) #Int is sometimes slow, but also sometimes Real doesn't give you what you want
# from sympy import * # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# import lmfit # try z3 or sympy first please
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area)
# from testtemplate import *



data1='''
'''.strip('\n').splitlines()
data2='''
'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores

s=[]
v=set()
# for line in data:
SHAPES=6
for index in range(SHAPES):
	data.pop(0)
	sh=[[ch for ch in data.pop(0)] for row in range(3)]
	s.append([(
		[0 if i!=index else 1 for i in range(SHAPES)],
		sh,
	)])
	t=tuple(tuple(s) for s in sh)
	v.add(t)

	data.pop(0)

for index in range(len(s)):
	sManifest,sh=s[index][0]
	sh=[[sh[j][2-i] for i in range(3)] for j in range(3)]
	t=tuple(tuple(s) for s in sh)
	if t in v: continue
	v.add(t)
	s[index].append((sManifest, sh))
for index in range(len(s)):
	for sManifest,sh in s[index].copy():
		for rotation in range(3):
			sh=[[sh[i][2-j] for i in range(3)] for j in range(3)]
			t=tuple(tuple(s) for s in sh)
			if t in v: continue
			v.add(t)
			s[index].append((sManifest, sh))

for index in range(len(s)):
	print(index)
	for sManifest,sh in s[index]:
		for row in sh:
			print(''.join(row))
		print()

def combine(aShape, bShape):
	global checkHeight,checkWidth,visited
	aManifest,a = aShape
	bManifest,b = bShape
	aHeight,aWidth = len(a),len(a[0])
	bHeight,bWidth = len(b),len(b[0])
	combinedManifest = [a+b for a,b in zip(aManifest,bManifest)]
	output = []
	for dy in range(-bHeight, aHeight+1):
		for dx in range(-bWidth, aWidth+1):
			if dx==0 and dy==0: continue
			aShiftY,aShiftX=-min(dy, 0),-min(dx, 0)
			bShiftY,bShiftX=dy-aShiftY,dx-aShiftX
			height,width=max(aShiftY+aHeight, bShiftY+bHeight),max(aShiftX+aWidth, bShiftX+bWidth)
			if height>checkHeight or width>checkWidth:
				continue

			good=True
			for y in range(aHeight):
				for x in range(aWidth):
					if a[y][x]=='.': continue
					y2,x2=y+dy,x+dx
					if y2<0 or y2>=bHeight or x2<0 or x2>=bWidth: continue
					if b[y2][x2]=='.': continue
					good=False
					break
				if not good: break
			if not good: continue

			newShape=[['.' for _ in range(width)] for _ in range(height)]
			for y in range(aHeight):
				for x in range(aWidth):
					if a[y][x]=='#':
						newShape[y+aShiftY][x+aShiftX]='#'
			for y in range(bHeight):
				for x in range(bWidth):
					if b[y][x]=='#':
						newShape[y+bShiftY][x+bShiftX]='#'
			t=(tuple(combinedManifest), (tuple(s) for s in newShape))
			if t in visited: continue
			visited.add(t)
			output.append((combinedManifest, newShape))
	return output

answer=0
for line in data:
	if line=='': continue
	line=[int(ch) for ch in re.findall('-?\d+', line)]
	checkWidth,checkHeight=line.pop(0),line.pop(0)

	# pool=[]
	# visited=set()
	# start=time.perf_counter()
	# for index,count in enumerate(line):
	# 	for c in range(count):
	# 		newPool=[]
	# 		for shape in s[index]:
	# 			if len(pool)==0:
	# 				newPool = [shape]
	# 			else:
	# 				for currentShape in pool:
	# 					newPool.extend(combine(currentShape, shape))
	# 			print('add', index, len(newPool), time.perf_counter()-start)
	# 		pool=newPool
	# 		print('### done adding shape ', index, len(pool), time.perf_counter()-start)
	# print('done', len(pool))

	space=0
	for index,count in enumerate(line):
		space+=sum(sum(count if ch=='#' else 0 for ch in row) for row in s[index][0][1])
	if space<=checkWidth*checkHeight:
		answer+=1
print(answer)

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

