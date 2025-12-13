#!/usr/bin/python3

# noinspection PyUnresolvedReferences
import math, re, sys, itertools, functools, copy, json, threading, random, heapq, time # list(itertools.permutations(range(4), 4)); heapq.heappush(a, 3)

# settings -> project -> python interpreter -> add new -> /usr/bin/pypy3 -> add new -> virtual environment .venv based on pypy3
# .venv/bin/pip3 install sortedcontainers astar z3-solver lmfit sympy shapely
# for lmfit:  sudo apt install python3-dev pypy3-dev libopenblas-dev gfortran
# for shapely:  sudo apt install python3-dev pypy3-dev libgeos-dev
# OR sudo apt install python3-dev pypy3-dev python3-sortedcontainers python3-z3 python3-sympy python3-shapely python3-numpy
sys.setrecursionlimit(100000)
# from sortedcontainers import SortedList #SortedList('bat') + 'cat'
# from astar import AStar #see astarExample.py
# from collections import defaultdict, deque, Counter
# from z3.z3 import * # s = Solver(); x = Real('x'); y = Real('y'); s.add([x <= 10, x >= 10]); print(s); print(s.check()); if s.check()==z3.sat: print(int(str(s.model()[x]))) #Int is sometimes slow, but also sometimes Real doesn't give you what you want
# import lmfit # try z3 first please
# from sympy import * # x,y=symbols('x y'); print(solve([x <= 10, x >= 10]))
# from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area)
# from testtemplate import *

data1='''
'''.strip('\n').splitlines()
data2='''
'''.strip('\n').splitlines()

data=data2

