#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#for line in data:

W=len(data[0])
H=len(data)

y=0

for i in range(W):
	if data[y][i]=='.':
		x=i
		break

b=[[[] for i in range(W)] for j in range(H)]

for j in range(H):
	for i in range(W):
		if data[j][i]=='>':
			b[j][i].append((1,0))
			data[j][i]='.'
		if data[j][i]=='<':
			b[j][i].append((-1,0))
			data[j][i]='.'
		if data[j][i]=='v':
			b[j][i].append((0,1))
			data[j][i]='.'
		if data[j][i]=='^':
			b[j][i].append((0,-1))
			data[j][i]='.'

cur=set([(x,y,0)])
for n in range(18000):
	new=set()

	bNew=[[[] for i in range(W)] for j in range(H)]
	for j in range(H):
		for i in range(W):
			for (dx,dy) in b[j][i]:
				newX,newY=i+dx,j+dy
				if data[newY][newX]=='#':
					if dx==1: newX=1
					if dx==-1: newX=W-2
					if dy==1: newY=1
					if dy==-1: newY=H-2
				bNew[newY][newX].append((dx,dy))
	b=bNew
				
			
	for (x,y,times) in cur:
		for dy in range(-1,2):
			for dx in range(-1,2):
				if dx!=0 and dy!=0: continue
				j=y+dy
				i=x+dx
				if j<0 or j>=H or i<0 or i>=W: continue
				if data[j][i]!='.' or len(b[j][i])!=0: continue
				if j==0:
					if times==1:
						times=2
				if j==H-1:
					#pt 1
					#print(n+1)
					#sys.exit(0)
					if times==0:
						times=1
					if times==2:
						print(n+1)
						sys.exit(0)
				new.add((i,j,times))
	cur=new

