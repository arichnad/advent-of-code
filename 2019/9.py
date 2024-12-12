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
104,1125899906842624,99
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]
data = [int(column) for column in re.findall('-?[\\d]+', data[0])]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)

data += [0 for _ in range(200000)]
orig = data
pc=0
ref=0
# input=[1]
input=[2]
data = orig[:]

while True:
    d=data[pc]
    code=d%100; d//=100
    type1=d%10; d//=10
    type2=d%10; d//=10
    type3=d%10

    if code==99:
        print('halt')
        break
    a,b,c = data[pc+1],data[pc+2] if pc+2 < len(data) else None,data[pc+3] if pc+3 < len(data) else None
    print(pc, ':', data[pc], a, b, c)#;print(type1, type2, type3)

    if code==3:
        a = 99999 if type1 == 1 else (a if type1 == 0 else a + ref)
    else:
        a = a if type1 == 1 else (data[a] if type1 == 0 else data[a + ref])
    if code!=3 and code!=4 and code!=9:
        b = b if type2 == 1 else (data[b] if type2 == 0 else data[b + ref])
        if code==1 or code==2 or code==3 or code==7 or code==8:
            c = 99999 if type3 == 1 else (c if type3 == 0 else c+ref)
        else:
            c = c if type3 == 1 else (data[c] if type3 == 0 else data[c + ref])

    if code==1:
        print('data[',c,']=',a,'+',b)
        data[c]=a+b
        pc += 4
    elif code==2:
        print('data[',c,']=',a,'*',b)
        data[c]=a*b
        pc += 4
    elif code==3:
        b=input.pop(0)
        print('data[', a, '] =', b)
        data[a]=b
        pc += 2
    elif code==4:
        print('### output', a)
        pc += 2
    elif code==5 or code==6:
        print('jump to ', b, 'if ', a, 'is', 'non-zero' if code==5 else 'zero')
        if a!=0 if code==5 else a==0:
            pc=b
        else:
            pc += 3
    elif code==7:
        print('data[', c, '] = 1 if', a, '<', b, 'else 0')
        data[c] = 1 if a < b else 0
        pc += 4
    elif code==8:
        print('data[', c, '] = 1 if', a, '==', b, 'else 0')
        data[c] = 1 if a == b else 0
        pc += 4
    elif code==9:
        ref += a
        print('ref +=', a)
        pc += 2
    else:
        print('oops')
        break


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

