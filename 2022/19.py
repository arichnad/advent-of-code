#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
from collections import defaultdict, deque, Counter

data1='''
Blueprint 1: Each ore robot costs 4 ore.  Each clay robot costs 2 ore.  Each obsidian robot costs 3 ore and 14 clay.  Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore.  Each clay robot costs 3 ore.  Each obsidian robot costs 3 ore and 8 clay.  Each geode robot costs 3 ore and 12 obsidian.
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data1
data=data2
TIME=24; ENTRIES=100
TIME=32; ENTRIES=3

print(len(data), TIME, ENTRIES)

data=data[:ENTRIES]

#data = [int(line) for line in data]
data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

def add(cur, robots, addition):
	#adds to the set, but makes sure to keep only the best values
	newCur=set()
	addMe=True
	for value in cur[robots] if robots in cur else []:
		if sum([value[i]>=addition[i] for i in range(4)])==4:
			addMe=False
		if sum([value[i]>addition[i] for i in range(4)])!=0:
			newCur.add(value)
	if addMe:
		newCur.add(addition)
	#print(sorted(newCur, key=lambda a:tuple(reversed(a)),reverse=True))
	cur[robots]=newCur
		

total=0
mult=1
for line in data:
	prev=set()
	cost=[[0,0,0,0] for i in range(4)]
	index, cost[0][0], cost[1][0], cost[2][0], cost[2][1], cost[3][0], cost[3][2] = line
	cur={(1,0,0,0): set([(0,0,0,0)])}
	for minute in range(TIME):
		prev=cur
		cur={}
		for robots in prev.keys():
			for have in prev[robots]:
				#performance hack:  if we can afford a geode robot, always buy it now, and try nothing else
				buy=3
				if sum([have[i]>=cost[buy][i] for i in range(4)])==4:
					newRobots=list(robots)
					newRobots[buy]+=1
					newRobots=tuple(newRobots)
					newHave = tuple([have[i]+robots[i]-cost[buy][i] for i in range(4)])
					add(cur, newRobots, newHave)
					continue
				
				#try to buy nothing
				newHave=tuple(have[i]+robots[i] for i in range(4))
				add(cur, robots, newHave)
				
				#try to buy each robot except the geode robot
				for buy in range(3):
					if sum([have[i]>=cost[buy][i] for i in range(4)])!=4:
						continue
					newRobots=list(robots)
					newRobots[buy]+=1
					newRobots=tuple(newRobots)
					newHave = tuple([have[i]+robots[i]-cost[buy][i] for i in range(4)])
					add(cur, newRobots, newHave)
		print(minute, len(cur))
	m=max(max(j[3] for j in i) for i in cur.values())
	print(m)
	total+=index*m
	mult*=m
	#print(sorted(cur.items(), key=lambda i:i[1][3])[-2])

print('total', total, 'mult', mult) #1681, 5394

