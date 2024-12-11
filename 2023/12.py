#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
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

mem={}
def recM(a, b, aPos, bPos):
	key = (aPos, bPos)
	if key in mem:
		return mem[key]
	output=rec(a, b, aPos, bPos)
	mem[key]=output
	return output
def rec(a, b, aPos, bPos):
	if bPos==len(b):
		for i in range(aPos, len(a)):
			if a[i]=='#':
				return 0
		return 1

	output=0
	for aPosTry in range(aPos, len(a)-b[bPos]):
		for i in range(aPos, aPosTry):
			if a[i]=='#':
				break
		else:
			for i in range(aPosTry, aPosTry+b[bPos]):
				if a[i]=='.':
					break
			else:
				if a[aPosTry+b[bPos]]!='#':
					output+=recM(a, b, aPosTry+b[bPos]+1, bPos+1)
	return output



answer=0
for line in data:
	a,b=line.split(' ')
	b=','.join(b for i in range(5))
	b=b.split(',')
	b=[int(b) for b in b]
	a=[a for a in '?'.join([a for i in range(5)])+'.']
	mem={}
	out=rec(a,b, 0, 0)
	print(out)
	answer+=out
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

# def rec(a, b, pos, bPos, run):
# 	if pos==len(a):
# 		return 1 if bPos == len(b) else 0
# 	elif a[pos]=='?':
# 		left=rec(a, b, pos + 1, bPos, run + 1)
# 		right=0
# 		if run > 0:
# 			if bPos<len(b) and b[bPos]==run:
# 				right = rec(a, b, pos + 1, bPos + 1, 0)
# 			else:
# 				right = 0
# 		else:
# 			right = rec(a, b, pos + 1, bPos, 0)
# 		return left+right
# 	elif a[pos]=='#':
# 		return rec(a, b, pos + 1, bPos, run + 1)
# 	elif a[pos]=='.':
# 		if run > 0:
# 			if bPos<len(b) and b[bPos]==run:
# 				return rec(a, b, pos + 1, bPos + 1, 0)
# 			else:
# 				return 0
# 		return rec(a, b, pos + 1, bPos, 0)
#
# answer=0
# for line in data:
# 	a,b=line.split(' ')
# 	b=b.split(',')
# 	b=[int(b) for b in b]
# 	a=a+'.'
# 	a=[a for a in a]
# 	answer+=rec(a,b, 0, 0, 0)
# print(answer)

# def rec(a, b, pos, bPos, run, aMin, aMax, bRight):
# 	if run > b[bPos] if bPos < len(b) else 0:
# 		return 0
# 	if pos==len(a):
# 		return 1 if bPos == len(b) else 0
# 	elif a[pos]=='?':
# 		left=rec(a, b, pos + 1, bPos, run + 1, aMin, aMax, bRight)
# 		right=0
# 		if run > 0:
# 			if bPos<len(b) and b[bPos]==run:
# 				bPos += 1
# 				br = bRight[bPos] if bPos < len(b) else 0
# 				if br > aMax[pos + 1] or br < aMin[pos + 1]:
# 					right = 0
# 				else:
# 					right = rec(a, b, pos + 1, bPos, 0, aMin, aMax, bRight)
# 			else:
# 				right = 0
# 		else:
# 			br = bRight[bPos] if bPos < len(b) else 0
# 			if br > aMax[pos + 1] or br < aMin[pos + 1]:
# 				right = 0
# 			else:
# 				right = rec(a, b, pos + 1, bPos, 0, aMin, aMax, bRight)
# 		return left+right
# 	elif a[pos]=='#':
# 		return rec(a, b, pos + 1, bPos, run + 1, aMin, aMax, bRight)
# 	elif a[pos]=='.':
# 		if run > 0:
# 			if bPos<len(b) and b[bPos]==run:
# 				bPos+=1
# 				br = bRight[bPos] if bPos < len(b) else 0
# 				if br > aMax[pos + 1] or br < aMin[pos + 1]:
# 					return 0
# 				return rec(a, b, pos + 1, bPos, 0, aMin, aMax, bRight)
# 			else:
# 				return 0
# 		br = bRight[bPos] if bPos < len(b) else 0
# 		if br > aMax[pos + 1] or br < aMin[pos + 1]:
# 			return 0
# 		return rec(a, b, pos + 1, bPos, 0, aMin, aMax, bRight)
#
# answer=0
# for line in data:
# 	a,b=line.split(' ')
# 	b=','.join(b for i in range(5))
# 	b=b.split(',')
# 	b=[int(b) for b in b]
# 	a=[a for a in '?'.join([a for i in range(5)])+'.']
# 	aMin=[sum([a[i]=='#' for i in range(j,len(a))]) for j in range(len(a)+1)]
# 	aMax = [sum([a[i] != '.' for i in range(j, len(a))]) for j in range(len(a)+1)]
# 	bRight = [sum(b[i] for i in range(j, len(b))) for j in range(len(b))]
# 	print(a)
# 	print(aMin)
# 	print(aMax)
# 	print(bRight)
# 	answer+=rec(a,b, 0, 0, 0, aMin, aMax, bRight)
# print(answer)
