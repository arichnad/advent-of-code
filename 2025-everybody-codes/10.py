#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); heapq.heappush(a, 3)
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
'''.strip('\n').splitlines()
data2='''
'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() #does not run in parallel on separate cores


#for line in data:



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

# bfs
# sheep=[]
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='D': startX,startY=i,j
# 		if data[j][i]=='S':
# 			data[j][i]='.'
# 			sheep.append((i,j))
# positions = [(0, startX, startY)]
# costs={}
# answer=0
# first=True
# while len(positions) > 0:
# 	newPositions = []
# 	visited=set()
# 	for (cost, x, y) in sorted(positions): #remove sorted here if it's not needed
# 		if cost == 3+1:
# 			continue
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if (x,y) in visited: continue
# 		visited.add((x,y))
# 		if data[y][x]!='#' and (x, y) in sheep: answer+=1
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue #change >= here to > if you need to analyze ties
# 		costs[(x, y)] = cost
#
# 		newPositions.append((cost + 1, x + 2, y+1))
# 		newPositions.append((cost + 1, x - 2, y+1))
# 		newPositions.append((cost + 1, x + 2, y-1))
# 		newPositions.append((cost + 1, x - 2, y-1))
# 		newPositions.append((cost + 1, x - 1, y+2))
# 		newPositions.append((cost + 1, x + 1, y+2))
# 		newPositions.append((cost + 1, x - 1, y-2))
# 		newPositions.append((cost + 1, x + 1, y-2))
#
#
#
# 	sheep = [(s[0],s[1]+1) for s in sheep]
# 	for (cost, x, y) in positions:
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x]!='#' and (x, y) in sheep:
# 			print('  ', x, y)
# 			answer+=1
#
# 	print(answer)
# print(answer)

# sheep=[]
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='D': startX,startY=i,j
# 		if data[j][i]=='S':
# 			data[j][i]='.'
# 			sheep.append((i,j))
# positions = [(0, startX, startY)]
# costs={}
# answer=0
# first=True
# for v in range(20):
# 	newPositions = []
# 	visited=set()
# 	for (cost, x, y) in sorted(positions): #remove sorted here if it's not needed
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if (x, y) in visited: continue
# 		visited.add((x,y))
#
# 		newPositions.append((cost + 1, x + 2, y+1))
# 		newPositions.append((cost + 1, x - 2, y+1))
# 		newPositions.append((cost + 1, x + 2, y-1))
# 		newPositions.append((cost + 1, x - 2, y-1))
# 		newPositions.append((cost + 1, x - 1, y+2))
# 		newPositions.append((cost + 1, x + 1, y+2))
# 		newPositions.append((cost + 1, x - 1, y-2))
# 		newPositions.append((cost + 1, x + 1, y-2))
#
# 	for (cost, x, y) in newPositions:
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x]!='#' and (x, y) in sheep:
# 			print('  ', x, y)
# 			answer+=1
# 			sheep.remove((x, y))
#
# 	sheep = [(s[0],s[1]+1) for s in sheep]
# 	print(answer)
#
# 	for (cost, x, y) in newPositions:
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x]!='#' and (x, y) in sheep:
# 			print('  ', x, y)
# 			answer+=1
# 			sheep.remove((x, y))
#
# 	print(answer)
#
# 	positions=newPositions
# 	print(answer)
# print(answer)

sh=[]
for j in range(H):
	for i in range(W):
		if data[j][i]=='D': startX,startY=i,j
		if data[j][i]=='S':
			data[j][i]='.'
			sh.append((i,j))
positions = {(startX, startY, tuple(sh)): 1}
answer=0
first=True
while len(positions)>0:
# for n in range(8):
	newPositions = {}
	for (x, y, sheep), ways in positions.items():
		moved=False
		tmp=list(sheep)
		for (sx,sy) in sheep:
			if sy+1==H:
				moved=True
				continue
			if data[sy+1][sx]=='#' or (x,y)!=(sx,sy+1):
				moved=True

				tmp.remove((sx,sy))
				tmp.append((sx,sy+1))
				key=(x,y,tuple(sorted(tmp)))
				if key in newPositions:
					newPositions[key]+=ways
				else:
					newPositions[key]=ways
				# moves + " S>{}{}".format(chr(ord('A')+sx), sy+1+1))
				tmp.remove((sx,sy+1))
				tmp.append((sx,sy))
		if not moved:
			if len(sheep)!=1: print('no')
			key=(x,y,sheep)
			if key in newPositions:
				newPositions[key]+=ways
			else:
				newPositions[key]=ways
	positions=newPositions

	newPositions={}
	for (x, y, sheep), ways in positions.items():
		if y<0 or y>=H or x<0 or x>=W: continue

		for (x, y) in (
				(x + 2, y+1),
				(x - 2, y+1),
				(x + 2, y-1),
				(x - 2, y-1),
				(x - 1, y+2),
				(x + 1, y+2),
				(x - 1, y-2),
				(x + 1, y-2),
		):
			if y<0 or y>=H or x<0 or x>=W: continue
			newSheep = []
			for (sx,sy) in sheep:
				if data[y][x] != '#' and (x,y)==(sx,sy):
					continue
				newSheep.append((sx, sy))
			if len(newSheep)==0:
				print('         ', answer, ways)
				answer += ways
				continue
			key=(x,y,tuple(newSheep))
			if key in newPositions:
				newPositions[key]+=ways
			else:
				newPositions[key]=ways
			# moves + " D>{}{}".format(chr(ord('A')+x), y+1))
	positions=newPositions
print(answer)

# dijkstra's
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startX,startY=i,j
# 		if data[j][i]=='E': endX,endY=i,j
# positions = [(0, startX, startY)]
# costs={}
# while len(positions) > 0:
# 	(cost, x, y) = heapq.heappop(positions)
# 	if y<0 or y>=H or x<0 or x>=W: continue
# 	if data[y][x]=='#': continue
# 	if (x, y) in costs and cost >= costs[(x, y)]: continue
# 	costs[(x, y)] = cost
#
# 	for (cost, x, y) in ((cost + 1, x + 1, y), (cost + 1, x - 1, y), (cost + 1, x, y - 1), (cost + 1, x, y + 1)):
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue
# 		heapq.heappush(positions, (cost, x, y))
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
