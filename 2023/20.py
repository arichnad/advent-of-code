#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''.strip('\n').splitlines()
data3='''
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''.strip('\n').splitlines()

data2='''

'''.strip('\n').splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)

m={}
num=0
for line in data:
	module,b = line.split(' -> ')
	b = b.split(', ')
	type=''
	if module.startswith('&'):
		type='&'
		module=module.replace('&','')
	elif module.startswith('%'):
		type='%'
		module=module.replace('%','')
	m[module] = [type, b, [], False, []]

for module in set(m.keys()):
	for child in m[module][1]:
		if child not in m:
			m[child] = ['', [], [], False, []]
		m[child][2].append(module)
		m[child][4].append(False)
output=[0, 0]
next=[]
def set(module, state, parentCalled):
	if module=='hp' and state==True:
		print(parentCalled, num)
	cur = m[module]
	# print(parentCalled, ' - ', 'high' if state else 'low', ' -> ', module)
	output[1 if state else 0] += 1

	if cur[0]=='%':
		if not state:
			cur[3] = not cur[3]
		else:
			return
	elif cur[0]=='&':
		answer=False
		for i,parent in enumerate(cur[2]):
			if parent==parentCalled:
				cur[4][i]=state
		for parent in cur[4]:
			if not parent:
				answer=True
		cur[3] = answer
	else:
		cur[3] = state

	for child in cur[1]:
		next.append((child, cur[3], module))

for i in range(5000):
	num+=1
	cur=[('broadcaster', False, 'button')]
	while len(cur)>0:
		next=[]
		for (a,b,c) in cur:
			set(a,b,c)
		cur=next
print(output) #18442, 44063
print(output[0]*output[1]) #812609846

print(math.lcm(3917, 3923, 3967, 4021)) #vq, sr, sn, rf




#dir=(dir+4)%4
#dx,dy=[(1,0),(0,1),(-1,0),(0,-1)][dir] #clockwise, starting right
#dir=1 if dy==1 else 3 if dx==0 else 0 if dx==1 else 2 #clockwise, starting right
#dir = "rdlu".find(ch.lower())

#data = [[column for column in line] for line in data]
#W,H=len(data[0]), len(data)
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

# m={}
#
# for line in data:
# 	module,b = line.split(' -> ')
# 	b = b.split(', ')
# 	type=''
# 	if module.startswith('&'):
# 		type='&'
# 		module=module.replace('&','')
# 	elif module.startswith('%'):
# 		type='%'
# 		module=module.replace('%','')
# 	m[module] = [type, b, [], False, []]
#
# for module in set(m.keys()):
# 	for child in m[module][1]:
# 		if child not in m:
# 			m[child] = ['', [], [], False, []]
# 		m[child][2].append(module)
# 		m[child][4].append(False)
# output=[0, 0]
# next=[]
# def set(module, state, parentCalled):
# 	cur = m[module]
# 	print(parentCalled, ' - ', 'high' if state else 'low', ' -> ', module)
# 	output[1 if state else 0] += 1
#
# 	if cur[0]=='%':
# 		if not state:
# 			cur[3] = not cur[3]
# 		else:
# 			return
# 	elif cur[0]=='&':
# 		answer=False
# 		for i,parent in enumerate(cur[2]):
# 			if parent==parentCalled:
# 				if cur[4][i]==state:
# 					True #return
# 				cur[4][i]=state
# 		for parent in cur[4]:
# 			if not parent:
# 				answer=True
# 		# print('ans', answer)
# 		cur[3] = answer
# 	else:
# 		cur[3] = state
#
# 	for child in cur[1]:
# 		next.append((child, cur[3], module))
#
#
# for i in range(1000):
# 	cur=[('broadcaster', False, 'button')]
# 	while len(cur)>0:
# 		next=[]
# 		for (a,b,c) in cur:
# 			set(a,b,c)
# 		cur=next
# 	print()
# print(output)
# print(output[0]*output[1])
