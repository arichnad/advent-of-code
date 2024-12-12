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
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
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
visited=set()


# def _(j, i):
# 	if (j, i) in visited: return (0, 0)
# 	visited.add((j, i))
# 	ch=data[j][i]
# 	perim=0
# 	area=1
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			if dx==0 and dy==0 or dx!=0 and dy!=0: continue
# 			newY,newX=j+dy,i+dx
# 			if newY<0 or newX<0 or newY>=H or newX>=W:
# 				perim+=1
# 				continue
# 			if data[newY][newX] != ch:
# 				perim+=1
# 				continue
# 			(p,a) = _(newY, newX)
# 			perim+=p
# 			area+=a
# 	return (perim, area)
# #for line in data:
# answer=0
# for j in range(H):
# 	for i in range(W):
# 		if (j, i) in visited: continue
# 		(p,a)=_(j, i)
# 		answer+=p*a
# 		print(data[j][i], p*a)
# print(answer)

def _(j, i):
	if (j, i) in visited: return (set(), 0)
	visited.add((j, i))
	ch=data[j][i]
	perim=set()
	area=1
	for dy in range(-1, 2):
		for dx in range(-1, 2):
			if dx==0 and dy==0 or dx!=0 and dy!=0: continue
			newY,newX=j+dy,i+dx
			if newY<0 or newX<0 or newY>=H or newX>=W or data[newY][newX] != ch:
				# if dx<0 or dy<0:
				# 	perim.add((newY, newX, -dy, -dx))
				# else:
				perim.add((j, i, dy, dx))
				continue
			(p,a) = _(newY, newX)
			for p in p: perim.add(p)
			area+=a
	return (perim, area)
#for line in data:
answer=0
for j in range(H):
	for i in range(W):
		if (j, i) in visited: continue
		(p,a)=_(j, i)
		total = 0
		for dy in [-1, 1]:
			for j2 in range(-1, H+1):
				on = False
				for i2 in range(-1, W+1):
					x=(j2, i2, dy, 0)
					if x not in p:
						on = False
						continue
					if not on:
						print(x)
						total += 1
					on=True
		for dx in [-1, 1]:
			for i2 in range(-1, W+1):
				on = False
				for j2 in range(-1, H+1):
					x=(j2, i2, 0, dx)
					if x not in p:
						on = False
						continue
					if not on:
						print(x)
						total += 1
					on=True


		answer+=total*a
		print(data[j][i], a, total, total*a)
print(answer) #913094



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

