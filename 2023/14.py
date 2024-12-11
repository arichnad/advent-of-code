#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
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

all={}
ans=[]
H,W=len(data),len(data[0])
for run in range(145):
	for dir in range(4):
		# print('len', len(all))
		#for line in data:

		dx, dy = [(0, -1), (-1, 0), (0, 1), (1, 0)][dir]
		for j in range(H) if dy<0 else reversed(range(H)):
			for i in range(W) if dx<0 else reversed(range(W)):
				if data[j][i]=='O':
					data[j][i]='.'
					x,y=i,j
					while True:
						if y+dy<0 or x+dx<0 or y+dy>=H or x+dx>=W or data[y+dy][x+dx]!='.':
							data[y][x]='O'
							break
						x+=dx
						y+=dy

	answer = 0
	for j, row in enumerate(data):
		for col in row:
			if col == 'O':
				answer += H - j
	# print(run+1, answer)
	ans.append(answer)
	t = tuple(tuple(row) for row in data)
	# if t in all:
	# 	break
	all[t] = True
print(ans[(1000000000-122)%(144-122)+122-1])
# for j, row in enumerate(data):
# 	print(''.join(row))






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

# #for line in data:
# H,W=len(data),len(data[0])
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='O':
# 			data[j][i]='.'
# 			k=j
# 			while True:
# 				if k==0:
# 					data[k][i]='O'
# 					break
# 				if data[k-1][i]!='.':
# 					data[k][i]='O'
# 					break
# 				k-=1
#
# answer=0
# for j,row in enumerate(data):
# 	for col in row:
# 		if col=='O':
# 			answer+=H-j
# 	print(''.join(row))
# print(answer)
