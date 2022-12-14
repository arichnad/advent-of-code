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
Sensor at x=2302110, y=2237242: closest beacon is at x=2348729, y=1239977
Sensor at x=47903, y=2473047: closest beacon is at x=-432198, y=2000000
Sensor at x=2363579, y=1547888: closest beacon is at x=2348729, y=1239977
Sensor at x=3619841, y=520506: closest beacon is at x=2348729, y=1239977
Sensor at x=3941908, y=3526118: closest beacon is at x=3772294, y=3485243
Sensor at x=3206, y=1564595: closest beacon is at x=-432198, y=2000000
Sensor at x=3123411, y=3392077: closest beacon is at x=2977835, y=3592946
Sensor at x=3279053, y=3984688: closest beacon is at x=2977835, y=3592946
Sensor at x=2968162, y=3938490: closest beacon is at x=2977835, y=3592946
Sensor at x=1772120, y=2862246: closest beacon is at x=2017966, y=3158243
Sensor at x=3283241, y=2619168: closest beacon is at x=3172577, y=2521434
Sensor at x=2471642, y=3890150: closest beacon is at x=2977835, y=3592946
Sensor at x=3163348, y=3743489: closest beacon is at x=2977835, y=3592946
Sensor at x=2933313, y=2919047: closest beacon is at x=3172577, y=2521434
Sensor at x=2780640, y=3629927: closest beacon is at x=2977835, y=3592946
Sensor at x=3986978, y=2079918: closest beacon is at x=3998497, y=2812428
Sensor at x=315464, y=370694: closest beacon is at x=-550536, y=260566
Sensor at x=3957316, y=3968366: closest beacon is at x=3772294, y=3485243
Sensor at x=2118533, y=1074658: closest beacon is at x=2348729, y=1239977
Sensor at x=3494855, y=3378533: closest beacon is at x=3772294, y=3485243
Sensor at x=2575727, y=210553: closest beacon is at x=2348729, y=1239977
Sensor at x=3999990, y=2813525: closest beacon is at x=3998497, y=2812428
Sensor at x=3658837, y=3026912: closest beacon is at x=3998497, y=2812428
Sensor at x=1551619, y=1701155: closest beacon is at x=2348729, y=1239977
Sensor at x=2625855, y=3330422: closest beacon is at x=2977835, y=3592946
Sensor at x=3476946, y=2445098: closest beacon is at x=3172577, y=2521434
Sensor at x=2915568, y=1714113: closest beacon is at x=2348729, y=1239977
Sensor at x=729668, y=3723377: closest beacon is at x=-997494, y=3617758
Sensor at x=3631681, y=3801747: closest beacon is at x=3772294, y=3485243
Sensor at x=2270816, y=3197807: closest beacon is at x=2017966, y=3158243
Sensor at x=3999999, y=2810929: closest beacon is at x=3998497, y=2812428
Sensor at x=3978805, y=3296024: closest beacon is at x=3772294, y=3485243
Sensor at x=1054910, y=811769: closest beacon is at x=2348729, y=1239977
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

