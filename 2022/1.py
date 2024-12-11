#!/usr/bin/python3

import math, re, sys, itertools
#from sortedcontainers import SortedList #pip3 install sortedcontainers
from collections import defaultdict, deque, Counter

data1='''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#m=0
#total=0
#for line in data:
#	if line == '':
#		if total>m:
#			m=total
#		total=0
#	else:
#		total+=int(line)
#
#if total>m:
#	m=total
#
#print(m)

m=0
total=0
a=[]
for line in data:
	if line == '':
		a.append(total)
		total=0
	else:
		total+=int(line)

a.append(total)

print(sum(list(reversed(sorted(a)))[:3]))

