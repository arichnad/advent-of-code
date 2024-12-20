#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
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

data.append('')
out=[]
output=0
for line in data:
	if line=='':
		H,W=len(out),len(out[0])
		for j in range(H-1):
			bad=0
			for dy in range(H-1):
				for i in range(W):
					if j-dy>=0 and j+dy+1<H and out[j-dy][i]!=out[j+dy+1][i]:
						bad+=1
			if bad == 1:
				output+=(j+1)*100
		print()
		for i in range(W-1):
			bad=0
			for dx in range(W-1):
				for j in range(H):
					if i-dx>=0 and i+dx+1<W and out[j][i-dx]!=out[j][i+dx+1]:
						bad+=1
			if bad == 1:
				output+=i+1
		out = []
	else:
		out.append([col for col in line])
print(output)



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

# data.append('')
# out=[]
# output=0
# for line in data:
# 	if line=='':
# 		H,W=len(out),len(out[0])
# 		for j in range(H-1):
# 			bad=False
# 			for dy in range(H-1):
# 				for i in range(W):
# 					if j-dy>=0 and j+dy+1<H and out[j-dy][i]!=out[j+dy+1][i]:
# 						bad=True
# 						break
# 			if not bad:
# 				output+=(j+1)*100
# 		print()
# 		for i in range(W-1):
# 			bad=False
# 			for dx in range(W-1):
# 				for j in range(H):
# 					if i-dx>=0 and i+dx+1<W and out[j][i-dx]!=out[j][i+dx+1]:
# 						bad=True
# 						break
# 			if not bad:
# 				output+=i+1
# 		out = []
# 	else:
# 		out.append([col for col in line])
# print(output)
