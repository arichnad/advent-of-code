#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, numpy
#sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
#import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
#from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
#from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
W,H=len(data[0]),len(data)





# answer=0
# seen=set()
# seen.add((y, x))
# answer+=1
# while True:
# 	newY, newX = y + dy, x + dx
# 	print(newY, newX)
# 	if newY < 0 or newX < 0 or newY >= H or newX >= W: break
# 	if data[newY][newX]=='#':
# 		dir = (dir+1)%4
# 		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]  # clockwise, starting right
# 		continue
# 	if (newY, newX) not in seen:
# 		seen.add((newY, newX))
# 		answer += 1
# 	x,y=newX, newY

# for j in range(H):
# 	for i in range(W):
# 		d=data[j][i]
# 		if d!='.' and d!='#':
# 			dir = '>v<^'.find(d.lower()) #clockwise, starting right
# 			dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
# 			y=j
# 			x=i
#
# answer=0
# seen= {}
# seen[(y, x, dir)]=0
# count=0
# while True:
# 	newY, newX = y + dy, x + dx
# 	if newY < 0 or newX < 0 or newY >= H or newX >= W: break
# 	if data[newY][newX]=='#':
# 		dir = (dir+1)%4
# 		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]  # clockwise, starting right
# 		continue
# 	count = count + 1
# 	if (newY, newX, dir) not in seen:
# 		seen[(newY, newX, dir)] = count
# 	x,y=newX, newY
# seenOriginal = seen
# for j in range(H):
# 	for i in range(W):
# 		d=data[j][i]
# 		if d!='.': continue
# 		found=None
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				if dx==0 and dy==0 or dx!=0 and dy!=0: continue
# 				newY, newX = j + dy, i + dx
# 				if newY < 0 or newX < 0 or newY >= H or newX >= W: continue
# 				dy=-dy
# 				dx=-dx
# 				dir = 1 if dy == 1 else 3 if dx == 0 else 0 if dx == 1 else 2  # clockwise, starting right
# 				if (newY, newX, dir) not in seen:
# 					continue
# 				count = seen[(newY, newX, dir)]
# 				# print((newY, newX, dir))
# 				# dir = (dir+1)%4
# 				x, y = newX, newY
# 				print('###', (newY, newX, dir))
# 				data[j][i]='#'
# 				seen = seenOriginal.copy()
# 				while True:
# 					newY, newX = y + dy, x + dx
# 					if newY < 0 or newX < 0 or newY >= H or newX >= W: break
# 					if data[newY][newX] == '#':
# 						dir = (dir + 1) % 4
# 						dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]  # clockwise, starting right
# 						continue
# 					# print('   ', (newY, newX, dir))
# 					if (newY, newX, dir) in seen:
# 						found = seen[(newY, newX, dir)] <= count
# 						break
# 					seen[(newY, newX, dir)] = count
# 					x, y = newX, newY
# 				data[j][i]='.'
# 				if found: break
# 			if found: break
# 		if found:
# 			print(j, i)
# 			answer+=1
#
# print(answer) #1809 1854

for j in range(H):
	for i in range(W):
		d=data[j][i]
		if d!='.' and d!='#':
			dir = '>v<^'.find(d.lower()) #clockwise, starting right
			dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
			y=j
			x=i

xStart,yStart,dirStart = x, y, dir
answer=0

for j in range(H):
	for i in range(W):
		d=data[j][i]
		if d!='.': continue
		data[j][i]='#'
		seen = set()
		x,y,dir = xStart,yStart,dirStart
		dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
		seen.add((y, x, dir))
		while True:
			newY, newX = y + dy, x + dx
			if newY < 0 or newX < 0 or newY >= H or newX >= W: break
			if data[newY][newX] == '#':
				dir = (dir + 1) % 4
				dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]  # clockwise, starting right
				continue
			if (newY, newX, dir) in seen:
				answer += 1
				break
			seen.add((newY, newX, dir))
			x, y = newX, newY
		data[j][i]='.'

print(answer)


# 1 7
# 3 4
#dir = (dir+4)%4
#dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir = 1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = 'rdlu'.find(d.lower()) #clockwise, starting right
#dir = ['right', 'down', 'left', 'up'].index(d.lower()) #clockwise, starting right
#dir = '>v<^'.find(d.lower()) #clockwise, starting right

#data = [[column for column in line] for line in data]

#for line in data: print(''.join(line))

