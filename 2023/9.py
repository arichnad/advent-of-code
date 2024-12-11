#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
data = [[int(column) for column in line.split(' ')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()

# answer=0
# for line in data:
# 	done=False
# 	while not done:
# 		newLine=[]
# 		done=True
# 		ch=0
# 		for i in range(len(line)-1):
# 			ch=line[i+1]-line[i]
# 			if ch!=0:
# 				done=False
# 			newLine.append(ch)
# 		answer+=line[-1]
# 		line=newLine
# print(answer)

total=0
for line in data:
	done=False
	answer=0
	newLine=[line[:]]
	for depth in range(10000):
		newLine.append([])
		done=True
		ch=0
		for i in range(len(newLine[depth])-1):
			ch=newLine[depth][i+1]-newLine[depth][i]
			if ch!=0:
				done=False
			newLine[depth+1].append(ch)
		if done:
			break
	for depth in reversed(range(len(newLine))):
		answer=newLine[depth][0]-answer
		print(newLine[depth], answer)
	print()
	total+=answer
print(total) #102

# total=0
# for line in data:
# 	done=False
# 	answer=0
# 	while not done:
# 		newLine=[]
# 		done=True
# 		ch=0
# 		for i in range(len(line)-1):
# 			ch=line[i+1]-line[i]
# 			if ch!=0:
# 				done=False
# 			newLine.append(ch)
# 		answer=line[0]-answer
# 		print(line, -answer)
# 		line=newLine
# 	total+=-answer
# 	print(-answer)
# 	break
# print(total) #102

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

