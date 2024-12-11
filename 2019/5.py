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


# data1='''1002,4,3,4,33'''.strip().splitlines()
data1='''3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'''.strip().splitlines()
data2='''
3,225,1,225,6,6,1100,1,238,225,104,0,1002,148,28,224,1001,224,-672,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,8,21,225,1102,13,10,225,1102,21,10,225,1102,6,14,225,1102,94,17,225,1,40,173,224,1001,224,-90,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,2,35,44,224,101,-80,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,26,94,224,101,-120,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1001,52,70,224,101,-87,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,16,92,225,1101,59,24,225,102,83,48,224,101,-1162,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,80,10,225,101,5,143,224,1001,224,-21,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1102,94,67,224,101,-6298,224,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,102,2,223,223,1005,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,359,101,1,223,223,1108,677,677,224,102,2,223,223,1005,224,374,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,389,101,1,223,223,108,226,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,419,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,449,1001,223,1,223,8,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,479,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,494,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,554,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,614,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226
'''.strip().splitlines()

data=data2
#for line in data:

orig=[int(d) for d in data[0].split(',')]

data=orig[:]

# pc=0
# while True:
# 	d=data[pc]
# 	code=d%100; d//=100
# 	immediate1=(d%10)!=0; d//=10
# 	immediate2=(d%10)!=0; d//=10
# 	immediate3=(d%10)!=0
#
# 	if code==99: break
# 	a,b,c = data[pc+1],data[pc+2],data[pc+3]
# 	if code==1 or code==2:
# 		a,b = a if immediate1 else data[a],b if immediate2 else data[b]
# 	if code==1:
# 		data[c]=a+b
# 		pc += 4
# 	elif code==2:
# 		data[c]=a*b
# 		pc += 4
# 	elif code==3:
# 		data[a]=1
# 		pc += 2
# 	elif code==4:
# 		print('output', data[a])
# 		pc += 2
# 	else:
# 		print('oops')
# 		break


pc=0
while True:
	d=data[pc]
	code=d%100; d//=100
	immediate1=(d%10)!=0; d//=10
	immediate2=(d%10)!=0; d//=10
	immediate3=(d%10)!=0

	if code==99: break
	a,b,c = data[pc+1],data[pc+2] if pc+2 < len(data) else None,data[pc+3] if pc+3 < len(data) else None
	print(code, a, b, c)
	if code!=3 and code!=4:
		a,b = a if immediate1 else data[a],b if immediate2 else data[b]
		print(code, a, b, c)
	if code==1:
		print('data[', c, '] =', a, '+', b)
		data[c]=a+b
		pc += 4
	elif code==2:
		print('data[', c, '] =', a, '*', b)
		data[c]=a*b
		pc += 4
	elif code==3:
		b=5
		print('data[', a, '] =', b)
		data[a]=b
		pc += 2
	elif code==4:
		print('output', data[a])
		pc += 2
	elif code==5 or code==6:
		print('jump to ', b, 'if ', a, 'is', 'non-zero' if code==5 else 'zero')
		if a!=0 if code==5 else a==0:
			pc=b
		else:
			pc += 3
	elif code==7:
		print('data[', c, '] = 1 if ', a, '<', b, 'else 0')
		data[c] = 1 if a < b else 0
		pc += 4
	elif code==8:
		print('data[', c, '] = 1 if ', a, '==', b, 'else 0')
		data[c] = 1 if a == b else 0
		pc += 4
	else:
		print('oops')
		break
