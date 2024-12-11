#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
30373
25512
65332
33549
35390
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#for line in data:
t=0
w=len(data[0])
h=len(data)
sMax=0
for row in range(h):
	for col in range(w):
		vis=False
		sTotal=1
		for dx in [-1, 0, 1]:
			for dy in [-1, 0, 1]:
				if dx==0 and dy==0 or dx!=0 and dy!=0:
					continue
				y,x=row,col
				x+=dx
				y+=dy
				while x>=0 and x<w and y>=0 and y<h:
					if data[y][x]>=data[row][col]:
						s=abs(y-row)+abs(x-col)
						break
					x+=dx
					y+=dy
				else:
					s=abs(y-row)+abs(x-col)-1
					vis=True
				sTotal*=s
				if row!=0 and row!=h-1 and col!=0 and col!=w-1 and sTotal>sMax:
					sMax=sTotal
		if vis:
			t+=1
print(t, sMax)

