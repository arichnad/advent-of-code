#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''.strip('\n').splitlines()

data1='''
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
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

# dir=data.pop(0)
# data.pop(0)
#
# a={}
# for line in data:
# 	b=line.split(' = (')
# 	a[b[0]] = (b[1].split(', ')[0], b[1].split(', ')[1].replace(')',''))
#
# print(data)
# pos='AAA'
# answer=0
# while True:
# 	for ch in dir:
# 		pos=a[pos][0 if ch == 'L' else 1]
# 		answer+=1
# 		if pos == 'ZZZ':
# 			print(answer)
# 			sys.exit(0)

dir=data.pop(0)
data.pop(0)

a={}
for line in data:
	b=line.split(' = (')
	a[b[0]] = (b[1].split(', ')[0], b[1].split(', ')[1].replace(')',''))

startPos=list(filter(lambda a: a.endswith('A'), a.keys()))
isEnd=[]
loopSize=[]
loopStart=[]
for i,pos in enumerate(startPos):
	done=False
	visited={}
	dist=0
	while not done:
		for j, ch in enumerate(dir):
			pos=a[pos][0 if ch == 'L' else 1]
			if pos.endswith('Z'):
				isEnd.append(dist)
			dist+=1
			if (pos, j) in visited:
				loopSize.append(dist - visited[(pos, j)])
				loopStart.append(visited[(pos, j)])
				done=True
				break
			visited[(pos, j)]=dist
print(loopStart, loopSize, isEnd, math.lcm(*loopSize))




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
