#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading, numpy, random
sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Int('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x])))
#import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
#from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
#from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)

nodes={}
edgesOriginal=set()
for line in data:
	a,b=line.split(": ")
	b=b.split(" ")
	for curB in b:
		edgesOriginal.add((a, curB, a, curB)) #there twice because we need the original unmodified edges
		edgesOriginal.add((curB, a, curB, a))

		if a not in nodes:
			nodes[a]=set()
		nodes[a].add(curB)
		if curB not in nodes:
			nodes[curB]=set()
		nodes[curB].add(a)




while True:
	edges = list(edgesOriginal.copy())
	nodeCount = len(nodes)
	while nodeCount!=2:
		joining = random.choice(edges)
		newEdges=[]
		(keep,remove,_,_)=joining
		for (first,second,originalFirst,originalSecond) in edges:
			if first==remove: first=keep
			if second==remove: second=keep
			if first==second: continue
			newEdges.append((first, second, originalFirst, originalSecond))
		nodeCount-=1
		edges=newEdges

	print(len(edges))

	if len(edges)==6:
		break


#with the six directed edges find the size of the two sides

skip=set()
for (first,second,originalFirst,originalSecond) in edges:
	skip.add((originalFirst, originalSecond))
	skip.add((originalSecond, originalFirst))
print(skip)

visited=set()
def ff(cur):
	if cur in visited: return
	visited.add(cur)
	for next in nodes[cur]:
		if (cur,next) in skip: continue
		ff(next)
ff(list(nodes.keys())[0])
print((len(nodes.keys()) - len(visited)) * len(visited))



#brute force solution below was entirely too slow


# visited=set()
# skip=set()
# def ff(cur):
# 	if cur in visited: return
# 	visited.add(cur)
# 	for next in m[cur]:
# 		if (cur,next) in skip: continue
# 		ff(next)
#
# for iPos, i in enumerate(m.keys()):
# 	for iPrime in m[i]:
# 		for jPos, j in enumerate(m.keys()):
# 			for jPrime in m[j]:
# 				if i==j and iPrime==jPrime or i==jPrime and j==iPrime: continue
# 				if (i, iPrime) > (j, jPrime):
# 					continue
# 				for k in m.keys():
# 					for kPrime in m[k]:
# 						if k == j and kPrime == jPrime or k == jPrime and j == kPrime: continue
# 						if k == i and kPrime == iPrime or k == iPrime and i == kPrime: continue
# 						if (j, jPrime) > (k, kPrime):
# 							continue
# 						visited=set()
# 						skip=set([(i,iPrime),(j,jPrime),(k,kPrime),(iPrime,i),(jPrime,j),(kPrime,k)])
# 						ff(list(m.keys())[0])
# 						if len(visited)!=len(m.keys()):
# 							print((len(m.keys())-len(visited))*len(visited))
# 							sys.exit(0)


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

