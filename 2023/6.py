#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

# data1='''
# Time:      7  15   30
# Distance:  9  40  200
# '''.strip('\n').splitlines()
# data2='''
# Time:        48     93     85     95
# Distance:   296   1928   1236   1391
# '''.strip('\n').splitlines()

data1='''
Time:      71530
Distance:  940200
'''.strip('\n').splitlines()
data2='''
Time:        48938595
Distance:   296192812361391
'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]


#for line in data:
# answer=1
# for time,distance in zip(data[0], data[1]):
# 	ways=0
# 	for a in range(time):
# 		if (time-a)*a > distance:
# 			print(a)
# 			ways+=1
# 	answer*=ways
# 	print(time, distance, ways)
# print(answer)
answer=1
for time,distance in zip(data[0], data[1]):
	ways=0
	for a in range(time):
		if (time-a)*a > distance:
			ways+=1
	answer*=ways
	# print(time, distance, ways)
print(answer)

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

