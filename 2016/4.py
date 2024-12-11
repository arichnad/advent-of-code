#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
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
# 	a={}
# 	for i in re.findall('[a-z]', re.findall('^[a-z-]+', line)[0]):
# 		a[i]=a[i]+1 if i in a else 1
# 	id=int(re.findall('[0-9]+', line)[0])
# 	min=0
# 	prev=None
# 	for ch in reversed(re.findall('\[[a-z]*\]', line)[0][1:-1]):
# 		if ch not in a or a[ch] < min or a[ch]==min and ord(prev) < ord(ch):
# 			break
# 		min=a[ch]
# 		prev=ch
# 	else:
# 		answer+=id
# print(answer)
for line in data:
	a={}
	for i in re.findall('[a-z]', re.findall('^[a-z-]+', line)[0]):
		a[i]=a[i]+1 if i in a else 1
	id=int(re.findall('[0-9]+', line)[0])
	min=0
	prev=None
	for ch in reversed(re.findall('\[[a-z]*\]', line)[0][1:-1]):
		if ch not in a or a[ch] < min or a[ch]==min and ord(prev) < ord(ch):
			break
		min=a[ch]
		prev=ch
	else:
		output=''
		for i in re.findall('[a-z-]', re.findall('^[a-z-]+', line)[0]):
			output+=' ' if i=='-' else chr((ord(i)-ord('a')+id)%26 + ord('a'))
		if output=='northpole object storage ':
			print(id)


#dir=(dir+4)%4191663
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

