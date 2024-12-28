#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, numpy
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
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)

m={}
for line in data:
    (f,t)=line.split(' => ')
    fConverted = []
    for i in f.split(', '):
        (count, thing) = i.split(' ')
        fConverted.append((int(count), thing))
    f=tuple(fConverted)
    t=tuple(t.split(' '))
    m[t[1]] = (int(t[0]), f)

# need={'FUEL': 1}
# ore=0
# working=True
# while working:
#     newNeed={}
#     working=False
#     for n, needCount in need.items():
#         if needCount == 0: continue
#         if needCount < 0:
#             if n not in newNeed: newNeed[n] = 0
#             newNeed[n] += needCount
#             continue
#         working=True
#         if n not in m:
#             if n != 'ORE': print('oops')
#             ore+=needCount
#             continue
#         print('need', needCount, n, 'applying', m[n][0], n, ' <= ', m[n][1])
#         (getCount, fromValues) = m[n]
#         if needCount != getCount:
#             # print('  balance', needCount - getCount)
#             if n not in newNeed: newNeed[n] = 0
#             newNeed[n] += needCount - getCount
#         for fromCount, f in fromValues:
#             if f not in newNeed: newNeed[f] = 0
#             newNeed[f] += fromCount
#     need=newNeed
#
#     print(newNeed, ore)
# print(ore)

mem={}
def solveReverse(need):
    global mem, m
    memFrom = tuple(sorted(need.items()))
    for memTest in mem.keys():
        for test in memTest:
            if need[test[0]] < test[1]: break
        else:
            print('nice')

            for test in memTest:
                need[test[0]] -= test[1]
                if need[test[0]] == 0: del need[test[0]]
            return mem[memFrom] + need
    ore=0
    working = True
    while working:
        newNeed={}
        working=False
        for n, needCount in need.items():
            if needCount == 0: continue
            if needCount < 0:
                if n not in newNeed: newNeed[n] = 0
                newNeed[n] += needCount
                continue
            working=True
            if n not in m:
                if n != 'ORE': print('oops')
                ore+=needCount
                continue
            # print('need', needCount, n, 'applying', m[n][0], n, ' <= ', m[n][1])
            (getCount, fromValues) = m[n]
            if needCount != getCount:
                # print('  balance', needCount - getCount)
                if n not in newNeed: newNeed[n] = 0
                newNeed[n] += needCount - getCount
            for fromCount, f in fromValues:
                if f not in newNeed: newNeed[f] = 0
                newNeed[f] += fromCount
        need=newNeed
    mem[memFrom] = (ore, dict(need))
    return ore, dict(need)

(ore, need) = solveReverse({'FUEL': 1})
print(ore, need)
need['FUEL']=1
(ore, need) = solveReverse(need)
print(ore, need)


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

