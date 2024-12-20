#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, numpy # list(itertools.permutations(range(4), 4))
# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
# from astar import AStar #python3 -mpip install astar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
# import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
# from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()


for j in range(H):
	for i in range(W):
		if data[j][i]=='S':
			startX,startY=i,j
		if data[j][i]=='E':
			endX,endY=i,j


positions = [(0, endX, endY)]
endCosts={}
while len(positions) > 0:
	newPositions = []
	for (cost, x, y) in positions:
		if y<0 or y>=H or x<0 or x>=W: continue
		if data[y][x] == '#': continue
		if (x, y) in endCosts and cost >= endCosts[(x, y)]: continue  # change >= here to > if you need to analyze ties
		endCosts[(x, y)]=cost

		newPositions.append((cost + 1, x + 1, y))
		newPositions.append((cost + 1, x - 1, y))
		newPositions.append((cost + 1, x, y - 1))
		newPositions.append((cost + 1, x, y + 1))
	positions=newPositions

# positions = [(0, (), startX, startY)]
# costs={}
# answers=[]
# while len(positions) > 0:
# 	print(len(positions))
# 	newPositions = []
# 	for (cost, ch, x, y) in positions:
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		# if data[y][x] == '#': continue
# 		if (ch, x, y) in costs and cost >= costs[(ch, x, y)]: continue #change >= here to > if you need to analyze ties
# 		costs[(ch, x, y)]=cost
# 		if data[y][x]=='#':
# 			if len(ch)==0:
# 				ch=((x, y))
# 			elif len(ch)==1:
# 				((i, j))=ch
# 				if (abs(x-i)==1 and y==j) or (abs(y-j)==1 and x==i):
# 					ch=(sorted([(i, j), (x, y)]))
# 				else: continue
# 			else: continue
# 		if len(ch)!=0 and (x, y) in endCosts:
# 			answers.append(endCosts[(x, y)]+cost)
# 			continue
#
# 		newPositions.append((cost + 1, ch, x + 1, y))
# 		newPositions.append((cost + 1, ch, x - 1, y))
# 		newPositions.append((cost + 1, ch, x, y - 1))
# 		newPositions.append((cost + 1, ch, x, y + 1))
# 	positions=newPositions
# total=costs[((), endX, endY)]
# answer=0
# # for (ch, x, y), t in costs.items():
# # 	if ch == () or x!=endX or y!=endY: continue
# # 	if total-t>=100: answer+=1
# for t in answers:
# 	if total-t>=100: answer+=1
# 	# print(ch, total-t)
#
# print(answer)

# positions = [(0, None, startX, startY, None, None)]
# costs={}
# answers=set()
# C=20
# while len(positions) > 0:
# 	# print(len(positions))
# 	newPositions = []
# 	for (cost, ch, x, y, prevX, prevY) in positions:
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if (ch, x, y) in costs and cost >= costs[(ch, x, y)]: continue #change >= here to > if you need to analyze ties
# 		costs[(ch, x, y)]=cost
# 		if data[y][x]=='#':
# 			if ch is None:
# 				ch=(cost, prevX, prevY, prevX, prevY)
# 			else:
# 				(c, x2, y2, x3, y3) = ch
#
# 				if cost + 1 < c + C:
# 					ch = (c, x2, y2, x, y)
# 				else:
# 					continue
# 		# else:
# 		# 	if ch is not None:
# 		# 		(c, x2, y2, x3, y3) = ch
# 		# 		ch = (-1000, x2, y2, x3, y3)
#
# 		if ch is not None and (x, y) in endCosts:
# 			(c, x2, y2, x3, y3) = ch
# 			# answers.add((endCosts[(x, y)]+cost, tuple(sorted([(x2, y2), (x, y)]))))
# 			answers.add((endCosts[(x, y)] + cost, ((x2, y2), (x, y))))
# 			# if cost + 1 >= c + C: continue
#
# 		newPositions.append((cost + 1, ch, x + 1, y, x, y))
# 		newPositions.append((cost + 1, ch, x - 1, y, x, y))
# 		newPositions.append((cost + 1, ch, x, y - 1, x, y))
# 		newPositions.append((cost + 1, ch, x, y + 1, x, y))
# 	positions=newPositions
# total=costs[(None, endX, endY)]
# answer=0
# print(answers)
# d={}
# for (t, k) in sorted(answers):
# 	if total-t>=50:
# 		if total-t==74: print(k, total, t)
# 		if total-t not in d: d[total-t]=0
# 		d[total-t]+=1
# 	if total-t>=100: answer+=1
# 	# print(ch, total-t)
# print(d)
# print(answer)

positions = [(0, None, startX, startY, None, None)]
costs={}
answers=set()
C=20
total=endCosts[(startX, startY)]
while len(positions) > 0:
	# print(len(positions))
	newPositions = []
	for (cost, ch, x, y, prevX, prevY) in positions:
		if y<0 or y>=H or x<0 or x>=W: continue
		if (ch, x, y) in costs and cost >= costs[(ch, x, y)]: continue #change >= here to > if you need to analyze ties
		costs[(ch, x, y)]=cost
		if data[y][x]=='#':
			continue
		else:
			for dy in range(-C,C+1):
				for dx in range(-C,C+1):
					x3,y3=x+dx,y+dy
					if (dx==0 and dy==0) or abs(dx)+abs(dy)>C or (x3, y3) not in endCosts:
						continue
					answers.add((total - (endCosts[(x3, y3)] + cost + abs(dx) + abs(dy)), ((x, y), (x3, y3))))

		newPositions.append((cost + 1, ch, x + 1, y, x, y))
		newPositions.append((cost + 1, ch, x - 1, y, x, y))
		newPositions.append((cost + 1, ch, x, y - 1, x, y))
		newPositions.append((cost + 1, ch, x, y + 1, x, y))
	positions=newPositions
answer=0
# print(answers)
d={}
for (t, k) in answers:
	# if t>=50:
	# 	if t==74: print(k, t)
	# 	if t not in d: d[t]=0
	# 	d[t]+=1
	if t>=100: answer+=1
# print(d)
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

# positions = [(0, startX, startY)]
# costs={}
# while len(positions) > 0:
# 	newPositions = []
# 	for (cost, x, y) in sorted(positions): #remove sorted here if it's not needed
#		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x] == '#': continue
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue #change >= here to > if you need to analyze ties
# 		costs[(x, y)] = cost
#
# 		newPositions.append((cost + 1, x + 1, y))
# 		newPositions.append((cost + 1, x - 1, y))
# 		newPositions.append((cost + 1, x, y - 1))
# 		newPositions.append((cost + 1, x, y + 1))
# 	positions=newPositions
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
# ff(startX, startY)
