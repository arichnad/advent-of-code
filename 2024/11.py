#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, numpy
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
125 17
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]
data = [[int(column) for column in re.findall('-?[\\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)

# data=data[0]
# for i in range(25):
# 	out = []
# 	for line in data:
# 		s=str(line)
# 		if line==0:
# 			out.append(1)
# 		elif len(s)%2==0:
# 			a,b=s[:len(s)//2],s[len(s)//2:]
# 			out.append(int(a))
# 			out.append(int(b))
# 		else:
# 			out.append(line*2024)
# 	data=out
# 	print(len(data))
# print(len(data))
out={}
for i in data[0]:
	out[i] = 1
data=out

for i in range(75):
	out = {}
	for line in data.keys():
		count=data[line]
		s=str(line)
		if line==0:
			if 1 not in out:
				out[1]=0
			out[1]+=count
		elif len(s)%2==0:
			a,b=int(s[:len(s)//2]),int(s[len(s)//2:])
			if a not in out:
				out[a] = 0
			out[a] += count
			if b not in out:
				out[b]=0
			out[b]+=count
		else:
			if line*2024 not in out:
				out[line*2024]=0
			out[line*2024]+=count
	data=out
	print(i, data, sum(data.values()))
print(sum(data.values()))

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

