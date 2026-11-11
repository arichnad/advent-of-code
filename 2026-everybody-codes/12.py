#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); itertools: product (like permutations with replacement.  repeat=N lets you use the same range multiple times), permutations, combinations, combinations_with_replacement. heapq.heappush(a, 3); d=copy.deepcopy(d)
from multiprocessing.connection import answer_challenge

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

data=data3
# import fileinput # data=[a.strip('\n') for a in fileinput.input()]

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores


def _(j, i, v, xs, yz, change):
	if i >= W or i < 0 or j >= H or j < 0 or data[j][i] != '#' or (j, i) in v:
		return
	xs.add(i)
	ys.add(j)
	v.add((j, i))
	if change:
		data[j][i]='.'
	_(j + 1, i, v, xs, ys, change)
	_(j - 1, i, v, xs, ys, change)
	_(j, i - 1, v, xs, ys, change)
	_(j, i + 1, v, xs, ys, change)

total = 0
for j in range(H):
	for i in range(W):
		if data[j][i] != '#': continue
		v=set()
		xs=set()
		ys=set()
		_(j, i, v, xs, ys, False)
		x0,x1 = min(xs),max(xs)
		y0,y1 = min(ys),max(ys)
		c=None
		dir=None
		if (y1, x1) not in v:
			c = (y0, x0)
			dir=(1, 1)
		if (y0, x1) not in v:
			c = (y1, x0)
			dir=(-1, 1)
		if (y1, x0) not in v:
			c = (y0, x1)
			dir=(1, -1)
		if (y0, x0) not in v:
			c = (y1, x1)
			dir=(-1, -1)
		if c is None:
			if (y1-y0+1)*(x1-x0+1) == len(v):
				c = (y0, x0)
				dir=(1, 1)
			else:
				w=y1-y0+1
				h=x1-x0+1
				x2,y2,x3,y3=None,None,None,None
				for y in range(y0, y1+1):
					for x in range(x0, x1+1):
						if (y, x) not in v:
							if x2 is None or x < x2: x2 = x
							if x3 is None or x > x3: x3 = x
							if y2 is None or y < y2: y2 = y
							if y3 is None or y > y3: y3 = y
				x1+=1
				y1+=1
				x3+=1
				y3+=1
				xv=[x0, x2, x3, x1]
				yv=[y0, y2, y3, y1]
				best=math.inf
				for z in range(512):
					current=0
					a=0
					rotation=[[None for i in range(3)] for j in range(3)]
					for yI in range(3):
						for xI in range(3):
							x = (xv[xI], xv[xI + 1])
							y = (yv[yI], yv[yI + 1])
							curRotation = 1 if z & (1 << a) != 0 else 0
							rotation[yI][xI] = curRotation
							if yI == 1 and xI == 1:
								rotation[yI][xI] = None
							else:
								rotationLeft=rotation[yI][xI-1] if xI>0 else None
								rotationAbove=rotation[yI-1][xI] if yI>0 else None
								if not ((curRotation==0 and rotationLeft==curRotation) or (curRotation==1 and rotationAbove==curRotation)):
									# print(yI, xI, curRotation, rotationAbove, rotationLeft, y[1]-y[0], x[1]-x[0])
									current+=(x[1]-x[0]) if curRotation == 1 else (y[1]-y[0])
							a+=1
					# print(z, current)
					if current<best: best=current
				print(j, i, best)
				total += best
				_(j, i, set(), set(), set(), True)
				# sys.exit(0)
				continue

		firstDist, secondDist = None, None
		firstDistCount, secondDistCount = 0, 0
		for k in range(H):
			chY, chX = c[0] + k * dir[0], c[1]
			if chY < 0 or chY >= H or chX < 0 or chX >= W or data[chY][chX] != '#':
				break

			dist = 0
			for l in range(W):
				chY, chX = c[0] + k * dir[0], c[1] + l * dir[1]
				if chY < 0 or chY >= H or chX < 0 or chX >= W or data[chY][chX] != '#':
					break
				dist = l + 1

			if firstDist is None or dist == firstDist:
				firstDist = dist
				firstDistCount += 1
			else:
				secondDist = dist
				secondDistCount += 1
		answer0 = min(firstDist, firstDistCount) + (min(secondDist, secondDistCount) if secondDist is not None else 0)

		firstDist, secondDist = None, None
		firstDistCount, secondDistCount = 0, 0
		for l in range(W):
			chY, chX = c[0], c[1] + l * dir[1]
			if chY < 0 or chY >= H or chX < 0 or chX >= W or data[chY][chX] != '#':
				break

			dist = 0
			for k in range(H):
				chY, chX = c[0] + k * dir[0], c[1] + l * dir[1]
				if chY < 0 or chY >= H or chX < 0 or chX >= W or data[chY][chX] != '#':
					break
				dist = l + 1

			if firstDist is None or dist == firstDist:
				firstDist = dist
				firstDistCount += 1
			else:
				secondDist = dist
				secondDistCount += 1
		answer1 = min(firstDist, firstDistCount) + (min(secondDist, secondDistCount) if secondDist is not None else 0)

		total += min(answer0, answer1)

		_(j, i, set(), set(), set(), True)

