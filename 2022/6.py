#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#for line in data:

b=[]
t=0
for a in data[0]:
	b.append(a)
	if len(b)>4:
		b.pop(0)
	if len(set(b))==4:
		break
	t+=1
	print(t, b, len(b))
print(t+1)

b=[]
t=0
for a in data[0]:
	b.append(a)
	if len(b)>14:
		b.pop(0)
	if len(set(b))==14:
		break
	t+=1
	print(t, b, len(b))
print(t+1)
