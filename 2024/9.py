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
2333133121414131402
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[int(column) for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)

# data = data[0]
# id=0
# output=[]
# while True:
# 	a=data.pop(0)
# 	output.extend([id] * a)
#
# 	id+=1
# 	if len(data)==0:
# 		break
#
# 	f=data.pop(0)
# 	output.extend([None] * f)
#
# 	if len(data)==0:
# 		break
#
# answer=[]
# while len(output)>0:
# 	start=output.pop(0)
# 	if start is None:
# 		while len(output)>0:
# 			x=output.pop()
# 			if x is not None:
# 				answer.append(x)
# 				break
# 	else:
# 		answer.append(start)
#
# a2=0
# for i, a in enumerate(answer):
# 	a2+=a*i
# print(a2)
data = data[0]
id=0
output=[]
while True:
	a=data.pop(0)
	output.append((id, a))

	id+=1
	if len(data)==0:
		break

	f=data.pop(0)
	output.append((None, f))

	if len(data)==0:
		break

answer=[]
for id in reversed(range(id)):
	for j, (i, length) in enumerate(output):
		if i==id:
			for k, (i, length2) in enumerate(output[0:j]):
				if i is None and length2>=length:
					if j+1<len(output) and output[j+1][0] is None:
						output[j+1]=(output[j+1][0], output[j+1][1]+length)
						output.pop(j)
					else:
						output[j]=(None, length)
					if length2==length:
						output[k]=(id, length)
					else:
						output[k]=(id, length)
						if k+1<len(output) and output[k+1][0] is None:
							output[k+1][1]+=length2-length
						else:
							output.insert(k+1, (None, length2-length))
					break
			break

a2=0
pos=0
for (a, length) in output:
	if a is None:
		pos+=length
		continue
	for k in range(length):
		a2+=a*pos
		pos+=1
print(a2)

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