print(total)

# def _(j, i, v, xs, yz, change):
# 	if i >= W or i < 0 or j >= H or j < 0 or data[j][i] != '#' or (j, i) in v:
# 		return
# 	xs.add(i)
# 	ys.add(j)
# 	v.add((j, i))
# 	if change:
# 		data[j][i]='.'
# 	_(j + 1, i, v, xs, ys, change)
# 	_(j - 1, i, v, xs, ys, change)
# 	_(j, i - 1, v, xs, ys, change)
# 	_(j, i + 1, v, xs, ys, change)
#
# total = 0
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i] != '#': continue
# 		v=set()
# 		xs=set()
# 		ys=set()
# 		_(j, i, v, xs, ys, False)
# 		x0,x1 = min(xs),max(xs)
# 		y0,y1 = min(ys),max(ys)
# 		c=None
# 		dir=None
# 		if (y1, x1) not in v:
# 			c = (y0, x0)
# 			dir=(1, 1)
# 		if (y0, x1) not in v:
# 			c = (y1, x0)
# 			dir=(-1, 1)
# 		if (y1, x0) not in v:
# 			c = (y0, x1)
# 			dir=(1, -1)
# 		if (y0, x0) not in v:
# 			c = (y1, x1)
# 			dir=(-1, -1)
# 		if c is None:
# 			c = (y0, x0)
# 			dir=(1, 1)
#
# 		firstDist, secondDist = None, None
# 		firstDistCount, secondDistCount = 0, 0
# 		for k in range(H):
# 			chY, chX = c[0] + k * dir[0], c[1]
# 			if chY < 0 or chY >= H or chX < 0 or chX >= W or data[chY][chX] != '#':
# 				break
#
# 			dist = 0
# 			for l in range(W):
# 				chY, chX = c[0] + k * dir[0], c[1] + l * dir[1]
# 				if chY < 0 or chY >= H or chX < 0 or chX >= W or data[chY][chX] != '#':
# 					break
# 				dist = l + 1
#
# 			if firstDist is None or dist == firstDist:
# 				firstDist = dist
# 				firstDistCount += 1
# 			else:
# 				secondDist = dist
# 				secondDistCount += 1
# 		answer0 = min(firstDist, firstDistCount) + (min(secondDist, secondDistCount) if secondDist is not None else 0)
#
# 		firstDist, secondDist = None, None
# 		firstDistCount, secondDistCount = 0, 0
# 		for l in range(W):
# 			chY, chX = c[0], c[1] + l * dir[1]
# 			if chY < 0 or chY >= H or chX < 0 or chX >= W or data[chY][chX] != '#':
# 				break
#
# 			dist = 0
# 			for k in range(H):
# 				chY, chX = c[0] + k * dir[0], c[1] + l * dir[1]
# 				if chY < 0 or chY >= H or chX < 0 or chX >= W or data[chY][chX] != '#':
# 					break
# 				dist = l + 1
#
# 			if firstDist is None or dist == firstDist:
# 				firstDist = dist
# 				firstDistCount += 1
# 			else:
# 				secondDist = dist
# 				secondDistCount += 1
# 		answer1 = min(firstDist, firstDistCount) + (min(secondDist, secondDistCount) if secondDist is not None else 0)
#
# 		total += min(answer0, answer1)
#
# 		_(j, i, set(), set(), set(), True)
#
# print(total)

