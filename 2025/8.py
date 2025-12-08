#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); heapq.heappush(a, 3)
# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# .venv/bin/pip3 install sortedcontainers astar z3 z3-solver lmfit sympy shapely
# for lmfit:  sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran
# for shapely:  sudo apt install python3-dev pypy3-dev libgeos-dev
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #SortedList('bat') + 'cat'
# from astar import AStar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3 import * # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
# import lmfit
# from sympy import * # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area)
# from testtemplate import *

data1='''
'''.strip('\n').splitlines()
data2='''
'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]; H=len(data)
data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores

dist=[]
for a in range(H):
	for b in range(a+1, H):
		# if a in s and b in s and s[a]==s[b]: continue
		cur=(data[a][0]-data[b][0])**2+(data[a][1]-data[b][1])**2+(data[a][2]-data[b][2])**2
		dist.append((cur, a, b))

s={}
t=[[i] for i in range(H)]
for i in range(H):
	s[i]=i

dist=sorted(dist, reverse=True)
print(dist[-1])
while True:
	(m,ma,mb) = dist.pop()
	print(len(dist), m, data[ma][0], data[mb][0], s)
	sma,smb=s[ma],s[mb]
	if sma==smb: continue
	# print(sma, smb)
	for x in t[smb]: t[sma].append(x)
	t[smb]=[]
	s[mb]=s[ma]
	for x in t[sma]: s[x]=sma
	last=(m,data[ma][0],data[mb][0])
	if len(t[sma])==H: break

print(last[1]*last[2])



# s={}
# d=set()
# for changes in range(1000):
# 	m=math.inf
# 	for a in range(H):
# 		for b in range(H):
# 			if a==b: continue
# 			if (a,b) in d: continue
# 			# if a in s and b in s and s[a]==s[b]: continue
# 			cur=(data[a][0]-data[b][0])**2+(data[a][1]-data[b][1])**2+(data[a][2]-data[b][2])**2
# 			if cur<m:
# 				m,ma,mb=cur,a,b
# 	d.add((ma,mb)); d.add((mb,ma))
# 	# print(data[ma], data[mb])
# 	if ma not in s:
# 		s[ma]=set()
# 	if mb not in s:
# 		s[mb]=set()
# 	s[ma].add(ma)
# 	s[mb].add(mb)
# 	changes=True
# 	while changes:
# 		changes=False
# 		for x in s[mb].copy():
# 			for y in s[ma].copy():
# 				if y not in s[x]:
# 					s[x].add(y)
# 					changes=True
# 				if x not in s[y]:
# 					s[y].add(x)
# 					changes=True
#
# print(s)
# v=set()
# answer=[]
# for i in s.values():
# 	aa=tuple(sorted(list(i)))
# 	if aa in v: continue
# 	v.add(aa)
# 	print(len(i), aa)
# 	answer.append(len(i))
# answerTotal=1
# for a in sorted(answer, reverse=True)[:3]:
# 	answerTotal*=a
# print(answerTotal)

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

