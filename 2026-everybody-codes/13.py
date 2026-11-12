#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); itertools: product (like permutations with replacement.  repeat=N lets you use the same range multiple times), permutations, combinations, combinations_with_replacement. heapq.heappush(a, 3); d=copy.deepcopy(d)
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


data=data3
# import fileinput # data=[a.strip('\n') for a in fileinput.input()]

# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores


line=0
total=0
while line<len(data):
	(x, hands) = data[line].split(' ')
	line+=1
	(x, dir) = data[line].split(' ')
	line+=1
	(x, cur) = data[line].split(' ')
	line+=1
	(x, move) = data[line].split(' ')
	line+=2
	hands=[int(x) for x in hands.split(':')]
	dir=[1 if x == 'CW' else -1 for x in dir.split(':')]
	cur=[int(x) for x in cur.split(':')]
	move=[int(x) for x in move.split(':')]

	W=len(hands)
	def sign(x): return (x > 0) - (x < 0)
	output=0

	def _():
		global output
		diff = {}
		for i in range(W):
			for j in range(i + 1, W):
				first = cur[i] * hands[j]
				second = cur[j] * hands[i]

				newDiff = second - first

				if newDiff * 2 > hands[i] * hands[j]:
					newDiff -= hands[i] * hands[j]
				if newDiff * 2 < -hands[i] * hands[j]:
					newDiff += hands[i] * hands[j]

				diff[(i, j)] = newDiff
		curSecond = [cur[i] for i in range(W)]
		for i in range(W):
			if move[i] == 0:
				dir[i] = 0
				continue
			curSecond[i] = cur[i] + dir[i]
			cur[i] = (cur[i] + dir[i] + hands[i]) % hands[i]
			move[i] -= 1
		for i in range(W):
			for j in range(i + 1, W):
				first = cur[i] * hands[j]
				second = cur[j] * hands[i]

				newDiff = second - first

				if newDiff * 2 > hands[i] * hands[j]:
					newDiff -= hands[i] * hands[j]
				if newDiff * 2 < -hands[i] * hands[j]:
					newDiff += hands[i] * hands[j]

				oldDiff = diff[(i, j)]

				if sign(oldDiff) != sign(newDiff):
					if oldDiff == 0:
						continue
					elif newDiff == 0:
						pass
					else:
						if dir[i] == dir[j]:
							if hands[i] == hands[j]:
								continue
							if (newDiff < oldDiff) ^ (hands[j] < hands[i]) ^ (dir[i] == 1):
								continue
						else:
							if (newDiff < oldDiff) ^ (dir[j] - dir[i] < 0):
								continue
					# print('#', i, j, oldDiff, newDiff)
					output += 1
				else:
					pass
			# print(' ', i, j, oldDiff, newDiff)


	# print('--------------', round, cur)

	while any(move[i]>0 for i in range(W)):
		allHands = math.lcm(*[hands[i] for i in range(W) if move[i]>0])
		while any(move[i]>0 for i in range(W)) and min(move[i] for i in range(W) if move[i]>0)<allHands:
			_()
		if not any(move[i]>0 for i in range(W)): break
		oldOutput=output
		for i in range(allHands):
			_()
		change=output-oldOutput
		if not any(move[i] > 0 for i in range(W)): break
		runs=min(move[i] for i in range(W) if move[i]>0)//allHands
		output+=change*runs
		move=[move[i]-(runs*allHands if move[i]>0 else 0) for i in range(W)]
		# print('***', runs)

	# print(output)
	total+=output
print(total)

# line=0
# total=0
# while line<len(data):
# 	(x, hands) = data[line].split(' ')
# 	line+=1
# 	(x, dir) = data[line].split(' ')
# 	line+=1
# 	(x, cur) = data[line].split(' ')
# 	line+=1
# 	(x, move) = data[line].split(' ')
# 	line+=2
# 	hands=[int(x) for x in hands.split(':')]
# 	dir=[1 if x == 'CW' else -1 for x in dir.split(':')]
# 	cur=[int(x) for x in cur.split(':')]
# 	move=[int(x) for x in move.split(':')]
#
# 	W=len(hands)
# 	def sign(x): return (x > 0) - (x < 0)
# 	output=0
# 	round=1
#
# 	while sum(move[i] for i in range(W))>0:
# 		diff={}
# 		for i in range(W):
# 			for j in range(i+1, W):
# 				first = cur[i] * hands[j]
# 				second = cur[j] * hands[i]
#
# 				newDiff = second - first
#
# 				if newDiff * 2 > hands[i]*hands[j]:
# 					newDiff -= hands[i] * hands[j]
# 				if newDiff * 2 < -hands[i]*hands[j]:
# 					newDiff += hands[i] * hands[j]
#
# 				diff[(i, j)]=newDiff
# 		curSecond=[cur[i] for i in range(W)]
# 		for i in range(W):
# 			if move[i]==0:
# 				dir[i]=0
# 				continue
# 			curSecond[i]=cur[i]+dir[i]
# 			cur[i]=(cur[i]+dir[i]+hands[i])%hands[i]
# 			move[i]-=1
# 		for i in range(W):
# 			for j in range(i+1, W):
# 				first = cur[i] * hands[j]
# 				second = cur[j] * hands[i]
#
# 				newDiff = second - first
#
# 				if newDiff * 2 > hands[i] * hands[j]:
# 					newDiff -= hands[i] * hands[j]
# 				if newDiff * 2 < -hands[i] * hands[j]:
# 					newDiff += hands[i] * hands[j]
#
# 				oldDiff = diff[(i, j)]
#
# 				if sign(oldDiff) != sign(newDiff):
# 					if oldDiff == 0:
# 						continue
# 					elif newDiff==0:
# 						pass
# 					else:
# 						if dir[i]==dir[j]:
# 							if hands[i]==hands[j]:
# 								continue
# 							if (newDiff < oldDiff) ^ (hands[j] < hands[i]) ^ (dir[i] == 1):
# 								continue
# 						else:
# 							if (newDiff < oldDiff) ^ (dir[j]-dir[i]<0):
# 								continue
# 					# print('#', i, j, oldDiff, newDiff)
# 					output+=1
# 				else:
# 					pass
# 					# print(' ', i, j, oldDiff, newDiff)
# 		# print('--------------', round, cur)
# 		round+=1
# 	print(output)
# 	total+=output
# print(total)






