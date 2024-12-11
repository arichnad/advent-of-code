#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
data = [[column for column in line.split(' ')] for line in data]
#data = [[column for column in line] for line in data]

# def getValue(char):
# 	return '23456789TJQKA'.find(char)
#
# def getValues(a):
# 	for i in range(len(a[0])):
# 		if getValue(a[0][i]) != getValue(a[1][i]):
# 			return 1 if getValue(a[0][i]) > getValue(a[1][i]) else -1
# 	return 0
#
# def compare(a, b):
# 	a=(a[0],b[0])
# 	count=[{},{}]
# 	highestCount=[0,0]
# 	secondHighestCount=[0,0]
# 	for v in range(2):
# 		for i in sorted(a[v]):
# 			count[v][i]=(count[v][i] if i in count[v] else 0)+1
# 		counts=list(reversed(sorted(count[v].values())))
# 		highestCount[v]=counts[0]
# 		secondHighestCount[v]=counts[1] if len(counts)>1 else 0
# 	if highestCount[0] == 5 and highestCount[1] == 5:
# 		return getValues(a)
# 	if highestCount[0] == 5:
# 		return 1
# 	if highestCount[1] == 5:
# 		return -1
#
# 	if highestCount[0] == 4 and highestCount[1] == 4:
# 		return getValues(a)
# 	if highestCount[0] == 4:
# 		return 1
# 	if highestCount[1] == 4:
# 		return -1
#
# 	if highestCount[0] == 3 and secondHighestCount[0] == 2 \
# 		and highestCount[1] == 3 and secondHighestCount[1] == 2:
# 		return getValues(a)
# 	if highestCount[0] == 3 and secondHighestCount[0] == 2:
# 		return 1
# 	if highestCount[1] == 3 and secondHighestCount[1] == 2:
# 		return -1
#
# 	if highestCount[0] == 3 and highestCount[1] == 3:
# 		return getValues(a)
# 	if highestCount[0] == 3:
# 		return 1
# 	if highestCount[1] == 3:
# 		return -1
#
# 	if highestCount[0] == 2 and secondHighestCount[0] == 2 \
# 		and highestCount[1] == 2 and secondHighestCount[1] == 2:
# 		return getValues(a)
# 	if highestCount[0] == 2 and secondHighestCount[0] == 2:
# 		return 1
# 	if highestCount[1] == 2 and secondHighestCount[1] == 2:
# 		return -1
#
# 	if highestCount[0] == 2 and highestCount[1] == 2:
# 		return getValues(a)
# 	if highestCount[0] == 2:
# 		return 1
# 	if highestCount[1] == 2:
# 		return -1
#
# 	return getValues(a)
#
# data = sorted(data, key=functools.cmp_to_key(compare))
# print([''.join(sorted(row[0])) for row in data])
# answer=0
# for i,row in enumerate(data):
# 	answer+=(i+1)*int(row[1])
# print(answer)
def getValue(char):
	return 'J23456789TQKA'.find(char)

def getValues(a):
	for i in range(len(a[0])):
		if getValue(a[0][i]) != getValue(a[1][i]):
			return 1 if getValue(a[0][i]) > getValue(a[1][i]) else -1
	return 0

def compare(a, b):
	a=(a[0],b[0])
	aCount=(a[0].count('J'), a[1].count('J'))
	aReplaced=(a[0].replace('J',''),a[1].replace('J',''))
	count=[{},{}]
	highestCount=[0,0]
	secondHighestCount=[0,0]
	for v in range(2):
		for i in sorted(aReplaced[v]):
			count[v][i]=(count[v][i] if i in count[v] else 0)+1
		counts=list(reversed(sorted(count[v].values())))
		highestCount[v]=(counts[0] if len(counts)>0 else 0) + aCount[v]
		secondHighestCount[v]=counts[1] if len(counts)>1 else 0

	if highestCount[0] == 5 and highestCount[1] == 5:
		return getValues(a)
	if highestCount[0] == 5:
		return 1
	if highestCount[1] == 5:
		return -1

	if highestCount[0] == 4 and highestCount[1] == 4:
		return getValues(a)
	if highestCount[0] == 4:
		return 1
	if highestCount[1] == 4:
		return -1

	if highestCount[0] == 3 and secondHighestCount[0] == 2 \
		and highestCount[1] == 3 and secondHighestCount[1] == 2:
		return getValues(a)
	if highestCount[0] == 3 and secondHighestCount[0] == 2:
		return 1
	if highestCount[1] == 3 and secondHighestCount[1] == 2:
		return -1

	if highestCount[0] == 3 and highestCount[1] == 3:
		return getValues(a)
	if highestCount[0] == 3:
		return 1
	if highestCount[1] == 3:
		return -1

	if highestCount[0] == 2 and secondHighestCount[0] == 2 \
		and highestCount[1] == 2 and secondHighestCount[1] == 2:
		return getValues(a)
	if highestCount[0] == 2 and secondHighestCount[0] == 2:
		return 1
	if highestCount[1] == 2 and secondHighestCount[1] == 2:
		return -1

	if highestCount[0] == 2 and highestCount[1] == 2:
		return getValues(a)
	if highestCount[0] == 2:
		return 1
	if highestCount[1] == 2:
		return -1

	return getValues(a)

data = sorted(data, key=functools.cmp_to_key(compare))
print([''.join(sorted(row[0])) for row in data])
answer=0
for i,row in enumerate(data):
	answer+=(i+1)*int(row[1])
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

