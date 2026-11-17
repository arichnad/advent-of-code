#!/usr/bin/python3
import collections
# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); itertools: product (like permutations with replacement.  repeat=N lets you use the same range multiple times), permutations, combinations, combinations_with_replacement. heapq.heappush(a, 3); d=copy.deepcopy(d)

# from sortedcontainers import SortedList

# from fractions import Fraction; Fraction(1, 3)
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

def _():

	round=0
	i=0
	while True:
		x,y,z=None,None,None
		group={}
		# firstGroup={}
		g=None
		for j in range(len(data)):
			if j==0 or data[j-1]!=data[j]:
				if data[j] not in group: group[data[j]]=0
				group[data[j]]+=1
		for j in range(len(data)):
			if group[data[j]]>1:
				g=data[j]
				break
		if g is None: break
		for j in range(len(data)):
			if data[j]==g:
				w=j
				break
		for j in range(w, len(data)):
			if data[j]!=g:
				x=j
				break
		# if x is None: break
		for j in reversed(range(x+1,len(data))):
			if data[j]==g:
				y=j
				break
		print(round+1, ''.join(data[x:]))
		# if x is None or y is None or z is None: break
		# c=data[:]
		for j in range(x, (x+y+1)//2):
			data[j],data[y-(j-x)]=data[y-(j-x)],data[j]
			i+=2
		if (x+y+1)%2==1:
			i+=1
		round+=1

	print(round, i)


data3='''
'''.strip('\n').splitlines() # 26 838
data4='''
'''.strip('\n').splitlines() # 55 2090
data5='''
'''.strip('\n').splitlines() # 3 22
data6='''
'''.strip('\n').splitlines() # 6199 24454793 61999 2446011368 ()



# data=[c for c in data6[0]]
data=[c for c in data6[0]]*100
# data=[c for c in data2[0]]*100
# import fileinput # data=[a.strip('\n') for a in fileinput.input()]

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores

# _(); sys.exit(0)

i=0
round=0
answer=0
j=0
start,end=0,len(data)-1

ending=[]
# ending=collections.deque()
round=0
data=collections.deque(data)
beginning=None
cur=data.popleft()
side=0
answer=0
while True:
	otherSide=-1-side
	while len(data)>=1 and data[side]==cur:
		data.popleft() if side == 0 else data.pop()

	while len(data)>=1 and data[otherSide]!=cur:
		value=data[otherSide]
		while len(data)>=1 and data[otherSide]==value:
			data.popleft() if otherSide == 0 else data.pop()
			ending.append(value)

	count=0
	while len(data)>=1 and data[otherSide]==cur:
		value=data.popleft() if otherSide == 0 else data.pop()
		count+=1
		ending.append(cur)

	if count==0:
		if len(data)==0:
			data=collections.deque(ending)
			ending=[]
			# data = ending
			# ending = collections.deque()
			print('done no more data', round+1)
			if len(data)==0:
				break

		cur=data.popleft() if side == 0 else data.pop()
		while len(data)>=1 and data[side]==cur:
			data.popleft() if side == 0 else data.pop()

		print('done', round+1)
		continue

	index = None
	for i in range(len(ending)):
		if ending[i][0]==cur:
			index = i
			break
	width = len(ending) - index
	answer+= len(data) + width
	ending=ending[:index]

	round+=1
	side=otherSide

	if round%1000==0:
		# print(round+1, ''.join(data if side==0 else reversed(data))+''.join(reversed(ending)))
		print(round, len(data), len(ending))
print(round, answer)
sys.exit(0)


# sys.exit(0)
# direction=1
# beginning=None
# for j in range(len(data)):
# 	if j==0 or data[j-1]!=data[j]:
# 		if beginning is not None:
# 			if data[j-1] not in h: h[data[j-1]]=[]
# 			h[data[j-1]].append((beginning, j-1))
# 		beginning=j
# h[data[-1]].append((beginning, j))
#
# j=0
# cur=data[0]
# curSection=h[cur].pop(0)
# direction=1
# while len(h)>1:
# 	leftIndex=0 if direction == 1 else -1
# 	rightIndex=-1 if direction == 1 else 0
# 	if len(h[cur])<=1:
# 		# a=h[cur].pop(leftIndex)
# 		del h[cur]
# 		if len(h)==0: break
# 		cur=min((h[_][leftIndex][0], _) for _ in h.keys())[1]
# 		# print('changing to', cur, h[cur][0])
# 		while len(h[cur]) >= 2 and h[cur][leftIndex][1]+1==h[cur][leftIndex+direction][0]:
# 			# print('first chop', cur)
# 			a=h[cur].pop(leftIndex)
# 			h[cur][leftIndex]=(a[0], h[cur][leftIndex][1])
# 		curSection=h[cur].pop(leftIndex)
# 		continue
# 	if direction==1:
# 		a,b=curSection,h[cur].pop(rightIndex)
# 	else:
# 		a,b=h[cur].pop(rightIndex),(curSection[0],curSection[1])
# 	while len(h[cur]) >= 1 and h[cur][rightIndex][1]==b[0]-1:
# 		# print('chopping', cur)
# 		b2=h[cur].pop(rightIndex)
# 		b=(b2[0],b[1])
# 	left,right=a[1]+1,b[1]
# 	width=b[1]-b[0]+1
# 	print(a, b, width)
# 	# if len(h[cur])==1 and len(h)==1:
# 	# 	print('skipping last', answer)
# 	# 	break
# 	answer+=right-left+1
# 	for v in h.keys():
# 		for w in range(len(h[v])):
# 			# if w==0 and v==cur: continue
# 			if not (h[v][w][0]>=left and h[v][w][1]<=right):
# 				h[v][w]=(right+left-h[v][w][1], right+left-h[v][w][0])
# 		h[v]=sorted(h[v]) # remove sort
# 		# if v==cur:
# 		# 	leftIndex=-1 if direction == 1 else 0
# 		# 	if direction==1:
# 		# 		h[v][leftIndex]=(h[v][leftIndex][0] - width, h[v][leftIndex][1])
# 		# 	else:
# 		# 		h[v][leftIndex]=(h[v][leftIndex][0], h[v][leftIndex][1] + width)
# 		print(v, h[v])
#
# 	print()
# 	curSection=(curSection[0], curSection[1]+width)
# 	# h[cur][0]=(h[cur][0][0], h[cur][0][1]+width)
#
#
#
#
# 	round+=1
# 	direction=-direction
#
# 	print(round+1, cur, answer)
# 	for i in range(len(data)) if direction == 1 else reversed(range(len(data))):
# 		for v, w in h.items():
# 			for ww in w:
# 				if ww[0]<=i<=ww[1]:
# 					print(v, end='')
# 		print(' ', end='')
# 	print()
#
# 	if round==2: break
#
# 	# j=left+b[1]-b[0]+1-1
#
# print(round, answer) # 135154 55 2090
# sys.exit(0)



#
#
# # for line in data:
# data=data[0]
# print(''.join(data))
# i=0
# while True:
# 	x,y,z=None,None,None
# 	group={}
# 	g=None
# 	for j in range(len(data)):
# 		if j==0 or data[j-1]!=data[j]:
# 			if data[j] not in group: group[data[j]]=0
# 			group[data[j]]+=1
# 	for j in range(len(data)):
# 		if group[data[j]]>1:
# 			print(j)
# 			g=data[j]
# 			break
# 	print(g)
# 	if g is None: break
# 	for j in range(len(data)):
# 		if data[j]==g:
# 			w=j
# 			break
# 	for j in range(w, len(data)):
# 		if data[j]!=g:
# 			x=j
# 			break
# 	# if x is None: break
# 	for j in reversed(range(x+1,len(data))):
# 		if data[j]==g:
# 			y=j
# 			break
# 	# if x is None or y is None or z is None: break
# 	print(w, x, y, z, data)
# 	c=data[:]
# 	for j in range(x, y+1):
# 		data[j]=c[y-(j-x)]
# 	print(''.join(data))
# 	i+=1
# print(i)

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
# 				if newY<0 or newY>=H or newX<0 or newX>=W: continue
#
# for line in data: print(''.join(line))

# bfs simple queue (sorting slows things down some, you can remove sort if costs go up by the same every round)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, (startY, startX))]
# endPoint = (endY, endX)
# costs={}
# while len(positions) > 0:
# 	# print(len(positions))
# 	newPositions = []
# 	for (cost, point) in sorted(positions): # remove sorted here if cost goes up by the same every round
# 		(y, x) = point
#
# 		costKey = point
# 		if costKey in costs and cost >= costs[costKey]: continue # change >= here to > if you need to analyze ties
# 		costs[costKey] = cost
#
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				# if dx==0 and dy==0: continue
# 				if abs(dx)+abs(dy) != 1: continue
# 				ny,nx = y+dy,x+dx
# 				if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
# 				if data[ny][nx] == '#': continue
#
# 				newCost = cost + 1
# 				newPoint = (ny, nx)
#
# 				if newPoint == endPoint:
# 					print(newCost)
# 					sys.exit(0)
#
# 				newPositions.append((newCost, newPoint))
# 	positions=newPositions


# bfs with a heap (fast sorting)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, (startY, startX))]
# endPoint = (endY, endX)
# costs={}
# while len(positions) > 0:
# 	(cost, point) = heapq.heappop(positions)
# 	(y, x) = point
#
# 	costKey = point
# 	if costKey in costs and cost >= costs[costKey]:
# 		continue
# 	costs[costKey] = cost
#
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			ny,nx = y+dy,x+dx
# 			if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
# 			if data[ny][nx] == '#': continue
#
# 			newCost = cost+1
# 			newPoint = (ny, nx)
#
# 			if newPoint==endPoint:
# 				print(newCost)
# 				sys.exit(0)
#
# 			costKey = newPoint
# 			if costKey in costs and newCost >= costs[costKey]: continue
#
# 			heapq.heappush(positions, (newCost, newPoint))

# flood fill does NOT work when want a breadth first (minimum cost, that sort of thing)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# visited=set()
# def ff(point):
# 	(y, x) = point
# 	if (y, x) in visited: return 0
# 	visited.add((y, x))
#
# 	answer=1
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			ny,nx = y+dy,x+dx
# 			if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
# 			if data[ny][nx] == '#': continue
#
# 			newPoint = (ny, nx)
# 			answer+=ff(newPoint)
# 	return answer
#
# print(ff((startY, startX), ))

