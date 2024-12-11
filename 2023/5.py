#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]

# seeds=data.pop(0)
#
# maps = [[] for i in range(7)]
#
# mapNumber=0
# for line in data:
# 	if len(line)==0:
# 		if len(maps[mapNumber]) != 0:
# 			mapNumber+=1
# 		continue
# 	maps[mapNumber].append(line)
#
# answer=None
# for seed in seeds:
# 	for map in maps:
# 		for [dest,source,range] in map:
# 			endSource=source+range
# 			if seed>=source and seed<endSource:
# 				seed=seed-source+dest
# 				break
# 	if answer is None or seed<answer:
# 		answer=seed
# print(answer)

seeds=data.pop(0)
seeds = [(seeds[i*2],seeds[i*2+1]) for i in range(len(seeds)//2)]

maps = [[] for i in range(7)]

mapNumber=0
for line in data:
	if len(line)==0:
		if len(maps[mapNumber]) != 0:
			mapNumber+=1
		continue
	maps[mapNumber].append(line)

answer=None
for seed in seeds:
	seed=[seed]
	for map in maps:
		outputSeed=[]
		for [dest,source,range] in map:
			endSource=source+range
			change=True
			while change:
				change=False
				for i, entry in enumerate(seed):
					if entry[0]>=source and entry[0]+entry[1]<=endSource:
						outputSeed.append((entry[0]-source+dest,entry[1]))
						seed.pop(i)
						change=True
						break
					if entry[0] < source and entry[0] + entry[1] > endSource:
						outputSeed.append((dest, range))
						removed = seed.pop(i)
						seed.append((entry[0], source - entry[0]))
						seed.append((endSource, entry[0] + entry[1] - endSource))
						change = True
						break
					if entry[0]<source and entry[0]+entry[1] > source:
						outputSeed.append((dest,entry[0]+entry[1]-source))
						removed=seed.pop(i)
						seed.append((entry[0],source-entry[0]))
						change=True
						break
					if entry[0] < endSource and entry[0] + entry[1] > endSource:
						outputSeed.append((entry[0]-source+dest,endSource-entry[0]))
						removed = seed.pop(i)
						seed.append((endSource, entry[0] + entry[1] - endSource))
						change = True
						break
		seed=seed+outputSeed
	for entry in seed:
		if answer is None or entry[0]<answer:
			answer=entry[0]
print(answer)



#dir=(dir+4)%4
#dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = "rdlu".find(ch.lower())

#data = [[column for column in line] for line in data]
#W,H=len(data[0]), len(data)
#for j in range(H):
#	for i in range(W):
#		for dy in range(-1, 2):
#			for dx in range(-1, 2):
#				#if dx==0 and dy==0: continue
#				if dx==0 and dy==0 or dx!=0 and dy!=0: continue
#
#				newY,newX=j+dy,i+dx
#				if newY<0 or newX<0 or newY>=H or newX>=W: continue
#
#for line in data: print(''.join(line))

