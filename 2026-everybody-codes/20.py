#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); itertools: product (like permutations with replacement.  repeat=N lets you use the same range multiple times), permutations, combinations, combinations_with_replacement. heapq.heappush(a, 3); d=copy.deepcopy(d)
# from fractions import Fraction; Fraction(1, 3)
# sort list in python3 with a comparator:  v.sort(key=functools.cmp_to_key(lambda a, b: -1 if (a, b) in g else 1 if (b, a) in g else 0))

# you CANNOT copy venv directories.  use this instead:  sudo apt install pypy3-venv && pypy3 -m venv .venv
# OR:  settings -> python -> interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# sudo apt install python3-dev pypy3-dev pypy3-venv libopenblas-dev gfortran libgeos-dev && .venv/bin/pip install sortedcontainers astar z3-solver lmfit sympy shapely
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #SortedList('bat') + 'cat'
# from astar import AStar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3.z3 import * # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); MAYBE s.minimize(sum(params)); print(s.check()); if s.check()==z3.sat: print(int(str(s.model()[x]))) #Int is sometimes slow, but also sometimes Real doesn't give you what you want
# from sympy import * # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# import lmfit # try z3 or sympy first please
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area)
# from testtemplate import *

data1='''

'''.strip('\n').splitlines()
data2='''
'''.strip('\n').splitlines()
data3='''

'''.strip('\n').splitlines()
data4='''

'''.strip('\n').splitlines()

data=data3
# import fileinput # data=[a.strip('\n') for a in fileinput.input()]

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores


# for line in data:


a ={'0':6, '1':2, '2': 5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6, '-':1, '+':2, '=':2, 'A':6, ' ': 0}

b = {
	'0': '1111110',
	'1': '0110000',
	'2': '1101101',
	'3': '1111001',
	'4': '0110011',
	'5': '1011011',
	'6': '1011111',
	'7': '1110000',
	'8': '1111111',
	'9': '1111011',
	'A': '1110111',
}
c={}
for i in b.keys():
	c[b[i]]=i

answer=0
def _(left, right, leftOp, rightOp):
	try:
		left=[''.join([c[''.join(i)] for i in j]) for j in left]
		right=[''.join([c[''.join(i)] for i in j]) for j in right]
	except KeyError:
		return False
	left=[int(l, 11) for l in left]
	right=[int(r, 11) for r in right]
	x,y=left,right
	left=left[0]-left[1] if leftOp=='-' else sum(left)
	right=right[0]-right[1] if rightOp=='-' else sum(right)
	# print(x, y, left, right)
	# if left==right:
	# 	print(x[0], leftOp, x[1], '=', y[0], rightOp, y[1])
	return left==right

def __(left, right, leftOp, rightOp):
	total=(len(left[0])+len(left[1])+len(right[0])+len(right[1]))*7 + 2
	leftOriginal=copy.deepcopy(left)
	rightOriginal=copy.deepcopy(right)
	leftOpOriginal,rightOpOriginal=leftOp,rightOp
	for a in range(total):
		for b in range(total):
			if a==b: continue
			left=copy.deepcopy(leftOriginal)
			right=copy.deepcopy(rightOriginal)
			leftOp,rightOp=leftOpOriginal,rightOpOriginal

			seg=a%7
			a2=a//7
			if a2<len(left[0]):
				side,operand=0,0
				letter=a2
			elif a2<len(left[0])+len(left[1]):
				side,operand=0,1
				letter=a2-(len(left[0]))
			elif a2<len(left[0])+len(left[1])+len(right[0]):
				side,operand=1,0
				letter=a2-(len(left[0])+len(left[1]))
			elif a2<len(left[0])+len(left[1])+len(right[0])+len(right[1]):
				side,operand=1,1
				letter=a2-(len(left[0])+len(left[1])+len(right[0]))
			else:
				side=2

			if side==0:
				if left[operand][letter][seg]=='0': continue
				left[operand][letter][seg]='0'
			elif side==1:
				if right[operand][letter][seg]=='0': continue
				right[operand][letter][seg]='0'
			else:
				if seg==0:
					if leftOp=='-': continue
					leftOp='-'
				else:
					if rightOp=='-': continue
					rightOp='-'


			seg=b%7
			b2=b//7
			if b2<len(left[0]):
				side,operand=0,0
				letter=b2
			elif b2<len(left[0])+len(left[1]):
				side,operand=0,1
				letter=b2-(len(left[0]))
			elif b2<len(left[0])+len(left[1])+len(right[0]):
				side,operand=1,0
				letter=b2-(len(left[0])+len(left[1]))
			elif b2<len(left[0])+len(left[1])+len(right[0])+len(right[1]):
				side,operand=1,1
				letter=b2-(len(left[0])+len(left[1])+len(right[0]))
			else:
				side=2

			if side==0:
				if left[operand][letter][seg]=='1': continue
				left[operand][letter][seg]='1'
			elif side==1:
				if right[operand][letter][seg]=='1': continue
				right[operand][letter][seg]='1'
			else:
				if seg==0:
					if leftOp=='+': continue
					leftOp='+'
				else:
					if rightOp=='+': continue
					rightOp='+'

			if _(left, right, leftOp, rightOp): return True
	return False

