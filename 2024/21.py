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
029A
980A
179A
456A
379A
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()


def d(pos0, pos1, bad):
	if pos0==pos1: return set('A')
	dx,dy=pos1[0]-pos0[0],pos1[1]-pos0[1]
	if dx!=0: dx//=abs(dx)
	if dy!=0: dy//=abs(dy)
	a,b = None,None
	if dx != 0:
		if (pos0[0] + dx, pos0[1]) != bad:
			first = '<' if dx < 0 else '>'
			aIn=d((pos0[0] + dx, pos0[1]), pos1, bad)
			a=set()
			for x in aIn: a.add(first+x)
	if dy != 0:
		if (pos0[0], pos0[1] + dy) != bad:
			first = '^' if dy < 0 else 'v'
			bIn=d((pos0[0], pos0[1] + dy), pos1, bad)
			b = set()
			for x in bIn: b.add(first + x)
	if a is None: return b
	if b is None: return a
	return a|b


def p(ch):
	if ch == '7': return (0, 0)
	if ch == '8': return (1, 0)
	if ch == '9': return (2, 0)

	if ch == '4': return (0, 1)
	if ch == '5': return (1, 1)
	if ch == '6': return (2, 1)

	if ch == '1': return (0, 2)
	if ch == '2': return (1, 2)
	if ch == '3': return (2, 2)

	if ch == '0': return (1, 3)
	if ch == 'A': return (2, 3)


def q(ch):
	if ch == '^': return (1, 0)
	if ch == 'A': return (2, 0)

	if ch == '<': return (0, 1)
	if ch == 'v': return (1, 1)
	if ch == '>': return (2, 1)

# answer=0
# R=2
# for line in data:
# 	pos=(2,3)
# 	a=set()
# 	for ch in line:
# 		add=d(pos, p(ch), (0, 3))
# 		pos = p(ch)
# 		if len(a)==0:
# 			a=add
# 		else:
# 			aIn = a
# 			a = set()
# 			for x in aIn:
# 				for y in add: a.add(x+y)
# 	out=a
# 	for r in range(R):
# 		outIn=out
# 		out=set()
# 		for xx in outIn:
# 			pos=(2, 0)
# 			a=set()
# 			for ch in xx:
# 				add=d(pos, q(ch), (0, 0))
# 				pos = q(ch)
# 				if len(a) == 0:
# 					a = add
# 				else:
# 					aIn = a
# 					a = set()
# 					for x in aIn:
# 						for y in add: a.add(x + y)
# 			out|=a
#
# 	m, n = None, None
# 	for xx in out:
# 		if m is None or len(xx) < m:
# 			m, n = len(xx), xx
# 	print(line, m, int(line.replace('A','')))
# 	answer += m * int(line.replace('A',''))
#
# print(answer)
R=25

firstMapping={}
for pos0 in ((1, 0), (2, 0), (0, 1), (1, 1), (2, 1)):
	for pos1 in ((1, 0), (2, 0), (0, 1), (1, 1), (2, 1)):
		add=d(pos0, pos1, (0, 0))
		minLength = None
		for x in add:
			if minLength is None or len(x)<minLength: minLength=len(x)
		out=set()
		for x in add:
			if len(x)==minLength:
				out.add(x)
		firstMapping[(pos0, pos1)] = (minLength, out)


lastMapping=firstMapping
for r in range(R - 1):
	mapping={}
	for pos0 in ((1, 0), (2, 0), (0, 1), (1, 1), (2, 1)):
		for pos1 in ((1, 0), (2, 0), (0, 1), (1, 1), (2, 1)):
			minLength = None
			for x in firstMapping[(pos0, pos1)][1]:
				pos = (2, 0)
				aLength=0
				for ch in x:
					(length, _)=lastMapping[(pos, q(ch))]
					pos=q(ch)
					aLength+=length

				if minLength is None or aLength<minLength:
					minLength=aLength
			mapping[(pos0, pos1)] = (minLength, None)
	lastMapping=mapping


answer=0
for line in data:
	pos=(2,3)
	a=set()
	for ch in line:
		add=d(pos, p(ch), (0, 3))
		pos = p(ch)
		if len(a)==0:
			a=add
		else:
			aIn = a
			a = set()
			for x in aIn:
				for y in add: a.add(x+y)
	minLength=None
	for xx in a:
		pos=(2, 0)
		a=0
		for ch in xx:
			(x, add)=mapping[(pos, q(ch))]
			a+=x
			pos = q(ch)

		if minLength is None or a < minLength:
			minLength=a

	print(line, minLength)
	answer += minLength * int(line.replace('A',''))

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

# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startX,startY=i,j
# 		if data[j][i]=='E': endX,endY=i,j
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