# (x, hands) = data[0].split(' ')
# (x, dir) = data[1].split(' ')
# (x, cur) = data[2].split(' ')
# (x, move) = data[3].split(' ')
# hands=[int(x) for x in hands.split(':')]
# dir=[1 if x == 'CW' else -1 for x in dir.split(':')]
# cur=[int(x) for x in cur.split(':')]
# move=[int(x) for x in move.split(':')]
#
# W=len(hands)
# def sign(x): return (x > 0) - (x < 0)
# output=0
# round=1
# skipZero={}
# # for i in range(W):
# # 	for j in range(i+1, W):
# # 		skipZero[(i, j)]=True
#
# while sum(move[i] for i in range(W))>0:
# 	diff={}
# 	for i in range(W):
# 		for j in range(i+1, W):
# 			first = cur[i] * hands[j]
# 			second = cur[j] * hands[i]
#
# 			diff0 = second - first
#
# 			if diff0 > hands[i]*hands[j]//2:
# 				diff0 -= hands[i]*hands[j]
# 			if diff0 < -hands[i]*hands[j]//2:
# 				diff0 += hands[i]*hands[j]
#
# 			diff[(i, j)]=diff0
# 	curSecond=[cur[i] for i in range(W)]
# 	for i in range(W):
# 		if move[i]==0: continue
# 		curSecond[i]=cur[i]+dir[i]
# 		cur[i]=(cur[i]+dir[i]+hands[i])%hands[i]
# 		move[i]-=1
# 	for i in range(W):
# 		for j in range(i+1, W):
# 			first = cur[i] * hands[j]
# 			second = cur[j] * hands[i]
#
# 			diff0 = second - first
#
# 			if diff0 > hands[i] * hands[j] // 2:
# 				diff0 -= hands[i] * hands[j]
# 			if diff0 < -hands[i] * hands[j] // 2:
# 				diff0 += hands[i] * hands[j]
#
# 			if sign(diff[(i, j)]) != sign(diff0):
# 				if sign(diff[(i, j)]) == 0:
# 					continue
# 				elif sign(diff0)==0:
# 					pass
# 				elif abs(diff[(i, j)]) > hands[i]*hands[j]//4 or abs(diff0) > hands[i]*hands[j]//4:
# 					continue
# 				print('#', i, j, diff[(i, j)], diff0)
# 				output+=1
# 			else:
# 				print(' ', i, j, diff[(i, j)], diff0)
# 	print('--------------', round, cur)
# 	round+=1
# print(output)


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
# 				if newY<0 or newX<0 or newY>=H or newX>=W: continue
# 
# for line in data: print(''.join(line))

# bfs simple queue
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, startY, startX)]
# costs={}
# while len(positions) > 0:
# 	# print(len(positions))
# 	newPositions = []
# 	for (cost, y, x) in sorted(positions): # remove sorted here if it's not needed
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x] == '#': continue
# 		if y==endY and x==endX:
# 			print(cost)
# 			newPositions=[]
# 			break
# 		if (y, x) in costs and cost >= costs[(y, x)]: continue # change >= here to > if you need to analyze ties
# 		costs[(y, x)] = cost
# 
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				# if dx==0 and dy==0: continue
# 				if abs(dx)+abs(dy)!=1: continue
# 				newPositions.append((cost + 1, y+dy, x+dx))
# 	positions=newPositions


# bfs (priority queue)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, startY, startX)]
# costs={}
# while len(positions) > 0:
# 	(cost, y, x) = heapq.heappop(positions)
# 	if y<0 or y>=H or x<0 or x>=W: continue
# 	if data[y][x]=='#': continue
# 	if (y, x) in costs and cost >= costs[(y, x)]: continue
# 	costs[(y, x)] = cost
# 	
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			if (y+dy, x+dx) in costs and cost+1 >= costs[(y+dy, x+dx)]: continue
# 			heapq.heappush(positions, (cost+1, y+dy, x+dx))
# print(costs[(endY, endX)])

# flood fill does NOT work when want a breadth first (minimum cost, that sort of thing)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# visited=set()
# def ff(y, x):
# 	if y<0 or x<0 or y>=H or x>=W: return 0
# 	if data[y][x] == '#' or (y, x) in visited: return 0
# 	visited.add((y, x))
# 
# 	answer=1
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			answer+=ff(y+dy, x+dx)
# 	return answer
# 
# print(ff(startY, startX))

