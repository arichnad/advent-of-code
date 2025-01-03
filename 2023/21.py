#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
W,H=len(data[0]),len(data)


#for line in data:

map=[[set() for i in range(W)] for j in range(H)]
# counted=[[0 for i in range(W)] for j in range(H)]
# countedLooped=[[0 for i in range(W)] for j in range(H)]
for j in range(H):
	for i in range(W):
		if data[j][i]=='S':
			data[j][i]='.'
			map[j][i]= {(0, 0)}
			# counted[j][i]=1

mapCount=[[[] for i in range(W)] for j in range(H)]
DISTANCE=26501365
for run in range(DISTANCE):
	nextMap=[[set() for i in range(W)] for j in range(H)]

	for j in range(H):
		for i in range(W):
			mapCount[j][i].append(len(map[j][i]))

	for j in range(H):
		for i in range(W):
			curMap = map[j][i]

			if len(map[j][i])==0: continue
			for dir in range(4):
				dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
				newY, newX = j + dy, i + dx
				if newY<0 or newX<0 or newY>=H or newX>=W:

					if newY<0:
						newY+=H
						mapChange=(-1, 0)
					if newX<0:
						newX+=W
						mapChange=(0, -1)
					if newY>=H:
						newY-=H
						mapChange=(1, 0)
					if newX>=W:
						newX-=W
						mapChange=(0, 1)
					for entry in curMap:
						nextMap[newY][newX].add((entry[0]+mapChange[0], entry[1]+mapChange[1]))
					continue
				if data[newY][newX] != '.': continue

				if run+1 not in nextMap[newY][newX]:
					nextMap[newY][newX].update(curMap)


	runs=H
	if (run+1) >= runs*2:
		run=DISTANCE-1
		base = (run + 1) // runs + 1
		base2 = (run + 1) // runs
		newMapCount=0
		for y in range(H):
			for x in range(W):
				if len(map[y][x])==0: continue
				offset1 = mapCount[y][x][(run + 1) % runs]
				guess1 = base*(base-1) + offset1*base


				offset2 = mapCount[y][x][(run+1) % runs + runs]
				guess2 = base2*(base2-1) + offset2*base2

				guess = min(guess1, guess2)
				newMapCount += guess

				# answer=len(nextMap[y][x])
				# if guess != answer:
				# 	print(run, y, x, runs, 'base2', base2, 'prev', len(map[y][x]), 'offset1', offset1, 'guess1', guess1, 'offset2', offset2, 'guess2', guess2, 'answer', answer)
		print(newMapCount)
		break




	map=nextMap


# print(sum(sum(len(col) for col in row) for row in map))
#
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='#':
# 			print('#', end='')
# 		else:
# 			# print('O' if distance[j][i] % 2 == 0 and distance[j][i] <= DISTANCE else ' ', end='')
# 			print('O' if len(map[j][i])>0 else ' ',end='')
# 	print()





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

# cur=[]
# distance=[[None for i in range(W)] for i in range(H)]
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S':
# 			data[j][i]='.'
# 			cur.append((j,i))
# 			distance[j][i]=0
#
# while len(cur)>0:
# 	next=[]
# 	for (j,i) in cur:
# 		for dir in range(4):
# 			dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][dir]
# 			newY, newX = j + dy, i + dx
# 			if newY<0 or newX<0 or newY>=H or newX>=W: continue
# 			if data[newY][newX] != '.': continue
# 			if distance[newY][newX] is not None: continue
# 			distance[newY][newX]=distance[j][i]+1
# 			next.append((newY,newX))
# 	cur=next
#
# d=[0 for i in range(MAX)]
# for j in range(H):
# 	for i in range(W):
# 		if distance[j][i] is not None:
# 			d[distance[j][i]]+=1
#
# print(sum(d[i] for i in range(0,64+1,2)))

