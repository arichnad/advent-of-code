#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]

# answer=0
# for line in data:
# 	line=line.split(": ")[1]
# 	a,b=line.split(" | ")
# 	# a=a.replace("  ", " ")
# 	# b=b.replace("  ", " ")
# 	# a = a.split(" ")
# 	# b = b.split(" ")
# 	a = re.findall('-?[\d]+', a)
# 	b = re.findall('-?[\d]+', b)
# 	a = [int(a) for a in a]
# 	b = [int(b) for b in b]
# 	point=-1
# 	for b0 in b:
# 		if b0 in a:
# 			point+=1
# 	answer+=2**point if point!=-1 else 0
# print(answer)

cards=[1 for i in range(len(data))]
for i, line in enumerate(data):
	print(i, cards[i])
	line=line.split(": ")[1]
	a,b=line.split(" | ")
	# a=a.replace("  ", " ")
	# b=b.replace("  ", " ")
	# a = a.split(" ")
	# b = b.split(" ")
	a = re.findall('-?[\d]+', a)
	b = re.findall('-?[\d]+', b)
	a = [int(a) for a in a]
	b = [int(b) for b in b]
	point=0
	for b0 in b:
		if b0 in a:
			point+=1
	for j in range(point):
		print("  ", i, j+1, cards[i])
		cards[i+j+1]+=cards[i]
print(sum(cards))



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

