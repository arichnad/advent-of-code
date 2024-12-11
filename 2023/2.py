#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
# data = [[column for column in re.findall('[\d]+|blue|red|green', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#
# ans = 0
# i=1
# for line in data:
# 	beg,n = line.split(": ")
# 	handfuls=n.split("; ")
# 	pos=True
# 	for handful in handfuls:
# 		for thing in handful.split(", "):
# 			num,color = thing.split(" ")
# 			num=int(num)
# 			if color == 'red' and num > 12:
# 				pos=False
# 			if color == 'green' and num > 13:
# 				pos=False
# 			if color == 'blue' and num > 14:
# 				pos=False
# 	if pos: ans+=i
# 	i+=1
# print(ans)
ans = 0
i=1
for line in data:
	beg,n = line.split(": ")
	handfuls=n.split("; ")
	pos=True
	min={'red': 0, 'blue': 0, 'green': 0}
	for handful in handfuls:
		for thing in handful.split(", "):
			num,color = thing.split(" ")
			num=int(num)
			m = min[color]
			if num>m: min[color]=num

	ans+=min['red']*min['blue']*min['green']
	i+=1
print(ans)

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

