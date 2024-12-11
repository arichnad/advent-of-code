#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading

#import lmfit

sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')
#from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

# data=data1;start=7;end=27
data=data2;start=200000000000000;end=400000000000000

#data = [int(line) for line in data]
data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)


# answer=0
# (x1, y1, z1, dx1, dy1, dz1) = data[0]
# (x2, y2, z2, dx2, dy2, dz2) = data[1]
# (x3, y3, z3, dx3, dy3, dz3) = data[3] #skipped one
#
# p1=[x1, y1, z1]
# d1=[dx1, dy1, dz1]
#
# d2=[dx2, dy2, dz2]
#
# p3=[x3, y3, z3]
# d3=[dx3, dy3, dz3]

# x0 + dx0 * t1 = x1 + dx1 * t1
# (x0 - x1) / (dx1 - dx0) = t1
# (x0 - x1) * (dy1 - dy0) = (y0 - y1) * (dx1 - dx0)


# planeNormal = numpy.cross(d1, d2)
# distance=numpy.dot(numpy.subtract(p1, p3), planeNormal) / (numpy.dot(d3, planeNormal))
# print(distance)
# print(p3 + numpy.multiply(d3, distance))

# import z3
# s = z3.Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')
x0,y0,z0,dx0,dy0,dz0=Reals('x0 y0 z0 dx0 dy0 dz0')
equations=[]
# equations=[
# 	x0 >= start, x0 <= end,
# 	y0 >= start, y0 <= end,
# 	z0 >= start, z0 <= end,
# ]
for i, line in enumerate(data[:3]):
	(x1, y1, z1, dx1, dy1, dz1) = line
	tVariable = Real('t' + str(i))
	equations += [
		tVariable > 0,
		x0 + dx0 * tVariable == x1 + dx1 * tVariable,
		y0 + dy0 * tVariable == y1 + dy1 * tVariable,
		z0 + dz0 * tVariable == z1 + dz1 * tVariable,
	]
s = z3.Solver()
s.add(equations)
print(s)
print(s.check())
if s.check() == sat:
	print(int(str(s.model()[x0])), int(str(s.model()[y0])), int(str(s.model()[z0])))
	print(int(str(s.model()[x0])) + int(str(s.model()[y0])) + int(str(s.model()[z0])))

# x0 + dx0 * t1 = x1 + dx1 * t1
# y0 + dy0 * t1 = y1 + dy1 * t1
# z0 + dz0 * t1 = z1 + dz1 * t1



# answer=0
# for i in range(len(data)):
# 	for j in range(i+1,len(data)):
# 		line1=data[i]
# 		line2=data[j]
# 		(x1, y1, z1, dx1, dy1, dz1) = line1
# 		(x2, y2, z2, dx2, dy2, dz2) = line2
#
# 		if dy1/dx1 == dy2/dx2: continue
# 		x = ((y2 - dy2/dx2 * x2) - (y1 - dy1/dx1 * x1)) / (dy1/dx1 - dy2/dx2)
# 		y = (dy1 / dx1) * x + (y1 - (dy1 / dx1) * x1)
# 		t1 = (y - y1) / dy1 if dy1 != 0 else (x - x1) / dx1
# 		t2 = (y - y2) / dy2 if dy2 != 0 else (x - x2) / dx2
#
# 		if t1<0 or t2 < 0:
# 			continue
# 		if start <= x <= end and start <= y <= end:
# 			answer+=1
#
# print(answer)




# fit_params = lmfit.Parameters()
# fit_params['x'] = lmfit.Parameter('x', value=24, min=0, max=end)
# fit_params['y'] = lmfit.Parameter('y', value=13, min=0, max=end)
# fit_params['z'] = lmfit.Parameter('z', value=10, min=0, max=end)
# fit_params['dx'] = lmfit.Parameter('dx', value=-3, min=-500, max=500)
# fit_params['dy'] = lmfit.Parameter('dy', value=1, min=-500, max=500)
# fit_params['dz'] = lmfit.Parameter('dz', value=2, min=-500, max=500)
# LARGE=1000000000000000000
#
# def myfunc(params, *args, **kws):
# 	# x1 = params['x'].value
# 	# y1 = params['y'].value
# 	# z1 = params['z'].value
# 	# dx1 = params['dx'].value
# 	# dy1 = params['dy'].value
# 	# dz1 = params['dz'].value
# 	# x1=24;y1=13;z1=10;dx1=-3;dy1=1;dz1=2
# 	(x1, y1, z1, dx1, dy1, dz1) = params
# 	residuals = []
# 	for line in data:
# 		(x2, y2, z2, dx2, dy2, dz2) = line
# 		residual=0
# 		tx = (x2 - x1) / (dx1 - dx2) if dx1 != dx2 else None
# 		# if tx is None and x1 != x2:
# 		# 	residuals.append(LARGE)
# 		# 	continue
# 		ty = (y2 - y1) / (dy1 - dy2) if dy1 != dy2 else None
# 		# if ty is None and y1 != y2:
# 		# 	residuals.append(LARGE)
# 		# 	continue
# 		tz = (z2 - z1) / (dz1 - dz2) if dz1 != dz2 else None
# 		# if tz is None and z1 != z2:
# 		# 	residuals.append(LARGE)
# 		# 	continue
# 		if tx is not None and ty is not None:
# 			residual += (tx - ty) * (tx - ty)
# 		if tx is not None and tz is not None:
# 			residual += (tx - tz) * (tx - tz)
# 		if tz is not None and ty is not None:
# 			residual += (tz - ty) * (tz - ty)
# 		residual = math.sqrt(residual)
# 		residuals.append(residual)
# 	print(x1, y1, z1, dx1, dy1, dz1, sum(residuals))
# 	return sum(residuals)

# result = lmfit.minimize(myfunc, fit_params, method='basinhopping', args=(data), max_nfev=0)
# print(lmfit.fit_report(result))

# from scipy.optimize import basinhopping
# x0 = (end//2, end//2, end//2, 10, 20, 30)
# minimizer_kwargs = {"method": "BFGS"}
# ret = basinhopping(myfunc, x0, minimizer_kwargs=minimizer_kwargs, niter=100)
# print(ret)
# print(myfunc(ret.x))
# from sympy import *
# x0,y0,z0,dx0,dy0,dz0=symbols('x0 y0 z0 dx0 dy0 dz0')
# tVariables=symbols('t1 t2 t3 t4 t5')
# equations=[
# 	x0-24,
# 	y0-13,
# 	z0-10,
# 	dx0--3,
# 	dy0-1,
# 	dz0-2,
# 	tVariables[0]-5,
# ]
# for i, line in enumerate(data):
# 	(x1, y1, z1, dx1, dy1, dz1) = line
# 	equations += [
# 		(x0 - x1) + tVariables[i] * (dx0 - dx1),
# 		(y1 - y0) + tVariables[i] * (dy0 - dy1),
# 		(z1 - z0) + tVariables[i] * (dz0 - dz1),
# 	]
# print(equations)
# print(nsolve(equations, [x0, y0, z0, dx0, dy0, dz0], [0, 0, 0, 0, 0, 0]))
# t2=symbols('t2	')
# (x2, y2, z2, dx2, dy2, dz2) = data[1]
