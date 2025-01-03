#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2
print(data)
W,H=len(data[0]),len(data)
sys.setrecursionlimit(100000)
#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()


#for line in data:

light=set()

def add(x, y, dir):
	if x<0 or y<0 or x==W or y==H or (x, y, dir) in light:
		return
	light.add((x, y, dir))
	dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
	if data[y][x] == '.':
		add(x+dx, y+dy, dir)
	elif data[y][x] == '\\':
		dx,dy=dy,dx
		add(x+dx, y+dy, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
	elif data[y][x] == "/":
		dx,dy=-dy,-dx
		add(x+dx, y+dy, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
	elif data[y][x] == '-':
		if dy==0:
			add(x+dx, y+dy, dir)
		else:
			dy=0
			dx = -1
			add(x + dx, y, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
			dx = 1
			add(x + dx, y, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
	elif data[y][x] == '|':
		if dx==0:
			add(x+dx, y+dy, dir)
		else:
			dx=0
			dy = -1
			add(x, y + dy, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
			dy = 1
			add(x, y + dy, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)

def getAns():
	ans = 0
	for j in range(H):
		for i in range(W):
			for dir in range(4):
				if (i, j, dir) in light:
					ans += 1
					break
	return ans
best=0
for x in range(W):
	y=0
	light=set()
	add(x, y, 1)
	if getAns()>best:
		best=getAns()
	y=H-1
	light=set()
	add(x, y, 3)
	if getAns()>best:
		best=getAns()
for y in range(H):
	x=0
	light = set()
	add(x, y, 0)
	if getAns()>best:
		best=getAns()
	x=W-1
	light = set()
	add(x, y, 2)
	if getAns()>best:
		best=getAns()

for j in range(H):
	for i in range(W):
		for dir in range(4):
			if (i,j,dir) in light:
				print(">v<^"[dir],end='')
				break
		else:
			print('.',end='')
	print()
print()

print(best) #11050 11575


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

# light=set()
#
# def add(x, y, dir):
# 	print(x, y, dir)
# 	if x<0 or y<0 or x==W or y==H or (x, y, dir) in light:
# 		return
# 	light.add((x, y, dir))
# 	dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
# 	if data[y][x] == '.':
# 		add(x+dx, y+dy, dir)
# 	elif data[y][x] == '\\':
# 		dx,dy=dy,dx
# 		add(x+dx, y+dy, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
# 	elif data[y][x] == "/":
# 		dx,dy=-dy,-dx
# 		add(x+dx, y+dy, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
# 	elif data[y][x] == '-':
# 		if dy==0:
# 			add(x+dx, y+dy, dir)
# 		else:
# 			dy=0
# 			dx = -1
# 			add(x + dx, y, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
# 			dx = 1
# 			add(x + dx, y, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
# 	elif data[y][x] == '|':
# 		if dx==0:
# 			add(x+dx, y+dy, dir)
# 		else:
# 			dx=0
# 			dy = -1
# 			add(x, y + dy, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
# 			dy = 1
# 			add(x, y + dy, 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2)
#
#
# add(0, 0, 0)
#
# for j in range(H):
# 	for i in range(W):
# 		for dir in range(4):
# 			if (i,j,dir) in light:
# 				print(">v<^"[dir],end='')
# 				break
# 		else:
# 			print('.',end='')
# 	print()
# print()
# ans=0
# for j in range(H):
# 	for i in range(W):
# 		for dir in range(4):
# 			if (i,j,dir) in light:
# 				ans+=1
# 				break
# print(ans)
