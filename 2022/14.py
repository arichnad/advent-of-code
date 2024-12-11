#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
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

W=1000
H=1000
d=[[' ' for x in range(W)] for y in range(H)]

for line in data:
	line=[[int(x) for x in col.split(',')] for col in line.split(' -> ')]
	for col in range(len(line)-1):
		[x1,y1]=line[col]
		[x2,y2]=line[col+1]
		dx=sign(x2-x1)
		dy=sign(y2-y1)
		while x1!=x2 or y1!=y2:
			d[y1][x1]='#'
			x1+=dx
			y1+=dy
		d[y2][x2]='#'



i=0
while True:
	x,y=500,0
	while y+1<H:
		if d[y+1][x]==' ':
			y+=1
			continue
		if d[y+1][x-1]==' ':
			y+=1
			x-=1
			continue
		if d[y+1][x+1]==' ':
			y+=1
			x+=1
			continue
		d[y][x]='o'
		#for row in d[:15]: print(''.join(row[480:520]))
		if x==500 and y==0:
			i+=1
			break
		i+=1
		break
	if y+1==H or x==H or (x==500 and y==0):
		break

print(i)

	

d=[[' ' for x in range(W)] for y in range(H)]

maxY=0
for line in data:
	line=[[int(x) for x in col.split(',')] for col in line.split(' -> ')]
	for col in range(len(line)-1):
		[x1,y1]=line[col]
		[x2,y2]=line[col+1]
		dx=sign(x2-x1)
		dy=sign(y2-y1)
		if y1>maxY: maxY=y1
		if y2>maxY: maxY=y2
		while x1!=x2 or y1!=y2:
			d[y1][x1]='#'
			x1+=dx
			y1+=dy
		d[y2][x2]='#'

x1,x2=0,W-1
y1,y2=maxY+2,maxY+2
dx=sign(x2-x1)
dy=sign(y2-y1)
while x1!=x2 or y1!=y2:
	d[y1][x1]='#'
	x1+=dx
	y1+=dy


i=0
while True:
	x,y=500,0
	while y+1<H:
		if d[y+1][x]==' ':
			y+=1
			continue
		if d[y+1][x-1]==' ':
			y+=1
			x-=1
			continue
		if d[y+1][x+1]==' ':
			y+=1
			x+=1
			continue
		d[y][x]='o'
		#for row in d[:15]: print(''.join(row[480:520]))
		if x==500 and y==0:
			i+=1
			break
		i+=1
		break
	if y+1==H or x==H or (x==500 and y==0):
		break

print(i)

	

