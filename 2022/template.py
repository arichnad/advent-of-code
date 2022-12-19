#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
from collections import defaultdict, deque, Counter

data1='''

'''.strip().splitlines()
data2='''
'''.strip().splitlines()

data=data1

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#for line in data:

