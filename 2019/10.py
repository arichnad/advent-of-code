#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, numpy
from functools import total_ordering

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
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
W,H=len(data[0]),len(data)

# best=0
# for j in range(H):
#     for i in range(W):
#         if data[j][i]!='#': continue
#         total=0
#         for newY in range(H):
#             for newX in range(W):
#                 if data[newY][newX]!='#': continue
#                 if newY==j and newX==i: continue
#                 dy=newY-j
#                 dx=newX-i
#                 y=j
#                 x=i
#                 if dx==0:
#                     while True:
#                         y += int(math.copysign(1, dy))
#                         if y==newY:
#                             total+=1
#                             break
#                         if data[y][x]=='#':
#                             break
#                 else:
#                     while True:
#                         x += int(math.copysign(1, dx))
#                         if x==newX:
#                             total+=1
#                             break
#                         if (dy * (x - newX)) % dx != 0: continue
#                         y = (dy * (x - newX)) // dx + newY
#                         if data[y][x]=='#':
#                             break
#         if total>best: best=total
# print(best)

best=(0, None, None)
for j in range(H):
    for i in range(W):
        if data[j][i]!='#': continue
        total=0
        for newY in range(H):
            for newX in range(W):
                if data[newY][newX]!='#': continue
                if newY==j and newX==i: continue
                dy=newY-j
                dx=newX-i
                y=j
                x=i
                if dx==0:
                    while True:
                        y += int(math.copysign(1, dy))
                        if y==newY:
                            total+=1
                            break
                        if data[y][x]=='#':
                            break
                else:
                    while True:
                        x += int(math.copysign(1, dx))
                        if x==newX:
                            total+=1
                            break
                        if (dy * (x - newX)) % dx != 0: continue
                        y = (dy * (x - newX)) // dx + newY
                        if data[y][x]=='#':
                            break
        if total>best[0]:
            best=(total,i,j)
(total,i,j)=best
print(i,j)
things=[]
theta = None
for num in range(200):
    for newY in range(H):
        for newX in range(W):
            if data[newY][newX] != '#': continue
            if newY == j and newX == i: continue
            dy = newY - j
            dx = newX - i
            y = j
            x = i
            if dx == 0:
                while True:
                    y += int(math.copysign(1, dy))
                    if y == newY:
                        angle=(math.atan2(dx, -dy)+math.tau)%math.tau
                        things.append((angle, newX, newY))
                        break
                    if data[y][x] == '#':
                        break
            else:
                while True:
                    x += int(math.copysign(1, dx))
                    if x == newX:
                        angle = (math.atan2(dx, -dy) + math.tau) % math.tau
                        things.append((angle, newX, newY))
                        break
                    if (dy * (x - newX)) % dx != 0: continue
                    y = (dy * (x - newX)) // dx + newY
                    if data[y][x] == '#':
                        break
    things=sorted(things)
    filtered=list(filter(lambda a: a[0]>theta if theta is not None else True, things))
    if len(filtered)==0:
        filtered=things
    (theta, newX, newY)=filtered[0]
    data[newY][newX]='.'
    print(num, newX*100+newY)

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

