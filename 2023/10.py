#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''.strip('\n').splitlines()
data1='''
..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
'''.strip('\n').splitlines()
data1='''
OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()



#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()

# visited=set()
# current={}
# data = [[column for column in line] for line in data]
# W,H=len(data[0]), len(data)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S':
# 			current[(j,i)]=0
#
# while len(current)>0:
# 	next= {}
# 	for (j,i),dist in current.items():
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				#if dx==0 and dy==0: continue
# 				if dx==0 and dy==0 or dx!=0 and dy!=0: continue
#
# 				newY,newX=j+dy,i+dx
# 				if newY<0 or newX<0 or newY>=H or newX>=W: continue
#
# 				old=data[j][i]
# 				new=data[newY][newX]
# 				if not (dx==1 and (new=='-' or new=='J' or new =='7') or
# 						dx==-1 and (new=='-' or new == 'L' or new =='F') or
# 						dy==1 and (new=='|' or new == 'L' or new == 'J') or
# 						dy==-1 and (new=='|' or new == 'F' or new == '7')):
# 					continue
# 				if not(
# 						old=='S' or
# 						dx == 1 and (old == '-' or old == 'L' or old == 'F') or
# 						dx == -1 and (old == '-' or old == 'J' or old == '7') or
# 						dy == 1 and (old == '|' or old == 'F' or old == '7') or
# 						dy == -1 and (old == '|' or old == 'L' or old == 'J')):
# 					continue
# 				if (newY, newX) in next:
# 					print('found n', max(next[(newY, newX)], dist))
# 				if (newY,newX) in current:
# 					print('found c', current[(newY, newX)], dist)
# 				if (newY,newX) in visited: continue
# 				next[(newY,newX)]=dist+1
# 				visited.add((newY,newX))
# 	current=next

data=data2

onLoop=set()
current={}
data = [[column for column in line] for line in data]
W,H=len(data[0]), len(data)
for j in range(H):
	for i in range(W):
		if data[j][i]=='S':
			current[(j,i)]=0
			onLoop.add((j,i))

startPos=set()
start=None
while len(current)>0:
	next= {}
	for (j,i),dist in current.items():
		for dy in range(-1, 2):
			for dx in range(-1, 2):
				#if dx==0 and dy==0: continue
				if dx==0 and dy==0 or dx!=0 and dy!=0: continue

				newY,newX=j+dy,i+dx
				if newY<0 or newX<0 or newY>=H or newX>=W: continue

				old=data[j][i]
				new=data[newY][newX]
				if not (dx==1 and (new=='-' or new=='J' or new =='7') or
						dx==-1 and (new=='-' or new == 'L' or new =='F') or
						dy==1 and (new=='|' or new == 'L' or new == 'J') or
						dy==-1 and (new=='|' or new == 'F' or new == '7')):
					continue
				if not(
						old=='S' or
						dx == 1 and (old == '-' or old == 'L' or old == 'F') or
						dx == -1 and (old == '-' or old == 'J' or old == '7') or
						dy == 1 and (old == '|' or old == 'F' or old == '7') or
						dy == -1 and (old == '|' or old == 'L' or old == 'J')):
					continue
				if (newY,newX) in onLoop: continue
				if old=='S':
					startPos.add((dx, dy))
					start=(j,i)
				next[(newY,newX)]=dist+1
				onLoop.add((newY, newX))
	current=next
if (1,0) in startPos and (0,1) in startPos:
	data[start[0]][start[1]]='F'
if (1,0) in startPos and (0,-1) in startPos:
	data[start[0]][start[1]]='L'
if (-1,0) in startPos and (0,1) in startPos:
	data[start[0]][start[1]]='7'
if (-1,0) in startPos and (0,-1) in startPos:
	data[start[0]][start[1]]='J'
if (-1,0) in startPos and (1,0) in startPos:
	data[start[0]][start[1]]='-'
if (0,1) in startPos and (0,-1) in startPos:
	data[start[0]][start[1]]='|'
for line in data:
	print(''.join(line))


current=set()
current.add((0,0))
outsideLoop=[[False for i in range(W*2)] for i in range(H*2)]
while len(current)>0:
	next= set()
	for (j,i) in current:
		for dy in range(-1, 2):
			for dx in range(-1, 2):
				if dx==0 and dy==0 or dx!=0 and dy!=0: continue

				newY,newX=j+dy,i+dx
				if newY < 0 or newX < 0 or newY >= H * 2 or newX >= W * 2: continue
				if outsideLoop[newY][newX]:
					continue
				if newY//2!=j//2 or newX//2!=i//2:
					outsideLoop[newY][newX] = True
					next.add((newY, newX))
					continue


				old=data[j//2][i//2] if i//2<W and j//2<H else ' '
				new=data[newY//2][newX//2]


				i2=i%2
				j2=j%2

				if (j//2, i//2) in onLoop and (
					abs(dx) == 1 and j2 == 0 and (old == '|' or old == 'J' or old == 'L') or
					abs(dx) == 1 and j2 == 1 and (old == '|' or old == '7' or old == 'F') or
					abs(dy) == 1 and i2 == 0 and (old == '-' or old == 'J' or old == '7') or
					abs(dy) == 1 and i2 == 1 and (old == '-' or old == 'F' or old == 'L')):
					continue
				if new == 'I':
					print(newY, newX, j//2, i//2, j2, i2, old, new, newY//2==j//2 and newX//2==i//2)

				outsideLoop[newY][newX]=True
				next.add((newY,newX))
	current=next

ans=H*W
for j in range(H):
	for i in range(W):
		outside=False
		for j2 in range(2):
			for i2 in range(2):
				if outsideLoop[j*2+j2][i*2+i2]:
					outside=True
		if outside:
			ans-=1


for j in range(H*2):
	for i in range(W*2):
		if (j//2,i//2) in onLoop:
			print('X', end='')
		elif outsideLoop[j][i]:
			print('*', end='')
		else:
			print(' ', end='')
	print()
print(ans) #631 too high






#dir=(dir+4)%4
#dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = "rdlu".find(ch.lower())



# current=set()
# for i in range(W):
# 	current.add((0, i))
# 	current.add((H, i))
# for j in range(H):
# 	current.add((j, 0))
# 	current.add((j, W))
# outsideLoop=[[False for i in range(W)] for i in range(H)]
# while len(current)>0:
# 	next= set()
# 	for (j,i) in current:
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				if dx==0 and dy==0 or dx!=0 and dy!=0: continue
#
# 				newY,newX=j+dy,i+dx
# 				if newY<0 or newX<0 or newY>=H or newX>=W: continue
#
# 				old=data[j][i] if i<W and j<H else ' '
# 				new=data[newY][newX]
# 				if outsideLoop[newY][newX]:
# 					continue
#
# 				if (j, i) in onLoop and (
# 					dx == 1 and (old == '|' or old == 'J' or old == 'L') or
# 					dx == -1 and (old == '|' or old == 'J' or old == 'L') or
# 					dy == 1 and (old == '-' or old == 'J' or old == '7') or
# 					dy == -1 and (old == '-' or old == 'J' or old == '7')):
# 					continue
# 				if (newY, newX) in onLoop and (
# 					dx == 1 and False or
# 					dx == -1 and (new == '|' or new == 'J' or new == 'L') or
# 					dy == 1 and False or
# 					dy == -1 and (new == '-' or new == 'J' or new == '7')):
# 					continue
# 				if new == 'I':
# 					print(newY, newX, j, i, old)
#
# 				outsideLoop[newY][newX]=True
# 				next.add((newY,newX))
# 	current=next
#
# ans=H*W
# for j in range(H):
# 	for i in range(W):
# 		if (j,i) in onLoop:
# 			print('X', end='')
# 			ans-=1
# 		elif outsideLoop[j][i]:
# 			print('*', end='')
# 			ans-=1
# 		else:
# 			print(' ', end='')
# 	print()
# print(ans) #631 too high

