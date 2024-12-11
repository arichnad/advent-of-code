#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

def sign(x):
	return 0 if x==0 else (1 if x>0 else -1)


headX,headY,tailX,tailY=0,0,0,0
pos=set()
for line in data:
	d,count=line.split(' ')
	count=int(count)
	for c in range(count):
		if d=='R':
			headX+=1
		if d=='L':
			headX-=1
		if d=='D':
			headY+=1
		if d=='U':
			headY-=1
		
		if abs(headX-tailX)>=2 or abs(headY-tailY)>=2:
			tailX+=sign(headX-tailX)
			tailY+=sign(headY-tailY)
		pos.add((tailX,tailY))
print(len(pos))
		
			

l=10
knotX=[0 for i in range(l)]
knotY=[0 for i in range(l)]
pos=set()
for line in data:
	d,count=line.split(' ')
	count=int(count)
	for c in range(count):
		if d=='R':
			knotX[0]+=1
		if d=='L':
			knotX[0]-=1
		if d=='D':
			knotY[0]+=1
		if d=='U':
			knotY[0]-=1
		
		for i in range(1,l):
			if abs(knotX[i-1]-knotX[i])>=2 or abs(knotY[i-1]-knotY[i])>=2:
				knotX[i]+=sign(knotX[i-1]-knotX[i])
				knotY[i]+=sign(knotY[i-1]-knotY[i])
		pos.add((knotX[l-1],knotY[l-1]))
print(len(pos))


