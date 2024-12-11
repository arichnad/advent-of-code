#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading
sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
#from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')

data1='''
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
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

p=False
parts=[]
rules={}
for line in data:
	if line=='':
		p=True
		continue
	if p:
		parts.append([int(column) for column in re.findall('-?[\d]+', line)])
	else:
		a,b=line.split('{')
		b=b.replace('}','')
		b=b.split(',')
		next=b.pop()
		bOut=[]
		for curB in b:
			c,d=curB.split(':')
			bOut.append(('xmas'.index(c[0]),c[1],int(c[2:]),d))
		rules[a]=(bOut,next)

answer=0
MIN,MAX=1,4000

def add(a, position, inputRange):
	c=[]
	for i in range(len(a)):
		if i==position:
			(minA,maxA)=a[i]
			(minB,maxB)=inputRange
			c.append((max(minA,minB), min(maxA,maxB)))
		else:
			c.append(a[i])
	return c

START=[(MIN,MAX) for i in range(4)]
REJECT_START=[(0,-1) for i in range(4)]

def recurse(rule, rulePart, prefix):
	if rule == 'R':
		return 0
	if rule == 'A':
		output=1
		for r in prefix:
			output*=r[1]-r[0]+1
		return output
	cur = rules[rule]
	if rulePart == len(cur[0]):
		return recurse(cur[1], 0, prefix)
	r = cur[0][rulePart]
	print(rule, rulePart, r)
	gt=r[1] == '>'
	added = (r[2]+1,MAX) if gt else (MIN,r[2]-1)
	subtracted = (MIN, r[2]) if gt else (r[2],MAX)
	return recurse(r[3], 0, add(prefix, r[0], added)) + \
		recurse(rule, rulePart+1, add(prefix, r[0], subtracted))

print(recurse('in', 0, START))




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

# p=False
# parts=[]
# rules={}
# for line in data:
# 	if line=='':
# 		p=True
# 		continue
# 	if p:
# 		parts.append([int(column) for column in re.findall('-?[\d]+', line)])
# 	else:
# 		a,b=line.split('{')
# 		b=b.replace('}','')
# 		b=b.split(',')
# 		next=b.pop()
# 		print(a,b,next)
# 		bOut=[]
# 		for curB in b:
# 			c,d=curB.split(':')
# 			bOut.append(('xmas'.index(c[0]),c[1],int(c[2:]),d))
# 		rules[a]=(bOut,next)
#
# print(rules)
# print(parts)
# answer=0
# for part in parts:
# 	rule='in'
# 	while True:
# 		print(part, rule)
# 		cur=rules[rule]
# 		rule=None
# 		for r in cur[0]:
# 			gt = r[1]=='>'
# 			if gt and part[r[0]] > r[2] or not gt and part[r[0]] < r[2]:
# 				rule=r[3]
# 				break
# 		else:
# 			rule=cur[1]
# 			print('going with', rule)
# 		if rule=='A':
# 			answer+=sum(part)
# 			break
# 		elif rule == 'R':
# 			break
# print(answer)