for line in data:
	x=line
	line=line.replace(' = ', '=')
	left,right=line.split('=')
	left=left.split(' ')
	right=right.split(' ')
	leftOp=left.pop(1)
	rightOp=right.pop(1)

	left=[[[k for k in b[i]] for i in j] for j in left]
	right=[[[k for k in b[i]] for i in j] for j in right]

	if _(left, right, leftOp, rightOp):
		answer+=(sum([a[x] for x in x]))
		continue
	if __(left, right, leftOp, rightOp):
		answer+=(sum([a[x] for x in x]))
		continue




alph=[c for c in '0123456789A']
out=''
while answer>0:
	out+=alph[answer%11]
	answer//=11
print(''.join(reversed(out)))


# a ={'0':6, '1':2, '2': 5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6, '-':1, '+':2, '=':2, 'A':6, ' ': 0}
# answer=0
#
# for line in data:
# 	x=line
# 	line=line.replace(' = ', '=')
# 	left,right=line.split('=')
# 	left=re.split('[ ]', left)
# 	right=re.split('[ ]', right)
# 	print(left, right)
# 	leftOp=left.pop(1)
# 	rightOp=right.pop(1)
# 	left=[int(l, 11) for l in left]
# 	right=[int(r, 11) for r in right]
# 	left=left[0]-left[1] if leftOp=='-' else sum(left)
# 	right=right[0]-right[1] if rightOp=='-' else sum(right)
# 	print(left, right, leftOp, rightOp)
# 	if left!=right: continue
# 	answer+=(sum([a[x] for x in x]))
#
# alph=[c for c in '0123456789A']
# while answer>0:
# 	print(alph[answer%11])
# 	answer//=11



# dir = (dir+4)%4
# dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] # clockwise, starting right
# dir = 1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 # clockwise, starting right
# dir = 'rdlu'.find(d.lower()) # clockwise, starting right
# dir = ['right', 'down', 'left', 'up'].index(d.lower()) # clockwise, starting right
# dir = '>v<^'.find(d.lower()) # clockwise, starting right

# data = [[column for column in line] for line in data]
# for j in range(H):
# 	for i in range(W):
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				# if dx==0 and dy==0: continue
# 				if abs(dx)+abs(dy)!=1: continue
#
# 				newY,newX=j+dy,i+dx
# 				if newY<0 or newY>=H or newX<0 or newX>=W: continue
#
# for line in data: print(''.join(line))

# bfs simple queue (sorting slows things down some, you can remove sort if costs go up by the same every round)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, (startY, startX))]
# endPoint = (endY, endX)
# costs={}
# while len(positions) > 0:
# 	# print(len(positions))
# 	newPositions = []
# 	for (cost, point) in sorted(positions): # remove sorted here if cost goes up by the same every round
# 		(y, x) = point
#
# 		costKey = point
# 		if costKey in costs and cost >= costs[costKey]: continue # change >= here to > if you need to analyze ties
# 		costs[costKey] = cost
#
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				# if dx==0 and dy==0: continue
# 				if abs(dx)+abs(dy) != 1: continue
# 				ny,nx = y+dy,x+dx
# 				if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
# 				if data[ny][nx] == '#': continue
#
# 				newCost = cost + 1
# 				newPoint = (ny, nx)
#
# 				if newPoint == endPoint:
# 					print(newCost)
# 					sys.exit(0)
#
# 				newPositions.append((newCost, newPoint))
# 	positions=newPositions
# print(costs[(endY, endX)])


# bfs with a heap (fast sorting)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, (startY, startX))]
# endPoint = (endY, endX)
# costs={}
# while len(positions) > 0:
# 	(cost, point) = heapq.heappop(positions)
# 	(y, x) = point
#
# 	costKey = point
# 	if costKey in costs and cost >= costs[costKey]:
# 		continue
# 	costs[costKey] = cost
#
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			ny,nx = y+dy,x+dx
# 			if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
# 			if data[ny][nx] == '#': continue
#
# 			newCost = cost+1
# 			newPoint = (ny, nx)
#
# 			if newPoint==endPoint:
# 				print(newCost)
# 				sys.exit(0)
#
# 			costKey = newPoint
# 			if costKey in costs and newCost >= costs[costKey]: continue
#
# 			heapq.heappush(positions, (newCost, newPoint))
# print(costs[(endY, endX)])

# flood fill does NOT work when want a breadth first (minimum cost, that sort of thing)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# visited=set()
# def ff(point):
# 	(y, x) = point
# 	if (y, x) in visited: return 0
# 	visited.add((y, x))
#
# 	answer=1
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			ny,nx = y+dy,x+dx
# 			if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
# 			if data[ny][nx] == '#': continue
#
# 			newPoint = (ny, nx)
# 			answer+=ff(newPoint)
# 	return answer
#
# print(ff((startY, startX), ))

