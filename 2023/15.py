#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
data = [[column for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()

ans=0
box=[[] for i in range(256)]
for col in data[0]:
	print(col)
	if '-' in col:
		lab,foc=col.split('-')
		a = 0
		for ch in lab:
			a += ord(ch)
			a *= 17
			a %= 256
		for i in range(len(box[a])):
			if box[a][i][0]==lab:
				print('removed!')
				del box[a][i]
				break
	else:
		lab,foc=col.split('=')

		a=0
		for ch in lab:
			a+=ord(ch)
			a*=17
			a%=256
		for i in range(len(box[a])):
			if box[a][i][0]==lab:
				print('changed!')
				box[a][i]=(lab,foc)
				break
		else:
			box[a].append((lab,foc))

	for i in range(len(box)):
		if len(box[i]) == 0: continue
		print(i, box[i])
answer=0
for i in range(len(box)):
	if len(box[i])==0: continue
	for j in range(len(box[i])):
		answer+=(i+1)*(j+1)*int(box[i][j][1])
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

# ans=0
# for col in data[0]:
# 	a=0
# 	for ch in col:
# 		a+=ord(ch)
# 		a*=17
# 		a%=256
# 	ans+=a
#
# print(ans)
