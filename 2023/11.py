#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
W=len(data[0])

expandJ=[]
for j, row in enumerate(data):
	for col in row:
		if col=='#': break
	else:
		expandJ.append(j)


H=len(data)

expandI=[]
for i in range(W):
	for j in range(H):
		ch=data[j][i]
		if ch=='#': break
	else:
		expandI.append(i)

W=len(data[0])

num=0
for line in data:
	for col in line:
		if col == '#': num+=1

aI, aJ = [], []
for j in range(H):
	for i in range(W):
		if data[j][i]=='#':
			aJ.append(j)
			aI.append(i)

answer=0

for a in range(num):
	for b in range(a+1,num):
		output=0
		for j in range(min(aJ[a], aJ[b]), max(aJ[a], aJ[b])):
			if j in expandJ:
				output+=1000000-1
		for i in range(min(aI[a], aI[b]), max(aI[a], aI[b])):
			if i in expandI:
				output+=1000000-1
		answer+=abs(aJ[a]-aJ[b])+abs(aI[a]-aI[b])+output
print(answer) #9918828


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

# expand=[]
# for j, row in enumerate(data):
# 	for col in row:
# 		if col=='#': break
# 	else:
# 		expand.append(j)
#
# pos=0
# for j in expand:
# 	data.insert(j+pos, ['.']*W)
# 	pos+=1
#
# H=len(data)
#
# expand=[]
# for i in range(W):
# 	for j in range(H):
# 		ch=data[j][i]
# 		if ch=='#': break
# 	else:
# 		expand.append(i)
# print(expand)
# pos=0
# for i in expand:
# 	for j in range(H):
# 		data[j].insert(i+pos, '.')
# 	pos+=1
# W=len(data[0])
#
# num=0
# for line in data:
# 	for col in line:
# 		if col == '#': num+=1
#
# answer=0
#
# for a in range(num):
# 	for b in range(a+1,num):
# 		count=0
# 		aJ, bJ, aI, bI = None, None, None, None
# 		for j in range(H):
# 			for i in range(W):
# 				if data[j][i]=='#':
#
# 					if count == a:
# 						aJ = j
# 						aI = i
# 					if count==b:
# 						bJ=j
# 						bI=i
# 					count += 1
# 		answer+=abs(aJ-bJ)+abs(aI-bI)
# print(answer)
