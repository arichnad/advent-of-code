#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

t=0
for line in data:
	a,b=line.split(',')
	c,d=[int(x) for x in a.split('-')]
	e,f=[int(x) for x in b.split('-')]
	if c<=e and d>=f or c>=e and d<=f: t+=1
print(t)

t=0
for line in data:
	a,b=line.split(',')
	c,d=[int(x) for x in a.split('-')]
	e,f=[int(x) for x in b.split('-')]
	if (c<=e<=d) or (c<=f<=d) or (e<=c<=f) or (e<=d<=f): t+=1
print(t)

