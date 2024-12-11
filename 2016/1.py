#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
R8, R4, R4, R8
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
data = [[column for column in re.findall('[RL][\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]



# dir,x,y=0,0,0
# for line in data[0]:
# 	if line[0]=='R':
# 		dir+=1
# 	if line[0]=='L':
# 		dir-=1
# 	dist=int(line[1:])
# 	dir=(dir+4)%4
# 	dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
# 	x+=dx*dist
# 	y+=dy*dist
# 	#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#
# print(abs(x)+abs(y))


a={}
dir,x,y=0,0,0
for line in data[0]:
	if line[0]=='R':
		dir+=1
	if line[0]=='L':
		dir-=1
	dist=int(line[1:])
	dir=(dir+4)%4
	dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
	for i in range(dist):
		x+=dx
		y+=dy
		if (x,y) in a:
			print(abs(x)+abs(y))
			sys.exit(0)
		a[(x,y)]=True

	#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right


#dir=(dir+4)%4
#dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right

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
