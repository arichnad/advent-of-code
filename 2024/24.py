#!/usr/bin/python3

# noinspection PyUnresolvedReferences
# WHOLE FILE:  noinspection PyUnboundLocalVariable
import math, re, sys, itertools, functools, copy, json, threading, numpy, random, bisect, heapq, time # list(itertools.permutations(range(4), 4))
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
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0
'''.strip('\n').splitlines()
data1G='''
x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
'''.strip('\n').splitlines()
data1='''
x00: 1
x01: 1
y00: 1
y01: 1
'''.strip('\n').splitlines()
data1G='''
x00 XOR y00 -> z01
x00 AND y00 -> z00
'''.strip('\n').splitlines()
data2='''

'''.strip('\n').splitlines()
data2G=open('24.txt', 'r').read().strip('\n').splitlines()

# data=data1;dataG=data1G
data=data2;dataG=data2G
# data = [int(line) for line in data]; H=len(data)
# data = [[int(column) for column in re.findall('-?\d+', line)] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [[int(column) for column in line.split(',')] for line in data]; W,H=len(data[0]),len(data)
# data = [[column for column in line] for line in data]; W,H=len(data[0]),len(data)
# data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()

value={}
for line in data:
	a,b=line.split(': ')
	value[a]=(b == '1')

# change=True
# while change:
# 	change=False
# 	for line in dataG:
# 		a,gate,b,dummy,out=line.split(' ')
# 		if a in value and b in value:
# 			a = value[a]
# 			b = value[b]
# 		else:
# 			continue
# 		if out in value: continue
# 		change=True
# 		if gate=='AND':
# 			value[out] = a and b
# 		elif gate=='OR':
# 			value[out] = a or b
# 		elif gate=='XOR':
# 			value[out] = a ^ b
#
# answer=0
# for a in reversed(sorted(value.keys())):
# 	if not a.startswith('z'): continue
# 	answer*=2
# 	answer+=1 if value[a] else 0
# print(answer)

check=20
# random.seed(10) ##########################################
gates= {}

outputs=set()
for line in dataG:
	a, gate, b, dummy, out = line.split(' ')
	gates[out] = ([a, gate, b])
	if out in value: continue
	outputs.add(out)
outputs=sorted(outputs)
gatesOriginal=copy.deepcopy(gates)


xIn = [i for i in sorted(value.keys()) if i.startswith('x')]
yIn = [i for i in sorted(value.keys()) if i.startswith('y')]
zOut = [i for i in outputs if i.startswith('z')]
N=len(zOut)

numsX=[2**i-1 for i in range(N)] + [random.randrange(2**(N-1)) for i in range(check)]
numsY=[1 for i in range(N)] + [random.randrange(2**(N-1)) for i in range(check)]

value = {}
xTemp=numsX[:]
for a in xIn:
	value[a]=[(xTemp[i]&1) != 0 for i in range(len(xTemp))]
	for i in range(len(xTemp)): xTemp[i]//=2
yTemp=numsY[:]
for a in yIn:
	value[a]=[(yTemp[i] & 1) != 0 for i in range(len(yTemp))]
	for i in range(len(yTemp)): yTemp[i] //= 2
startValue=value
rightAnswer=[numsX[i] + numsY[i] for i in range(len(numsX))]


###
value={}
xTemp=numsY[:]
for a in xIn:
	value[a]=[(xTemp[i]&1) != 0 for i in range(len(xTemp))]
	for i in range(len(xTemp)): xTemp[i]//=2
yTemp=numsX[:]
for a in yIn:
	value[a]=[(yTemp[i] & 1) != 0 for i in range(len(yTemp))]
	for i in range(len(yTemp)): yTemp[i] //= 2
startValue2=value
###

def findCorrect(startValue):
	global N
	value=copy.deepcopy(startValue)

	change=True
	while change:
		change=False
		for out, (a, gate, b) in gates.items():
			if out in value or a not in value or b not in value: continue
			a = value[a]
			b = value[b]
			change=True
			if gate=='AND':
				value[out] = [a[i] and b[i] for i in range(len(a))]
			elif gate=='OR':
				value[out] = [a[i] or b[i] for i in range(len(a))]
			elif gate=='XOR':
				value[out] = [a[i] ^ b[i] for i in range(len(a))]


	for j in range(len(rightAnswer)):
		tempRightAnswer=rightAnswer[:]
		for a in zOut:
			if a not in value: return None
			if value[a][j]!=((tempRightAnswer[j]&1) != 0):
				return -j
			for i in range(len(tempRightAnswer)): tempRightAnswer[i] //= 2
	return -len(rightAnswer)

#######
positions=[([], set())]
swapsSet=set()
start_time = time.time()
for k in range(4):
	newPositions = []
	print('***', positions)
	best,bestSwap=None,None
	for (swapsList, swapsSet) in positions:
		for swapA,swapB in swapsList:
			s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s

		for swapA in outputs:
			if swapA in swapsSet: continue
			for swapB in outputs:
				if swapB <= swapA or swapB in swapsSet: continue

				s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
				correct1=findCorrect(startValue)
				correct2=findCorrect(startValue2)
				s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s

				if correct1 is None or correct2 is None:
					continue

				correct = max(correct1, correct2)
				if best is None or correct<best:
					newPositions=[]
					best=correct
					print(len(swapsList), correct)
				if correct <= best:
					newSwapsList=swapsList.copy()
					heapq.heappush(newSwapsList, (swapA, swapB))
					newSwapsSet = swapsSet.copy()
					newSwapsSet.add(swapA)
					newSwapsSet.add(swapB)
					newPositions.append((newSwapsList, newSwapsSet))
					# print('.', end='')

		for swapA,swapB in reversed(swapsList):
			s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s

	if gates != gatesOriginal: print('oof')
	positions = newPositions

print(time.time() - start_time)
for (swapsList, swapsSet) in positions:
	for swapA,swapB in swapsList:
		s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
	print('done', swapsList, ','.join(sorted([i[0] for i in swapsList] + [i[1] for i in swapsList])), findCorrect(startValue), findCorrect(startValue2))
	for swapA,swapB in reversed(swapsList):
		s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s


sys.exit(0)


#######
# positions = [(findCorrect(), [], set())]
# print('start', positions)
# visited = set()
# start_time = time.time()
# while len(positions) > 0:
# 	# if len(visited)>=10000: break
# 	(c, swapsList, swapsSet) = positions[0]
# 	print(len(positions), len(visited), (c, swapsList))
#
# 	for (a,b) in swapsList:
# 		s=gates[a]; gates[a]=gates[b]; gates[b]=s
#
# 	swappable = {}
# 	for j in xIn, yIn:
# 		for i in j:
# 			swappable[i] = set(outputs)
# 	change=True
# 	while change:
# 		change=False
# 		for out, (a, gate, b) in gates.items():
# 			if out in swappable or a not in swappable or b not in swappable: continue
# 			change=True
# 			swappable[out] = set(i for i in swappable[a] if i in swappable[b] and i != out and i not in swapsSet)
#
# 	for swapA in outputs:
# 		if swapA in swapsSet: continue
# 		for swapB in swappable[swapA]:
# 			if swapB <= swapA or swapA not in swappable[swapB]: continue
#
# 			newSwapsList=swapsList.copy()
# 			heapq.heappush(newSwapsList, (swapA, swapB))
#
# 			newSwapsTuple=tuple(newSwapsList)
# 			if newSwapsTuple in visited: continue
# 			visited.add(newSwapsTuple)
#
# 			s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
# 			correct=findCorrect()
# 			s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
#
# 			if correct is None:
# 				print('oof')
# 				continue
#
# 			if correct==-len(rightAnswer):
# 				print('done', correct, newSwapsList, ','.join(sorted([i[0] for i in newSwapsList] + [i[1] for i in newSwapsList])))
# 				sys.exit(0)
#
# 			if len(newSwapsList)==4: continue
#
# 			newSwapsSet = swapsSet.copy()
# 			newSwapsSet.add(swapA)
# 			newSwapsSet.add(swapB)
#
# 			heapq.heappush(positions, (correct+len(newSwapsList)*1000, newSwapsList, newSwapsSet))
# 			break
# 		else: continue
# 		break
# 	else:
# 		heapq.heappop(positions)
#
# 	for (a,b) in reversed(swapsList):
# 		s=gates[a]; gates[a]=gates[b]; gates[b]=s
#
# print(time.time() - start_time) #9.3
# sys.exit(0)




# bests = []
# scores = []
# totalScores = 0
#
# best=None
# for swapA in outputs:
# 	print(swapA)
# 	for swapB in outputs:
# 		if swapA <= swapB: continue
# 		s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
# 		correct = findCorrect()
# 		s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
# 		if correct is None: continue
#
# 		if best is None or correct < best:
# 			best,bestA,bestB = correct,swapA,swapB
# 			print(swapA, swapB, correct)
# 		correct = int(64**(correct/len(rightAnswer)))
# 		scores.append((correct, swapA, swapB))
# 		totalScores+=correct
#
# 	# s = gates[bestA]; gates[bestA] = gates[bestB]; gates[bestB] = s
# 	# bests.append(bestA)
# 	# bests.append(bestB)
# scores=list(reversed(sorted(scores)))
# print(scores[0], scores[1], scores[2])
#
# best=None
# while True:
# 	swapA = random.randrange(0, totalScores)
# 	while True:
# 		swapB = random.randrange(0, totalScores)
# 		if swapB != swapA: break
# 	while True:
# 		swapC = random.randrange(0, totalScores)
# 		if swapC != swapB and swapC != swapA: break
# 	while True:
# 		swapD = random.randrange(0, totalScores)
# 		if swapD != swapC and swapD != swapB and swapD != swapA: break
#
# 	# swapA=0
# 	# swapB=swapA+scores[0][0]+1
# 	# swapC=swapB+scores[1][0]+1
# 	# swapD=swapC+scores[2][0]+1
#
# 	bestA,bestB,bestC,bestD,bestE,bestF,bestG,bestH=None,None,None,None,None,None,None,None
# 	for score in scores:
# 		s=score[0]
# 		if swapA is not None:
# 			swapA-=s
# 			if swapA<=0:
# 				(_,bestA,bestB)=score
# 				swapA=None
# 		if swapB is not None:
# 			swapB-=s
# 			if swapB<=0:
# 				(_,bestC,bestD)=score
# 				swapB=None
# 		if swapC is not None:
# 			swapC-=s
# 			if swapC<=0:
# 				(_,bestE,bestF)=score
# 				swapC=None
# 		if swapD is not None:
# 			swapD-=s
# 			if swapD<=0:
# 				(_,bestG,bestH)=score
# 				swapD=None
# 	s = gates[bestG]; gates[bestG] = gates[bestH]; gates[bestH] = s
# 	s = gates[bestE]; gates[bestE] = gates[bestF]; gates[bestF] = s
# 	s = gates[bestC]; gates[bestC] = gates[bestD]; gates[bestD] = s
# 	s = gates[bestA]; gates[bestA] = gates[bestB]; gates[bestB] = s
#
# 	correct=findCorrect()
#
# 	if correct is not None and (best is None or correct<best):
# 		best=correct
# 		print(bestA, bestB, bestC, bestD, bestE, bestF, bestG, bestH, correct)
# 	if correct == 0:
# 		print(','.join(sorted([bestA, bestB, bestC, bestD, bestE, bestF, bestG, bestH])), correct)
# 		break
#
# 	s = gates[bestA]; gates[bestA] = gates[bestB]; gates[bestB] = s
# 	s = gates[bestC]; gates[bestC] = gates[bestD]; gates[bestD] = s
# 	s = gates[bestE]; gates[bestE] = gates[bestF]; gates[bestF] = s
# 	s = gates[bestG]; gates[bestG] = gates[bestH]; gates[bestH] = s


# bests = []
# for ii in range(4):
# 	best = None
#
# 	for swapA in outputs:
# 		for swapB in outputs:
# 			if swapA == swapB: continue
# 			s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
# 			value=copy.deepcopy(startValue)
#
# 			change=True
# 			while change:
# 				change=False
# 				for out, (a, gate, b) in gates.items():
# 					if out in value or a not in value or b not in value: continue
# 					a = value[a]
# 					b = value[b]
# 					change=True
# 					if gate=='AND':
# 						value[out] = [a[i] and b[i] for i in range(len(a))]
# 					elif gate=='OR':
# 						value[out] = [a[i] or b[i] for i in range(len(a))]
# 					elif gate=='XOR':
# 						value[out] = [a[i] ^ b[i] for i in range(len(a))]
#
#
# 			correct=0
# 			# answer=0
# 			tempRightAnswer=rightAnswer[:]
# 			for a in zOut:
# 				# answer*=2
# 				# answer+=1 if value[a] else 0
# 				if a not in value: continue
# 				for i in range(len(rightAnswer)):
# 					if value[a][i]==((tempRightAnswer[i]&1) != 0):
# 						correct += 1
# 				for i in range(len(tempRightAnswer)): tempRightAnswer[i] //= 2
#
# 			s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
# 			if best is None or correct > best:
# 				best,bestA,bestB = correct,swapA,swapB
# 				print(ii, swapA, swapB, correct, len(numsX)*N)
#
# 	s = gates[bestA]; gates[bestA] = gates[bestB]; gates[bestB] = s
# 	bests.append(bestA)
# 	bests.append(bestB)
# print(','.join(sorted(bests))) #btg,crj,gnj,gsw,pfn,tpk,wkb,z23

# N=46
# check=5
#
# gates= {}
#
# outputs=set()
# for line in dataG:
# 	a, gate, b, dummy, out = line.split(' ')
# 	gates[out] = ([a, gate, b])
# 	if out in value: continue
# 	outputs.add(out)
#
# xIn = [i for i in sorted(value.keys()) if i.startswith('x')]
# yIn = [i for i in sorted(value.keys()) if i.startswith('y')]
# zOut = [i for i in sorted(outputs) if i.startswith('z')]
#
# numsX=[random.randrange(0, 2**N) for i in range(check)]
# numsY=[random.randrange(0, 2**N) for i in range(check)]
#
# value = {}
# xTemp=numsX[:]
# for a in xIn:
# 	value[a]=[(xTemp[i]&1) != 0 for i in range(len(xTemp))]
# 	for i in range(len(xTemp)): xTemp[i]//=2
# yTemp=numsY[:]
# for a in yIn:
# 	value[a]=[(yTemp[i] & 1) != 0 for i in range(len(yTemp))]
# 	for i in range(len(yTemp)): yTemp[i] //= 2
# startValue=value
# rightAnswer=[numsX[i] + numsY[i] for i in range(len(numsX))]
#
# bests = []
# for ii in range(2):
# 	best = None
#
# 	for swapA in outputs:
# 		print(swapA)
# 		for swapB in outputs:
# 			if swapA == swapB: continue
# 			for swapC in outputs:
# 				if swapC == swapB or swapC == swapA: continue
# 				for swapD in outputs:
# 					if swapD == swapC or swapD == swapB or swapD == swapA: continue
# 					s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
# 					s=gates[swapC]; gates[swapC]=gates[swapD]; gates[swapD]=s
# 					value=copy.deepcopy(startValue)
#
# 					change=True
# 					while change:
# 						change=False
# 						for out, (a, gate, b) in gates.items():
# 							if out in value or a not in value or b not in value: continue
# 							a = value[a]
# 							b = value[b]
# 							change=True
# 							if gate=='AND':
# 								value[out] = [a[i] and b[i] for i in range(len(a))]
# 							elif gate=='OR':
# 								value[out] = [a[i] or b[i] for i in range(len(a))]
# 							elif gate=='XOR':
# 								value[out] = [a[i] ^ b[i] for i in range(len(a))]
#
#
# 					correct=0
# 					# answer=0
# 					tempRightAnswer=rightAnswer[:]
# 					for a in zOut:
# 						# answer*=2
# 						# answer+=1 if value[a] else 0
# 						if a not in value: continue
# 						for i in range(len(rightAnswer)):
# 							if value[a][i]==((tempRightAnswer[i]&1) != 0):
# 								correct += 1
# 						for i in range(len(tempRightAnswer)): tempRightAnswer[i] //= 2
#
# 					s=gates[swapA]; gates[swapA]=gates[swapB]; gates[swapB]=s
# 					s=gates[swapC]; gates[swapC]=gates[swapD]; gates[swapD]=s
# 					if best is None or correct > best:
# 						best,bestA,bestB,bestC,bestD = correct,swapA,swapB,swapC,swapD
# 						print(ii, swapA, swapB, swapC, swapD, correct, len(numsX)*N)
#
# 	s = gates[bestA]; gates[bestA] = gates[bestB]; gates[bestB] = s
# 	s = gates[bestC]; gates[bestC] = gates[bestD]; gates[bestD] = s
# 	bests.append(bestA)
# 	bests.append(bestB)
# 	bests.append(bestC)
# 	bests.append(bestD)
# print(','.join(sorted(bests)))

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

# for j in range(H):
# 	for i in range(W):
# 		if data[j][i]=='S': startX,startY=i,j
# 		if data[j][i]=='E': endX,endY=i,j
# positions = [(0, startX, startY)]
# costs={}
# while len(positions) > 0:
# 	newPositions = []
# 	for (cost, x, y) in sorted(positions): #remove sorted here if it's not needed
#		if y<0 or y>=H or x<0 or x>=W: continue
# 		if data[y][x] == '#': continue
# 		if (x, y) in costs and cost >= costs[(x, y)]: continue #change >= here to > if you need to analyze ties
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
