#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')
#from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
W,H=len(data[0]),len(data)
answer=[0]
visited=set()

choices=[]
for j in range(H):
	for i in range(W):
		if data[j][i] == '#': continue
		choice=0
		for dir in range(4):
			dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
			newY, newX = j + dy, i + dx
			if newY < 0 or newX < 0 or newY >= H or newX >= W:
				choices.append((i,j))
				choice=0
				break
			if data[newY][newX] == '#': continue
			choice+=1
		if choice>2:
			choices.append((i,j))
c={}
for choice in choices:
	(choiceX, choiceY) = choice
	ans=[]
	for startDir in range(4):
		dir=startDir
		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
		y, x = choiceY + dy, choiceX + dx
		if y < 0 or y < 0 or y >= H or x >= W or data[y][x] == '#': continue
		distance=1
		while True:
			previousDir = dir
			for dir in range(4):
				if previousDir == (dir+2)%4: continue
				dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
				newY, newX = y + dy, x + dx
				if newY < 0 or newX < 0 or newY >= H or newX >= W:
					x, y = newX, newY
					break
				if data[newY][newX] == '#': continue
				x,y=newX,newY
				break
			else:
				print('found dead end', (x,y))
				break
			distance+=1
			if y < 0 or x < 0 or y >= H or x >= W:
				break
			if (x,y) in choices:
				ans.append((x,y,distance))
				break
	c[choice] = ans

answer=[0]
visited=set()
def rec(i,j,distance):
	if (i,j) in visited: return
	if j == H - 1:
		if distance > answer[0]:
			answer[0] = distance
			print(answer[0])
			return
	visited.add((i,j))
	for choice in c[(i,j)]:
		(newX,newY,addDistance)=choice
		rec(newX,newY,distance+addDistance)
	visited.remove((i,j))

rec(1,0,0)
print(answer[0])


# best = [[set() for i in range(W)] for j in range(H)]
#
# best[0][1].add((0, ((1, 0),)))
#
# changes=True
# while changes:
# 	if len(best[-1][-2])>0:
# 		print(max(tb[0] for tb in best[-1][-2]))
# 	changes=False
# 	print(len(best[20][20]), len(best[40][20]), len(best[60][20]))
# 	for j in range(H):
# 		for i in range(W):
# 			for tb in best[j][i]:
# 				for dir in range(4):
# 					dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
# 					newY, newX = j + dy, i + dx
# 					if newY < 0 or newX < 0 or newY >= H or newX >= W or data[j][i] == '#': continue
#
# 					if (newX, newY) not in tb[1]:
# 						newVisited = set(tb[1])
# 						newVisited.add((newX,newY))
# 						newElement=(tb[0] + 1, tuple(sorted(newVisited)))
# 						if newElement in best[newY][newX]: continue
# 						best[newY][newX].add(newElement)
# 						changes=True

# m=map()
# def recM(i,j):
# 	if((i,j,tuple(visited)) in m)
# def rec(i,j,distance):
# 	if (i,j) in visited: return
# 	visited.add((i,j))
# 	for dir in range(4):
# 		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
# 		newY, newX = j + dy, i + dx
# 		if newY>=H:
# 			if distance-1>answer[0]:
# 				print(distance-1)
# 				answer[0]=distance-1
#
# 		if newY<0 or newX<0 or newY>=H or newX>=W or data[j][i]=='#': continue
# 		ch = data[j][i]
# 		# if ch=='>' or ch == '>' or ch == '^' or ch == 'v':
# 		# 	dir2 = ">v<^".find(ch)
# 		# 	if dir != dir2: continue
# 		rec(newX,newY,distance+1)
# 	visited.remove((i,j))
#
# rec(1,0,0)
# print(answer[0]) #6731

#dir=(dir+4)%4
#dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = "rdlu".find(ch.lower())

#data = [[column for column in line] for line in data]
#W,H=len(data[0]), len(data)
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

# answer=[0]
# visited=set()
# def rec(i,j,distance):
# 	if (i,j) in visited: return
# 	visited.add((i,j))
# 	for dir in range(4):
# 		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
# 		newY, newX = j + dy, i + dx
# 		if newY>=H:
# 			if distance-1>answer[0]:
# 				answer[0]=distance-1
#
# 		if newY<0 or newX<0 or newY>=H or newX>=W or data[j][i]=='#': continue
# 		ch = data[j][i]
# 		if ch=='>' or ch == '>' or ch == '^' or ch == 'v':
# 			dir2 = ">v<^".find(ch)
# 			if dir != dir2: continue
# 		rec(newX,newY,distance+1)
# 	visited.remove((i,j))
#
# rec(1,0,0)
# print(answer[0])
