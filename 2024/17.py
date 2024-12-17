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
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]; H=len(data)
data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()


#for line in data:
[a,b,c,dummy,data] = data

# a,b,c=a[0],b[0],c[0]
# pc=0
# while True:
# 	i=data[pc]
# 	literal=data[pc+1]
# 	if literal==4:
# 		combo=a
# 	elif literal==5:
# 		combo=b
# 	elif literal==6:
# 		combo=c
# 	else:
# 		combo=literal
#
#
# 	if i==0:
# 		a=a//(2 ** combo)
# 		pc+=2
# 	elif i==1:
# 		b=b^literal
# 		pc+=2
# 	elif i==2:
# 		b= combo % 8
# 		pc+=2
# 	elif i==3:
# 		if a!=0:
# 			pc=literal
# 		else:
# 			pc+=2
# 	elif i==4:
# 		b=b^c
# 		pc+=2
# 	elif i==5:
# 		print(combo%8, end=',')
# 		pc+=2
# 	elif i==6:
# 		b = a // (2 ** combo)
# 		pc += 2
# 	elif i == 7:
# 		c = a // (2 ** combo)
# 		pc += 2
# print()

def getA(aOriginal, aPosition):
	return aOriginal[aPosition] + \
			  (aOriginal[aPosition+1] if aPosition + 1 < len(aOriginal) else 0) * 8 + \
			  (aOriginal[aPosition+2] if aPosition + 2 < len(aOriginal) else 0) * (8*8) + \
			  (aOriginal[aPosition+3] if aPosition + 3 < len(aOriginal) else 0) * (8*8*8)


bOriginal,cOriginal=b[0],c[0]
aOriginal=[0, 0, 0, 0]
while True:
	b,c=bOriginal,cOriginal

	pc=0
	output=0
	aPosition=0
	a=getA(aOriginal, aPosition)
	# a=aOriginal[aPosition]
	while pc<len(data):
		i=data[pc]
		literal=data[pc+1]
		if literal==4:
			combo=a
		elif literal==5:
			combo=b
		elif literal==6:
			combo=c
		else:
			combo=literal


		if i==0:
			# a=a//(2 ** combo)
			aPosition+=1
			if aPosition+3>=len(aOriginal):
				break
			# a=aOriginal[aPosition]
			a = getA(aOriginal, aPosition)
			pc+=2
		elif i==1:
			b=b^literal
			pc+=2
		elif i==2:
			b= combo % 8
			pc+=2
		elif i==3:
			if a!=0:
				pc=literal
			else:
				pc+=2
		elif i==4:
			b=b^c
			pc+=2
		elif i==5:
			if combo%8 != data[output]: break
			output+=1
			pc+=2
		elif i==6:
			b = a // (2 ** combo)
			pc += 2
		elif i == 7:
			c = a // (2 ** combo)
			pc += 2
	# print(aOriginal, aPosition, output)
	if output==len(data):
		print(aOriginal)
		break
	if aPosition+3>=len(aOriginal):
		aOriginal.append(0)
	elif aOriginal[-1]+1 < 8:
		aOriginal[-1] += 1
	else:
		while aOriginal[-1]+1 >= 8:
			aOriginal.pop()
		aOriginal[-1]+=1
		while len(aOriginal)<4:
			aOriginal.append(0)
a = 0
for v in reversed(aOriginal):
	a *= 8
	a += (v % 8)
print(a)

b,c=bOriginal,cOriginal

pc=0
output=0
aPosition=0
while pc<len(data):
	i=data[pc]
	literal=data[pc+1]
	if literal==4:
		combo=a
	elif literal==5:
		combo=b
	elif literal==6:
		combo=c
	else:
		combo=literal


	if i==0:
		a=a//(2 ** combo)
		pc+=2
	elif i==1:
		b=b^literal
		pc+=2
	elif i==2:
		b= combo % 8
		pc+=2
	elif i==3:
		if a!=0:
			pc=literal
		else:
			pc+=2
	elif i==4:
		b=b^c
		pc+=2
	elif i==5:
		print(combo%8,end=',')
		pc+=2
	elif i==6:
		b = a // (2 ** combo)
		pc += 2
	elif i == 7:
		c = a // (2 ** combo)
		pc += 2
print()

# 2,4 b=a%8
# 1,6 b=b^6
# 7,5 c=a//(2**b)
# 4,6 b=b^c
# 1,4 b=b^4
# 5,5 output b%8
# 0,3 a//=8
# 3,0 jnz 0
#
# b=(a%8)^6
# c=a//(2**b)
# b=b^c^4
# output b%8
# a//=8
# jnz 0

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

# positions = [(0, startX, startY)]
# costs={}
# while len(positions) > 0:
# 	newPositions = []
# 	for (cost, x, y) in sorted(positions):
# 		if data[y][x] == '#': continue
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue
# 		costs[(x, y)] = cost
#
# 		newPositions.append((cost + 1, x + 1, y))
# 		newPositions.append((cost + 1, x - 1, y))
# 		newPositions.append((cost + 1, x, y - 1))
# 		newPositions.append((cost + 1, x, y + 1))
# 	positions=newPositions
# print(costs[(endX, endY)])

# # flood fill does NOT work when want a breadth first (minimum cost, that sort of thing)
# visited=set()
# def ff(x, y):
# 	if y<0 or x<0 or y>=H or x>=W: return
# 	if data[y][x] == '#' or (x, y) in visited: return
# 	visited.add((x, y))
# 	ff(x + 1, y)
# 	ff(x - 1, y)
# 	ff(x, y + 1)
# 	ff(x, y - 1)
#
# ff(startX, startY)
