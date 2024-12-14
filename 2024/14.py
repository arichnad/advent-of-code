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
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

# data=data1;W=11;H=7
data=data2;W=101;H=103

#data = [int(line) for line in data]
data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)


# for time in range(100):
#     for i in range(len(data)):
#         data[i][0] += data[i][2]
#         data[i][1] += data[i][3]
#
# ans = [0, 0, 0, 0]
# for i in range(len(data)):
#     data[i][0] %= W
#     data[i][1] %= H
#     if data[i][0] < W // 2:
#         q = 0
#     elif data[i][0] > W // 2:
#         q = 1
#     else:
#         continue
#
#     if data[i][1] < H // 2:
#         q += 0
#     elif data[i][1] > H // 2:
#         q += 2
#     else:
#         continue
#
#     ans[q] += 1
# print(ans)
# print(ans[0] * ans[1] * ans[2] * ans[3])
best=None
for time in range(10000):
    for i in range(len(data)):
        data[i][0] += data[i][2]
        data[i][1] += data[i][3]


    ans = [0, 0, 0, 0]
    for i in range(len(data)):
        data[i][0] %= W
        data[i][1] %= H
        if data[i][0] < W // 2:
            q = 0
        elif data[i][0] > W // 2:
            q = 1
        else:
            continue

        if data[i][1] < H // 2:
            q += 0
        elif data[i][1] > H // 2:
            q += 2
        else:
            continue

        ans[q] += 1
    ans = ans[0] * ans[1] * ans[2] * ans[3]
    if best is None or ans < best:
        # b = [[0 for i in range(W)] for j in range(H)]
        # for line in data: b[line[1] % H][line[0] % W] += 1
        # for line in b: print(''.join([str(i) if i>0 else ' ' for i in line]))
        best,bestTime=ans,time+1

print(bestTime)

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

