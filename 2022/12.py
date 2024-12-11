#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#for line in data:

w=len(data[0])
h=len(data)


for y in range(h):
	for x in range(w):
		if data[y][x]=='S':
			v=[[False for x in range(w)] for y in range(h)]
			q=[(x, y, ord('a'))]
			distance=0
			while len(q)>0:
				newQ=[]
				while len(q)>0:
					(x,y,last)=q.pop()
					if x<0 or x>=w or y<0 or y>=h:
						continue
					if ord(data[y][x] if data[y][x]!='E' else 'z')-last>1:
						continue
					if data[y][x]=='E':
						print(distance)
						newQ=[]
						break
					if v[y][x]:
						continue
					v[y][x]=True
					cur=ord(data[y][x] if data[y][x]!='S' else 'a')
					newQ.append((x+1, y, cur))
					newQ.append((x-1, y, cur))
					newQ.append((x, y+1, cur))
					newQ.append((x, y-1, cur))
				q=newQ
				distance+=1

d=[]
for y in range(h):
	for x in range(w):
		if data[y][x]=='S' or data[y][x]=='a':
			v=[[False for x in range(w)] for y in range(h)]
			q=[(x, y, ord('a'))]
			distance=0
			while len(q)>0:
				newQ=[]
				while len(q)>0:
					(x,y,last)=q.pop()
					if x<0 or x>=w or y<0 or y>=h:
						continue
					if ord(data[y][x] if data[y][x]!='E' else 'z')-last>1:
						continue
					if data[y][x]=='E':
						d.append(distance)
						newQ=[]
						break
					if v[y][x]:
						continue
					v[y][x]=True
					cur=ord(data[y][x] if data[y][x]!='S' else 'a')
					newQ.append((x+1, y, cur))
					newQ.append((x-1, y, cur))
					newQ.append((x, y+1, cur))
					newQ.append((x, y-1, cur))
				q=newQ
				distance+=1
print(list(reversed(sorted(d)))[-1])
