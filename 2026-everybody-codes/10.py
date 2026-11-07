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

data1='''

'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()
data3='''

'''.strip('\n').splitlines()

data=data2; C=1000000000000
# data=data2; C=10000
# import fileinput # data=[a.strip('\n') for a in fileinput.input()]

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores


ghost={}
g=0
data = [[column for column in line] for line in data]
for j in range(H):
	for i in range(W):
		d=data[j][i]
		dir = '>v<^'.find(d.lower())
		if dir!=-1:
			ghost[g]=(i, j, dir, 0)
			data[j][i]='.'
			g+=1

round=1
seen={}; collisions={}
while len(ghost)>=1:
	simpleGhost=tuple((g, ghost[g][0:3]) for g in ghost.keys())
	if simpleGhost in seen:
		(originalRound, originalCollisions)=seen[simpleGhost]
		roundChange = round - originalRound
		shortestRounds=None
		for g in list(ghost.keys()):
			if g not in collisions:
				# print('oof')
				continue
			o=originalCollisions[g] if g in originalCollisions else 0
			rounds=(C - ghost[g][3])//(collisions[g]-o)-1
			if rounds<0: rounds=0
			if shortestRounds is None or rounds < shortestRounds:
				shortestRounds=rounds
		if shortestRounds is not None:
			print('------------yes', shortestRounds, roundChange)
			# fast-forward
			round+=shortestRounds*roundChange
			for g in list(ghost.keys()):
				if g not in collisions: continue
				(i, j, dir, c) = ghost[g]
				o = originalCollisions[g] if g in originalCollisions else 0
				c+=(collisions[g]-o)*shortestRounds
				ghost[g] = (i, j, dir, c)
			seen={}; collisions={}
	seen[simpleGhost]=(round, dict(collisions))
	for g in list(ghost.keys()):
		(i, j, dir, c) = ghost[g]
		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
		newY, newX = j + dy, i + dx
		if newY<0 or newX<0 or newY>=H or newX>=W: continue
		if data[newY][newX]!='.':
			a,b=newX,newY
			newY,newX=j,i
			dir=(dir+1)%4
			if g not in collisions: collisions[g] = 0
			collisions[g] += 1
			c+=1
			if c==C:
				del ghost[g]
				seen={}; collisions={}
				print('---------------', round, len(ghost))
				continue
		ghost[g]=(newX, newY, dir, c)
	spots = {}
	for g in ghost.keys():
		(i, j, dir, c) = ghost[g]
		if (i, j) not in spots: spots[(i, j)] = set()
		spots[(i, j)].add(g)
	for g in list(ghost.keys()):
		(i, j, dir, c) = ghost[g]
		if len(spots[(i, j)])==1: continue
		dir = (dir + 2)%4
		if g not in collisions: collisions[g] = 0
		collisions[g] += 1
		c+=1
		if c==C:
			del ghost[g]
			seen={}; collisions={}
			print('---------------', round, len(ghost))
			continue
		ghost[g]=(i, j, dir, c)
	round+=1
	if len(ghost)==1:
		print(round, len(ghost), len(seen), len(collisions))
print(round-1, len(ghost))
# ghost={}
# g=0
# data = [[column for column in line] for line in data]
# for j in range(H):
# 	for i in range(W):
# 		d=data[j][i]
# 		dir = '>v<^'.find(d.lower())
# 		if dir!=-1:
# 			ghost[g]=(i, j, dir, 0)
# 			data[j][i]='.'
# 			g+=1
#
# round=1
# while len(ghost)>=1:
# 	for g in list(ghost.keys()):
# 		(i, j, dir, c) = ghost[g]
# 		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
# 		newY, newX = j + dy, i + dx
# 		if newY<0 or newX<0 or newY>=H or newX>=W: continue
# 		if data[newY][newX]!='.':
# 			a,b=newX,newY
# 			newY,newX=j,i
# 			dir=(dir+1)%4
# 			c+=1
# 			if c==C:
# 				del ghost[g]
# 				continue
# 		ghost[g]=(newX, newY, dir, c)
# 	spots = {}
# 	for g in ghost.keys():
# 		(i, j, dir, c) = ghost[g]
# 		if (i, j) not in spots: spots[(i, j)] = set()
# 		spots[(i, j)].add(g)
# 	for g in list(ghost.keys()):
# 		(i, j, dir, c) = ghost[g]
# 		if len(spots[(i, j)])==1: continue
# 		dir = (dir + 2)%4
# 		c+=1
# 		if c==C:
# 			del ghost[g]
# 			continue
# 		ghost[g]=(i, j, dir, c)
# 	round+=1
# print(round-1, len(ghost))


# ghost=[]
# data = [[column for column in line] for line in data]
# for j in range(H):
# 	for i in range(W):
# 		d=data[j][i]
# 		dir = '>v<^'.find(d.lower())
# 		if dir!=-1:
# 			ghost.append((i, j, dir))
# 			data[j][i]='.'
#
# collision=0
# for round in range(10):
# 	for g in range(len(ghost)):
# 		(i, j, dir) = ghost[g]
# 		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
# 		newY, newX = j + dy, i + dx
# 		if newY<0 or newX<0 or newY>=H or newX>=W: continue
# 		if data[newY][newX]!='.':
# 			a,b=newX,newY
# 			newY,newX=j,i
# 			dir=(dir+1)%4
# 			collision+=1
# 		ghost[g]=(newX, newY, dir)
# 	spots = {}
# 	for g in range(len(ghost)):
# 		(i, j, dir) = ghost[g]
# 		if (i, j) not in spots: spots[(i, j)] = set()
# 		spots[(i, j)].add(g)
# 	for g in range(len(ghost)):
# 		(i, j, dir) = ghost[g]
# 		if len(spots[(i, j)])==1: continue
# 		dir = (dir + 2)%4
# 		collision+=1
# 		ghost[g]=(i, j, dir)
# print(collision)

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

