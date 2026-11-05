#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); itertools: product (like permutations with replacement.  repeat=N lets you use the same range multiple times), permutations, combinations, combinations_with_replacement. heapq.heappush(a, 3)

# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# .venv/bin/pip3 install sortedcontainers astar z3-solver lmfit sympy shapely
# for lmfit:  sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran
# for shapely:  sudo apt install python3-dev pypy3-dev libgeos-dev
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
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

# data=data1;V=0
data=data2;V=1

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall(r'-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores


D=(H+1)//2
E=(H+1)//2-1
answer=0
for y in range(H):
	for x in range(W):
		if data[y][x]!='.': data[y][x]=int(data[y][x])
w=0
while True:
	output=0
	warriors=0
	for i in range(D*2-1):
		x=i
		y=D-1-i
		while y<0:
			x+=1
			y+=1
		h=0
		while True:
			if h>0: h-=1
			if data[y][x]<=0:
				data[y][x]+=1
			elif data[y][x]>h:
				output+=1
				h=data[y][x]
				data[y][x]+=1
				if data[y][x]==10:
					warriors+=1
					data[y][x]=-2
			x+=1
			y+=1
			if x>=W or y>=H or data[y][x]=='.': break
	dataOriginal=[[v for v in data[y]] for y in range(H)]
	for y in range(H):
		for x in range(W):
			left=E-y
			newY,newX = (x-left)//2, W-E+(x-left)//2-y*2-1
			if 0 <= newY < H and 0 <= newX < W:
				if (x+y)%2==V:
					data[y][x]=dataOriginal[newY][newX]
	# for row in data:
	# 	for column in row:
	# 		if column=='.': print('.', end='')
	# 		elif column<=0: print('X', end='')
	# 		else: print(column, end='')
	# 	print()
	print(output, warriors)

	answer+=output
	w+=warriors
	if w >= 100000:
		break
print(answer, answer-output)


# D=(H+1)//2
# E=(H+1)//2-1
# output=0
#
# for r in range(6):
# 	dataOriginal=[[v for v in data[y]] for y in range(H)]
# 	for y in range(H):
# 		for x in range(W):
# 			left=E-y
# 			newY,newX = (x-left)//2, W-E+(x-left)//2-y*2-1
# 			if 0 <= newY < H and 0 <= newX < W:
# 				if (x+y)%2==V:
# 					print(y, x, newY, newX, data[y][x], dataOriginal[newY][newX])
# 					data[y][x]=dataOriginal[newY][newX]
# 	for i in range(D*2-1):
# 		x=i
# 		y=D-1-i
# 		while y<0:
# 			x+=1
# 			y+=1
# 		h=0
# 		while True:
# 			if h>0: h-=1
# 			# print(i, x, y, data[y][x], data[y][x], h, int(data[y][x])>h)
# 			if int(data[y][x])>h:
# 				output+=1
# 				h=int(data[y][x])
#
# 			x+=1
# 			y+=1
# 			if x>=W or y>=H or data[y][x]=='.': break
# print(output)


# D=(H+1)//2
# output=0
# # for line in data:
# for i in range(D*2-1):
# 	x=i
# 	y=D-1-i
# 	while y<0:
# 		x+=1
# 		y+=1
# 	h=0
# 	while True:
# 		if h>0: h-=1
# 		# print(i, x, y, data[y][x], data[y][x], h, int(data[y][x])>h)
# 		if int(data[y][x])>h:
# 			output+=1
# 			h=int(data[y][x])
#
# 		x+=1
# 		y+=1
# 		if x>=W or y>=H or data[y][x]=='.': break


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
# 				newY,newX,newCost=y+dy,x+dx,cost+1
# 				newPositions.append((newCost, newY, newX))
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
#			newY,newX,newCost=y+dy,x+dx,cost+1
# 			if (newY, newX) in costs and newCost >= costs[(newY, newX)]: continue
# 			heapq.heappush(positions, (newCost, newY, newX))
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

