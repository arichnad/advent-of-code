#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data1
searchRow=10
data=data2
searchRow=2000000


searchSpace=searchRow*2

#data = [int(line) for line in data]
data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

union=[]
for line in data:
	[x,y,x2,y2]=line
	d=abs(x2-x)+abs(y2-y)
	dRow=d-abs(y-searchRow)
	if dRow<=0:
		continue
	union.append((x-dRow,x+dRow))

changed=True
while changed:
	changed=False
	union=sorted(union)
	for first in range(len(union)):
		for second in range(first+1,len(union)):
			f,s=union[first],union[second]
			if f[0]<=s[0] and f[1]>=s[1]:
				union.remove(s)
				changed=True
				break
			if f[0]<=s[0] and f[1]>=s[0]:
				union.remove(f)
				union.remove(s)
				union.append((f[0],s[1]))
				changed=True
				break
			if f[1]+1==s[0]:
				union.remove(f)
				union.remove(s)
				union.append((f[0],s[1]))
				changed=True
				break
print(union[0][1]-union[0][0])


for searchRow in range(searchSpace+1):
	union=[]
	for line in data:
		[x,y,x2,y2]=line
		d=abs(x2-x)+abs(y2-y)
		dRow=d-abs(y-searchRow)
		if dRow<=0:
			continue
		union.append((x-dRow,x+dRow))

	changed=True
	while changed:
		changed=False
		union=sorted(union)
		for first in range(len(union)):
			for second in range(first+1,len(union)):
				f,s=union[first],union[second]
				if f[0]<=s[0] and f[1]>=s[1]:
					union.remove(s)
					changed=True
					break
				if f[0]<=s[0] and f[1]>=s[0]:
					union.remove(f)
					union.remove(s)
					union.append((f[0],s[1]))
					changed=True
					break
				if f[1]+1==s[0]:
					union.remove(f)
					union.remove(s)
					union.append((f[0],s[1]))
					changed=True
					break
	if(len(union)>1):
		print(searchRow+searchSpace*(union[0][1]+1))
		break

