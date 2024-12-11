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
