#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
245182-790572
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=[int(x) for x in data1[0].split('-')]

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#count=0
#for value in range(data[0], data[1]+1):
#	a=[int(v) for v in str(value)]
#	if a != sorted(a): continue
#	last=None
#	for i in a:
#		if last == i:
#			break
#		last=i
#	else: continue
#	count+=1
#print(count)

count=0
for value in range(data[0], data[1]+1):
	a=[int(v) for v in str(value)]
	if a != sorted(a): continue
	good=False
	bad=False
	last = None
	c = Counter(a)
	if 2 in c.values():
		count+=1
print(count)