# data = [int(line) for line in data]; H=len(data)
data = [[column for column in re.findall('\S+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# python threads are not real:  thread=threading.Thread(target=lambda line: print(line), args=(line)); thread.start(); thread.join() # does not run in parallel on separate cores


# import numpy as np
#
# def getAInverse(guesses, buttons, joltage):
# 	buttonsSize = len(buttons)
# 	joltageSize = len(joltage)
#
# 	# if guesses is more than the difference between sizes of joltage and buttons, we'll probaly write over the end of the list
# 	A=[[1 if j in buttons[i] else 0 for i in range(buttonsSize)] for j in range(buttonsSize)]
#
# 	# linear algebra!  system of linear equations:   A * x = joltage
# 	# A = the equations
# 	# x = the answers
# 	# b = the right side of all those equations
# 	# x = aInverse * joltage
#
# 	#if buttonsSize > len(joltage), fill in the last few rows with guesses
#
# 	for i in range(guesses):
# 		j=joltageSize + i
# 		A[j][i]=1
#
# 	#make joltage vertical, and either crop it to buttonsSize or fill in zeros at the end
# 	paddedJoltage = np.pad(np.array(joltage).reshape(joltageSize, 1), ((0, guesses), (0,0)))
#
# 	for r in A:
# 		print(' '.join(str(r) for r in r))
# 	print()
# 	print(paddedJoltage)
# 	print()
#
# 	A = np.array(A)
# 	determinant = np.linalg.det(A)
# 	if determinant == 0:
# 		#ooof, let's add a guess
# 		return getAInverse(guesses+1, buttons, joltage)
# 	print()
# 	aInverse = np.linalg.inv(np.array(A))
#
# 	return guesses, aInverse, paddedJoltage


ans=0
MAX_SCORE=1_000_000
start = time.perf_counter()
for n, line in enumerate(data):
	_=line.pop(0)
	buttons=[]
	while line[0][0]=='(':
		b=line.pop(0)
		b=b.replace('(','').replace(')','').split(',')
		b=[int(b) for b in b]
		buttons.append(b)
	joltage=line[0]
	joltage=joltage.replace('{','').replace('}','').split(',')
	joltage=[int(j) for j in joltage]
	# presses=[set() for i in range(50)]
	# presses[0].add(tuple(joltage))
	buttonsSize = len(buttons)
	joltageSize = len(joltage)

	buttonsReversed = [[1 if j in buttons[i] else 0 for i in range(buttonsSize)] for j in range(joltageSize)]

	pool=[]

	previousButtonPresses=0
	while True:
		for j in range(10_000 if len(pool)==0 else 0):
			newEntry=[random.randrange(max(joltage)) for i in range(buttonsSize)]
			score = max(MAX_SCORE - sum(abs(sum(buttonsReversed[j][i] * newEntry[i] for i in range(buttonsSize)) - joltage[j]) for j in range(joltageSize)), 0)
			buttonPresses = sum(newEntry)
			pool.append((score, -buttonPresses, newEntry))
		pool=sorted(pool, reverse=True)[0:1_000]
		(bestScore, bestButtonPresses, bestEntry)=pool[0]

		# newPool=[]
		# sumScores=sum(p[0] for p in pool)
		# for addToPool in range(1_000):
		# 	pick = random.randrange(sumScores)
		# 	for (score, buttonPresses, entry) in pool:
		# 		pick -= score
		# 		if pick <= 0:
		# 			newPool.append((score, buttonPresses, entry))
		# 			break
		# pool=newPool
		#
		# bestScore=-1
		# for (score, buttonPresses, entry) in pool:
		# 	if score>bestScore or (score==bestScore and buttonPresses < bestButtonPresses):
		# 		(bestScore, bestButtonPresses, bestEntry)=(score, buttonPresses, entry)

		# print('  ', n, bestScore, bestButtonPresses, bestEntry, '%.2f'%((time.perf_counter()-start)/(n+1)))
		if bestScore==MAX_SCORE:
			if previousButtonPresses==bestButtonPresses:
				break
			previousButtonPresses=bestButtonPresses
		for i in range(len(pool)):
			for copy in range(10):
				(_, _, entry)=pool[i]
				newEntry=entry[:]
				for index in range(len(entry)):
					val = random.randint(-1, 1)
					newEntry[index]+=val
					newEntry[index]=max(min(newEntry[index],300), 0)
				score = max(MAX_SCORE - sum(abs(sum(buttonsReversed[j][i] * newEntry[i] for i in range(buttonsSize)) - joltage[j]) for j in range(joltageSize)), 0)
				buttonPresses = sum(newEntry)
				pool.append((score, -buttonPresses, newEntry))
	print(n, -bestButtonPresses, '%.2f'%((time.perf_counter()-start)/(n+1)))
	ans+=-bestButtonPresses


	# # ok, let's do this without z3!
	# # reorganize the information in the buttons array
	#
	# #NOTE:  if buttonsSize > len(joltage) then the last few buttons will have zeros in them
	# #NOTE:  if buttonsSize < len(joltage) then maybe we crop off a few joltage rows???  i'm not sure.
	#
	# guesses = max(buttonsSize-len(joltage), 0)
	#
	# guesses, aInverse, paddedJoltage = getAInverse(guesses, buttons, joltage)
	#
	# MAX = 300
	#
	# best=math.inf
	# for guess in itertools.product(range(0, MAX), repeat=guesses):
	# 	for i, j in enumerate(guess):
	# 		paddedJoltage[len(joltage) + i][0]=j
	# 	# print(guess, paddedJoltage)
	#
	# 	possibleAnswer = np.matmul(aInverse, paddedJoltage)
	# 	if any(possibleAnswer < 0):
	# 		continue
	# 	possibleAnswer = round(sum(sum(possibleAnswer)))
	#
	# 	if possibleAnswer < best:
	# 		best=possibleAnswer
	# print(best)
	# ans+=best


	# s = Optimize()
	# params=[]
	# for i in range(len(buttons)):
	# 	a = Int('a%d'%i)
	# 	s.add([a >= 0, a <= 300])
	# 	params.append(a)
	# rev=[[] for i in range(len(joltage))]
	# for i in range(len(buttons)):
	# 	for n in buttons[i]:
	# 		rev[n].append(i)
	# for i, r in enumerate(rev):
	# 	s.add(sum([params[r] for r in r]) == joltage[i])
	# s.minimize(sum(params))
	# if s.check()==z3.sat:
	# 	m=s.model()
	# 	print(sum(int(str(m[x])) for x in params))
	# 	ans+=sum(int(str(m[x])) for x in params)

	# done=False
	# for num in range(len(presses)):
	# 	curJoltages=presses[num]
	# 	print(num, len(curJoltages))
	# 	for curJoltage in curJoltages:
	# 		for b in buttons:
	# 			newJoltage=list(curJoltage)
	# 			done=True
	# 			good=True
	# 			for n in b:
	# 				if newJoltage[n]==0:
	# 					good=False
	# 					break
	# 				newJoltage[n]-=1
	# 			if good:
	# 				done=all(n==0 for n in newJoltage)
	# 				if done:
	# 					print('done', num+1)
	# 					ans+=num+1
	# 					break
	# 				presses[num+1].add(tuple(newJoltage))
	# 			done=False
	# 		if done: break
	# 	if done: break

	# import numpy as np
	# from lmfit import minimize, Parameters, Parameter, report_fit
	#
	# def fit(params, joltage):
	# 	joltage=joltage[:]
	# 	a=[]
	# 	for i in range(len(buttons)):
	# 		p=params['a%d'%(i)]+0
	# 		a.append(abs(p-round(p)))
	# 		a.append(p/100)
	# 		for n in buttons[i]:
	# 			joltage[n]-=p
	# 	a.extend(joltage)
	# 	# print([params['a%d'%(i)]+0 for i in range(len(buttons))], sum(a), a)
	# 	return a
	#
	# params = Parameters()
	# for i in range(len(buttons)):
	# 	params.add('a%d'%(i), value=1, min = 0, max = 300)
	# result = minimize(fit, params, args=(joltage,), method='leastsq')
	# print(fit(result.params, joltage))
	# print()
	# m=0
	# for i in range(len(buttons)):
	# 	r=result.params['a%d'%(i)]+0
	# 	print(r, end=' ')
	# 	m+=round(r)
	# print(m)
	# print()
	# ans+=m
	# # report_fit(result)
print(ans)


# ans=0
# for line in data:
# 	state=line.pop(0)
# 	state=state.replace('[','').replace(']','')
# 	state=[s=='#' for s in state]
# 	buttons=[]
# 	while line[0][0]=='(':
# 		b=line.pop(0)
# 		b=b.replace('(','').replace(')','').split(',')
# 		b=[int(b) for b in b]
# 		buttons.append(b)
# 	m=math.inf
#
# 	for i in range(1<<len(buttons)):
# 		curState=state[:]
# 		cur=0
# 		k=i
# 		changes=0
# 		for j in range(len(buttons)):
# 			if k&1!=0:
# 				changes+=1
# 				for n in buttons[j]:
# 					curState[n]=not curState[n]
# 			k>>=1
# 		if all(curState[n]==False for n in range(len(state))):
# 			if changes<m:
# 				m=changes
# 	print(state, buttons, m)
# 	ans+=m
# print(ans)

# dir = (dir+4)%4
# dx,dy = [(1,0),(0,1),(-1,0),(0,-1)][dir] # clockwise, starting right
# dir = 1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 # clockwise, starting right
# dir = 'rdlu'.find(d.lower()) # clockwise, starting right
# dir = ['right', 'down', 'left', 'up'].index(d.lower()) # clockwise, starting right
# dir = '>v<^'.find(d.lower()) # clockwise, starting right

# data = [[column for column in line] for line in data]
# for j in range(H):
# 	for i in range(W):
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				# if dx==0 and dy==0: continue
# 				if abs(dx)+abs(dy)!=1: continue
# 
# 				newY,newX=j+dy,i+dx
# 				if newY<0 or newX<0 or newY>=H or newX>=W: continue
# 
# for line in data: print(''.join(line))

# bfs simple queue
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, startY, startX)]
# costs={}
# while len(positions) > 0:
# 	# print(len(positions))
# 	newPositions = []
# 	for (cost, y, x) in sorted(positions): # remove sorted here if it's not needed
# 		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x] == '#': continue
# 		if y==endY and x==endX:
# 			print(cost)
# 			newPositions=[]
# 			break
# 		if (y, x) in costs and cost >= costs[(y, x)]: continue # change >= here to > if you need to analyze ties
# 		costs[(y, x)] = cost
# 
# 		for dy in range(-1, 2):
# 			for dx in range(-1, 2):
# 				# if dx==0 and dy==0: continue
# 				if abs(dx)+abs(dy)!=1: continue
# 				newPositions.append((cost + 1, y+dy, x+dx))
# 	positions=newPositions


# bfs (priority queue)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# positions = [(0, startY, startX)]
# costs={}
# while len(positions) > 0:
# 	(cost, y, x) = heapq.heappop(positions)
# 	if y<0 or y>=H or x<0 or x>=W: continue
# 	if data[y][x]=='#': continue
# 	if (y, x) in costs and cost >= costs[(y, x)]: continue
# 	costs[(y, x)] = cost
# 	
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			if (y+dy, x+dx) in costs and cost+1 >= costs[(y+dy, x+dx)]: continue
# 			heapq.heappush(positions, (cost+1, y+dy, x+dx))
# print(costs[(endY, endX)])

# flood fill does NOT work when want a breadth first (minimum cost, that sort of thing)
# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startY,startX=j,i
# 		if data[j][i]=='E': endY,endX=j,i
# visited=set()
# def ff(y, x):
# 	if y<0 or x<0 or y>=H or x>=W: return 0
# 	if data[y][x] == '#' or (y, x) in visited: return 0
# 	visited.add((y, x))
# 
# 	answer=1
# 	for dy in range(-1, 2):
# 		for dx in range(-1, 2):
# 			# if dx==0 and dy==0: continue
# 			if abs(dx)+abs(dy)!=1: continue
# 			answer+=ff(y+dy, x+dx)
# 	return answer
# 
# print(ff(startY, startX))