#
# def _2(j, i, v):
# 	if i>=W or i<0 or j>=H or j<0:
# 		return
# 	if data[j][i]!='#':
# 		return
# 	data[j][i]='.'
# 	_2(j + 1, i, v)
# 	_2(j - 1, i, v)
# 	_2(j, i-1, v)
# 	_2(j, i+1, v)
# def _(j, i, v, v2):
# 	if i>=W or i<0 or j>=H or j<0:
# 		return 0
# 	if data[j][i]!='#':
# 		return 0
# 	if (j, i) in v2:
# 		return 0
# 	v2.add((j, i))
# 	if (j, i) in v:
# 		a=_(j + 1, i, v, v2) + _(j - 1, i, v, v2)+_(j, i-1, v, v2) + _(j, i+1, v, v2)
# 		# print('    * ', j, i, a)
# 		return a
#
# 	vOrginal=v
# 	v2Original=v2
# 	v=set(vOrginal)
# 	v2=set(v2Original)
# 	for x in range(W):
# 		chX, chY = i - x, j
# 		if chX < 0 or chX >= W or chY < 0 or chY >= H or data[chY][chX] != '#' or (chY, chX) in v:
# 			break
# 		v.add((chY, chX))
# 	for x in range(1, W):
# 		chX, chY = i + x, j
# 		if chX < 0 or chX >= W or chY < 0 or chY >= H or data[chY][chX] != '#' or (chY, chX) in v:
# 			break
# 		v.add((chY, chX))
# 	output0 = 1+ _(j + 1, i, v, v2) + _(j - 1, i, v, v2)+_(j, i-1, v, v2) + _(j, i+1, v, v2)
#
# 	v = set(vOrginal)
# 	v2 = set(v2Original)
# 	for y in range(H):
# 		chX, chY = i, j-y
# 		if chX < 0 or chX >= W or chY < 0 or chY >= H or data[chY][chX] != '#' or (chY, chX) in v:
# 			break
# 		v.add((chY, chX))
# 	for y in range(1, H):
# 		chX, chY = i, j+y
# 		if chX < 0 or chX >= W or chY < 0 or chY >= H or data[chY][chX] != '#' or (chY, chX) in v:
# 			break
# 		v.add((chY, chX))
# 	output1 = 1 + _(j + 1, i, v, v2) + _(j - 1, i, v, v2)+_(j, i-1, v, v2) + _(j, i+1, v, v2)
# 	print('    ', j, i, output0, output1)
# 	return min(output0, output1)


# total=0
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]!='#': continue
# 		h=w=0
# 		for hCheck in range(H):
# 			if j+hCheck>=H or data[j+hCheck][i]!='#':
# 				break
# 			h=hCheck+1
# 		for wCheck in range(W):
# 			if i+wCheck>=W or data[j][i+wCheck]!='#':
# 				break
# 			w=wCheck+1
# 		print(data[j][i], h, w)
# 		for y in range(h):
# 			for x in range(w):
# 				data[j+y][i+x]='.'
# 		total+=min(h, w)
# print(total)





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

