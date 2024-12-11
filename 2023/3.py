#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[column for column in line]+['.'] for line in data]
H=len(data)
W=len(data[0])

# num=''
# ans=0
# for j, row in enumerate(data):
# 	for i, column in enumerate(row):
# 		if ord(column)>=ord('0') and ord(column)<=ord('9'):
# 			if num == '': numStart=i
# 			num+=column
# 		else:
#
# 			if num != '':
# 				partFound = False
# 				for y in range(max(j - 1, 0), min(j + 1, H - 1)+1):
# 					for x in range(max(numStart - 1, 0), min(i, W - 1)+1):
# 						c=data[y][x]
# 						if ord(c) >= ord('0') and ord(c) <= ord('9'): continue
# 						if c == '.': continue
# 						partFound = True
# 				if partFound: ans+=int(num)
# 			num=''
# print(ans)

num=''
ans=0
partAt=[[[] for i in range(W)] for j in range(H)]

for j, row in enumerate(data):
	for i, column in enumerate(row):
		if ord(column)>=ord('0') and ord(column)<=ord('9'):
			if num == '': numStart=i
			num+=column
		else:

			if num != '':
				partFound = False
				for y in range(max(j - 1, 0), min(j + 1, H - 1)+1):
					for x in range(max(numStart - 1, 0), min(i, W - 1)+1):
						c=data[y][x]
						if c != '*': continue
						partAt[y][x].append(int(num))
			num=''

for row in partAt:
	for column in row:
		if len(column)==2:
			cur=1
			for i in column:
				cur*=i
			ans+=cur
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

