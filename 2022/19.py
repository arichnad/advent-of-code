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
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 17 clay. Each geode robot costs 4 ore and 20 obsidian.
Blueprint 2: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 3: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 7 clay. Each geode robot costs 4 ore and 13 obsidian.
Blueprint 4: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 10 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 5: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 6: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 16 clay. Each geode robot costs 2 ore and 15 obsidian.
Blueprint 7: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 15 clay. Each geode robot costs 2 ore and 15 obsidian.
Blueprint 8: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 2 ore and 18 obsidian.
Blueprint 9: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 7 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 10: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 6 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 11: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 12: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 13: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 17 obsidian.
Blueprint 14: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 2 ore and 14 obsidian.
Blueprint 15: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 10 clay. Each geode robot costs 2 ore and 11 obsidian.
Blueprint 16: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 13 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 17: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 3 ore and 10 obsidian.
Blueprint 18: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 2 ore and 17 obsidian.
Blueprint 19: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 11 clay. Each geode robot costs 4 ore and 12 obsidian.
Blueprint 20: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 7 clay. Each geode robot costs 3 ore and 10 obsidian.
Blueprint 21: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 13 clay. Each geode robot costs 3 ore and 7 obsidian.
Blueprint 22: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 23: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 3 ore and 18 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 18 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 25: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 15 obsidian.
Blueprint 26: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 3 ore and 9 obsidian.
Blueprint 27: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 5 clay. Each geode robot costs 3 ore and 7 obsidian.
Blueprint 28: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 11 clay. Each geode robot costs 2 ore and 8 obsidian.
Blueprint 29: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 12 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 30: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 10 clay. Each geode robot costs 3 ore and 10 obsidian.
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
				buy=3
				if sum([have[i]>=cost[buy][i] for i in range(4)])==4:
					newRobots=list(robots)
					newRobots[buy]+=1
					newRobots=tuple(newRobots)
					newHave = tuple([have[i]+robots[i]-cost[buy][i] for i in range(4)])
					add(cur, newRobots, newHave)
					continue
				newHave=tuple(have[i]+robots[i] for i in range(4))
				add(cur, robots, newHave)
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

