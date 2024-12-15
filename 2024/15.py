#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, numpy # list(itertools.permutations(range(4), 4))
# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
# from astar import AStar #python3 -mpip install astar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3 import * #python3 -mpip install install z3 z3-solver # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()) # if s.check()==z3.sat: print(int(str(s.model()[x]))) #don't use Int or Ints:  they are very slow
# import lmfit #sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran && python3 -mpip install lmfit
# from sympy import * #python3 -mpip install sympy # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install python3-dev pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########
'''.strip('\n').splitlines()
data1Moves='''
<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''.strip('\n').splitlines()

data1B='''
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######
'''.strip('\n').splitlines()
data1BMoves='''
<vv<<^^<<^^
'''.strip('\n').splitlines()

data2='''

'''.strip('\n').splitlines()
data2Moves='''

'''.strip('\n').splitlines()

# data=data1; moves=data1Moves
# data=data1B; moves=data1BMoves
data=data2; moves=data2Moves

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()

# W,H=len(data[0]),len(data)
#
#
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='@':
# 			robotX=i;robotY=j
# 			data[j][i]='.'
#
# for line in moves:
# 	for d in line:
# 		dir = '>v<^'.find(d.lower()) #clockwise, starting right
# 		dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
# 		newX = robotX+dx
# 		newY = robotY+dy
# 		if data[newY][newX]=='#':
# 			continue
# 		if data[newY][newX]=='O':
# 			checkX=newX
# 			checkY=newY
# 			while True:
# 				if data[checkY][checkX]=='#':
# 					moveEm=False
# 					break
# 				# if data[checkY][checkX]=='O':
# 				# 	continue
# 				if data[checkY][checkX]=='.':
# 					moveEm=True
# 					break
# 				checkX+=dx
# 				checkY+=dy
# 			if moveEm:
# 				data[checkY][checkX]='O'
# 				data[newY][newX]='.'
# 			else:
# 				continue
# 		robotX+=dx
# 		robotY+=dy
#
# for line in data:
# 	print(''.join(line))
# answer=0
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='O': answer+=100*j+i
# print(answer)


W,H=len(data[0]),len(data)


for j in range(H):
	for i in range(W):
		if data[j][i]=='@':
			robotX=i;robotY=j
			data[j][i]='.'

oldData=data
data=[]
for j in range(H):
	out=''
	for i in range(W):
		if oldData[j][i]=='O':
			out+='[]'
		elif oldData[j][i]=='.':
			out+='..'
		elif oldData[j][i]=='#':
			out+='##'
	data.append([i for i in out])
W*=2
robotX*=2


def move(newX, newY, dx, dy):
	global data
	if data[newY][newX]=='.':
		return True
	if data[newY][newX]=='#':
		return False

	left = data[newY][newX]=='['
	if dx!=0:
		output = move(newX+dx*2, newY, dx, dy)
	elif dy!=0:
		output = move(newX, newY+dy, dx, dy) and move(newX + (1 if left else -1), newY+dy, dx, dy)

	if output:
		# print(data, newX, newY)
		data[newY][newX] = '.'
		data[newY][newX + (1 if left else -1)] = '.'
		data[newY+dy][newX+dx] = '[' if left else ']'
		data[newY+dy][newX+dx + (1 if left else -1)] = ']' if left else '['

	return output


for line in moves:
	for d in line:
		dir = '>v<^'.find(d.lower()) #clockwise, starting right
		dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
		newX = robotX+dx
		newY = robotY+dy
		if data[newY][newX]=='#':
			continue
		if data[newY][newX]=='[' or data[newY][newX]==']':
			dataOrig=copy.deepcopy(data)
			if not move(newX, newY, dx, dy):
				data=dataOrig
				continue
		robotX+=dx
		robotY+=dy

		for line in data:
			print(''.join(line))
		print()
answer=0
for j in range(H):
	for i in range(W):
		if data[j][i]=='[': answer+=100*j+i
print(answer) #1533489

#dir = (dir+4)%4
#dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir = 1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = 'rdlu'.find(d.lower()) #clockwise, starting right
#dir = ['right', 'down', 'left', 'up'].index(d.lower()) #clockwise, starting right
#dir = '>v<^'.find(d.lower()) #clockwise, starting right

#data = [[column for column in line] for line in data]
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

