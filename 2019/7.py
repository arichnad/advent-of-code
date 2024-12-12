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
3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
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

# orig = data
# best=-1
# for phase in list(itertools.permutations(range(5), 5)):
#     input = 0
#     for ph in phase:
#         data=orig[:]
#         pc=0
#         output = None
#         while True:
#             d=data[pc]
#             code=d%100; d//=100
#             immediate1=(d%10)!=0; d//=10
#             immediate2=(d%10)!=0; d//=10
#             immediate3=(d%10)!=0
#
#             if code==99: break
#             a,b,c = data[pc+1],data[pc+2] if pc+2 < len(data) else None,data[pc+3] if pc+3 < len(data) else None
#             # print(code, a, b, c)
#             if code!=3 and code!=4:
#                 a,b = a if immediate1 else data[a],b if immediate2 else data[b]
#             if code==1:
#                 data[c]=a+b
#                 pc += 4
#             elif code==2:
#                 data[c]=a*b
#                 pc += 4
#             elif code==3:
#                 b=ph if ph is not None else input
#                 ph = None
#                 print('### data[', a, '] =', b)
#                 data[a]=b
#                 pc += 2
#             elif code==4:
#                 print('### output', data[a])
#                 output = data[a]
#                 pc += 2
#             elif code==5 or code==6:
#                 if a!=0 if code==5 else a==0:
#                     pc=b
#                 else:
#                     pc += 3
#             elif code==7:
#                 data[c] = 1 if a < b else 0
#                 pc += 4
#             elif code==8:
#                 data[c] = 1 if a == b else 0
#                 pc += 4
#             else:
#                 print('oops')
#                 break
#         input = output
#         print("********")
#     if output>best: best=output
# print(best)

orig = data
best=-1

for phase in list(itertools.permutations(range(5, 10), 5)):
    datas = [(orig[:], 0, [phase[i]]) for i in range(5)]
    datas[0] = (datas[0][0], datas[0][1], datas[0][2] + [0])

    running=[True for _ in range(5)]
    moreOutput=[]
    while any(running):
        for i, (data, pc, input) in enumerate(datas):
            input.extend(moreOutput)
            moreOutput = []
            if not running[i]:
                continue #moreOutput?
            while True:
                d=data[pc]
                code=d%100; d//=100
                immediate1=(d%10)!=0; d//=10
                immediate2=(d%10)!=0; d//=10
                immediate3=(d%10)!=0

                if code==99:
                    print(i, 'halt')
                    running[i]=False
                    break
                a,b,c = data[pc+1],data[pc+2] if pc+2 < len(data) else None,data[pc+3] if pc+3 < len(data) else None
                # print(code, a, b, c)
                if code!=3 and code!=4:
                    a,b = a if immediate1 else data[a],b if immediate2 else data[b]
                if code==1:
                    data[c]=a+b
                    pc += 4
                elif code==2:
                    data[c]=a*b
                    pc += 4
                elif code==3:
                    b=input.pop(0)
                    ph = None
                    print('### data[', a, '] =', b)
                    data[a]=b
                    pc += 2
                elif code==4:
                    print('### output', i, data[a])
                    if i==4: finalOutput=data[a]
                    moreOutput.append(data[a])
                    pc += 2
                    break
                elif code==5 or code==6:
                    if a!=0 if code==5 else a==0:
                        pc=b
                    else:
                        pc += 3
                elif code==7:
                    data[c] = 1 if a < b else 0
                    pc += 4
                elif code==8:
                    data[c] = 1 if a == b else 0
                    pc += 4
                else:
                    print('oops')
                    break

            datas[i] = (data, pc, input)

            print("********")
        print(finalOutput)
        if finalOutput>best: best=finalOutput
print(best)

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

