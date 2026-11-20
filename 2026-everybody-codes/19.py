
# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); itertools: product (like permutations with replacement.  repeat=N lets you use the same range multiple times), permutations, combinations, combinations_with_replacement. heapq.heappush(a, 3); d=copy.deepcopy(d)


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
data3='''

'''.strip('\n').splitlines()
data4='''

'''.strip('\n').splitlines()

data=data4
# import fileinput # data=[a.strip('\n') for a in fileinput.input()]

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores


aOriginal=data

best=0
total=W*H
# goal=int(math.ceil(math.cbrt(total)))
g=total//3
out={}
for i in ['K', 'C', 'M', 'Y', 'R', 'G', 'B']:
	out[i]=0
for a in aOriginal:
	for a in a:
		out[a]+=1
outOriginal=copy.deepcopy(out)
for y in list(itertools.combinations(['K', 'C', 'M', 'Y', 'R', 'G', 'B'], 3)):
	# z={}
	# print(y)
	# for f, t in zip(['C', 'M', 'Y', 'K'], y):
	# 	z[f]=t
	# if a=='K' or b=='K':
	# 	out['K']+=1
	# elif a=='C' and b=='M' or a=='M' and b=='C':
	# 	out['B']+=1
	# elif a=='C' and b=='Y' or a=='Y' and b=='C':
	# 	out['G']+=1
	# elif a=='M' and b=='Y' or a=='Y' and b=='M':
	# 	out['R']+=1
	# else:
	# 	# print(a, b)
	# 	out[a]+=1


	# for goal in range(g-1, g+2):
	for goal in range(g-8000, g+2):
		out=copy.deepcopy(outOriginal)

		d=[0, 0, 0]
		# print(y, goal, out, total)
		for i, a in enumerate(y):
			if a=='K' or a=='C' or a=='M' or a=='Y':
				take=min(out[a], goal-d[i])
				d[i]+=take
				out[a]-=take
				# print('    ', i, take, a)
				continue
			if a=='R':
				b,c='M','Y'
			if a=='G':
				b,c='C','Y'
			if a=='B':
				b,c='C','M'
			if out[b] > out[c]:
				b,c=c,b

			take=min(out[b], goal-d[i])
			d[i]+=take
			out[b]-=take
			# print('    ', i, take, b, c)

			take=min(out[c], goal-d[i])
			d[i]+=take
			out[c]-=take

			# print('    ', i, take, b, c)

		for i, a in enumerate(y):
			if a=='K' or a=='C' or a=='M' or a=='Y':
				take=out[a]
				d[i]+=take
				out[a]-=take
				continue
			if a=='R':
				b,c='M','Y'
			if a=='G':
				b,c='C','Y'
			if a=='B':
				b,c='C','M'
			if out[b] > out[c]:
				b,c=c,b

			take=out[b]
			d[i]+=take
			out[b]-=take
			# print('    ', i, take, b, c)

			take=out[c]
			d[i]+=take
			out[c]-=take

			# print('    ', i, take, b, c)

		white=d[0]*d[1]*d[2]
		# print(y, goal, d[0], d[1], d[2], white, out)
		# x=sorted(out.items(), key=lambda a: a[1], reverse=True)
		# white = x[0][1]* x[1][1]* x[2][1]
		# print(y, x[0][1], x[1][1], x[2][1], white)
		if white>best: best=white
	# break
print(best)



# aOriginal=data[0:H]
# bOriginal=data[H+1:]
# best=0
# for y in list(itertools.permutations(range(4), 4)):
# 	out={}
# 	for i in ['K', 'C', 'M', 'Y', 'R', 'G', 'B']:
# 		out[i]=0
# 	for a,b in zip(aOriginal,bOriginal):
# 		for a,b in zip(a, b):
# 			b=int(b)-1
# 			if a=='K' or b==y[3]:
# 				out['K']+=1
# 			elif a=='C' and b==y[1] or a=='M' and b==y[0]:
# 				out['B']+=1
# 			elif a=='C' and b==y[2] or a=='Y' and b==y[0]:
# 				out['G']+=1
# 			elif a=='M' and b==y[2] or a=='Y' and b==y[1]:
# 				out['R']+=1
# 			else:
# 				# print(a, b)
# 				out[a]+=1
# 	x=sorted(out.items(), key=lambda a: a[1], reverse=True)
# 	white = x[0][1]* x[1][1]* x[2][1]
# 	print(y, x[0][1], x[1][1], x[2][1], white)
# 	if white>best: best=white
# print(best)

# a=data[0:H]
# b=data[H+1:]
# out={}
# for i in ['K', 'C', 'M', 'Y', 'R', 'G', 'B']:
# 	out[i]=0
#
# for a,b in zip(a,b):
# 	for a,b in zip(a, b):
# 		if a=='K' or b=='K':
# 			out['K']+=1
# 		elif a=='C' and b=='M' or a=='M' and b=='C':
# 			out['B']+=1
# 		elif a=='C' and b=='Y' or a=='Y' and b=='C':
# 			out['G']+=1
# 		elif a=='M' and b=='Y' or a=='Y' and b=='M':
# 			out['R']+=1
# 		else:
# 			print(a, b)
# 			out[a]+=1
# x=sorted(out.items(), key=lambda a: a[1], reverse=True)
# print(x[0][1]* x[1][1]* x[2][1])




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

